from __future__ import annotations

import types
from collections.abc import Iterator, Mapping
from dataclasses import fields
from functools import lru_cache
from typing import Any, Literal, TypeVar, Union, get_args, get_origin, get_type_hints


ModelT = TypeVar("ModelT", bound="ApiModel")


class ModelDecodeError(ValueError):
    """Raised when a wire value cannot be decoded as its declared API type."""


class ApiModel(Mapping[str, Any]):
    """Read-only, typed API response with backwards-compatible mapping access."""

    __slots__ = ("_extra", "_present_fields")

    @classmethod
    def from_dict(cls: type[ModelT], value: Mapping[str, Any]) -> ModelT:
        decoded = decode_value(cls, value)
        if not isinstance(decoded, cls):
            raise ModelDecodeError(f"expected {cls.__name__}, got {type(decoded).__name__}")
        return decoded

    def __getitem__(self, key: str) -> Any:
        attribute = _attribute_for_wire_name(type(self), key)
        if attribute is not None and attribute in self._present_fields:
            return object.__getattribute__(self, attribute)
        try:
            return self._extra[key]
        except KeyError:
            raise KeyError(key) from None

    def __iter__(self) -> Iterator[str]:
        for model_field in fields(self):
            if model_field.name in self._present_fields:
                yield _wire_name(model_field)
        yield from self._extra

    def __len__(self) -> int:
        return len(self._present_fields) + len(self._extra)

    def __repr__(self) -> str:
        values = ", ".join(f"{name}={value!r}" for name, value in self.items())
        return f"{type(self).__name__}({values})"

    def to_dict(self) -> dict[str, Any]:
        return {name: encode_value(value) for name, value in self.items()}


@lru_cache(maxsize=None)
def _model_hints(model_type: type[ApiModel]) -> dict[str, Any]:
    return get_type_hints(model_type)


@lru_cache(maxsize=None)
def _attribute_for_wire_name(model_type: type[ApiModel], wire_name: str) -> str | None:
    for model_field in fields(model_type):
        if _wire_name(model_field) == wire_name:
            return model_field.name
    return None


def _wire_name(model_field: Any) -> str:
    return str(model_field.metadata.get("wire_name", model_field.name))


def decode_value(annotation: Any, value: Any) -> Any:
    """Decode JSON-compatible data into generated response model instances."""

    if annotation is Any or annotation is object:
        return value
    if value is None:
        if annotation is type(None) or type(None) in get_args(annotation):
            return None
        raise ModelDecodeError(f"null is not valid for {annotation!r}")

    origin = get_origin(annotation)
    arguments = get_args(annotation)

    if origin is Literal:
        if value not in arguments:
            raise ModelDecodeError(f"{value!r} is not one of {arguments!r}")
        return value
    if origin in (Union, types.UnionType):
        errors: list[Exception] = []
        for candidate in arguments:
            if candidate is type(None):
                continue
            try:
                return decode_value(candidate, value)
            except (ModelDecodeError, TypeError, ValueError) as error:
                errors.append(error)
        raise ModelDecodeError(f"value does not match {annotation!r}: {errors!r}")
    if origin is list:
        if not isinstance(value, list):
            raise ModelDecodeError(f"expected list, got {type(value).__name__}")
        item_type = arguments[0] if arguments else Any
        return [decode_value(item_type, item) for item in value]
    if origin is dict:
        if not isinstance(value, dict):
            raise ModelDecodeError(f"expected object, got {type(value).__name__}")
        key_type, value_type = arguments if len(arguments) == 2 else (Any, Any)
        return {
            decode_value(key_type, key): decode_value(value_type, item)
            for key, item in value.items()
        }

    if isinstance(annotation, type) and issubclass(annotation, ApiModel):
        if not isinstance(value, Mapping):
            raise ModelDecodeError(f"expected object for {annotation.__name__}")
        instance = annotation.__new__(annotation)
        hints = _model_hints(annotation)
        present: set[str] = set()
        consumed: set[str] = set()
        for model_field in fields(annotation):
            wire_name = _wire_name(model_field)
            if wire_name not in value:
                continue
            field_type = hints.get(model_field.name, Any)
            object.__setattr__(instance, model_field.name, decode_value(field_type, value[wire_name]))
            present.add(model_field.name)
            consumed.add(wire_name)
        object.__setattr__(instance, "_present_fields", frozenset(present))
        object.__setattr__(instance, "_extra", {key: item for key, item in value.items() if key not in consumed})
        return instance

    if annotation is float:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ModelDecodeError(f"expected float, got {type(value).__name__}")
        return value
    if annotation in (str, int, bool):
        if not isinstance(value, annotation) or (annotation is int and isinstance(value, bool)):
            raise ModelDecodeError(f"expected {annotation.__name__}, got {type(value).__name__}")
        return value
    return value


def encode_value(value: Any) -> Any:
    """Convert generated response models back into JSON-compatible values."""

    if isinstance(value, ApiModel):
        return value.to_dict()
    if isinstance(value, list):
        return [encode_value(item) for item in value]
    if isinstance(value, tuple):
        return [encode_value(item) for item in value]
    if isinstance(value, Mapping):
        return {key: encode_value(item) for key, item in value.items()}
    return value
