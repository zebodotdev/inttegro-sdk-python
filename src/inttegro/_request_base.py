from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, fields
from enum import Enum
from typing import Any


class UnsetType:
    """Sentinel type used for request fields that were not supplied."""

    __slots__ = ()

    def __repr__(self) -> str:
        return "UNSET"

    def __bool__(self) -> bool:
        return False


UNSET = UnsetType()


@dataclass(frozen=True, slots=True, kw_only=True)
class ApiRequest:
    """Base class for immutable, JSON-serializable API request objects."""

    def to_dict(self) -> dict[str, Any]:
        payload: dict[str, Any] = {}
        for request_field in fields(self):
            value = getattr(self, request_field.name)
            if value is UNSET:
                continue
            wire_name = str(
                request_field.metadata.get("wire_name", request_field.name)
            )
            payload[wire_name] = encode_request_value(value)
        return payload


def encode_request_value(value: Any) -> Any:
    """Convert request objects and nested values into JSON-compatible data."""

    if value is UNSET:
        raise ValueError("UNSET cannot be serialized outside an optional request field")
    if isinstance(value, ApiRequest):
        return value.to_dict()
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, Mapping):
        return {
            str(key): encode_request_value(item)
            for key, item in value.items()
            if item is not UNSET
        }
    if isinstance(value, (list, tuple)):
        return [encode_request_value(item) for item in value]
    return value
