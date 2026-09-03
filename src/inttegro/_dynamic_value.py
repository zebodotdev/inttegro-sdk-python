from __future__ import annotations

from collections.abc import Iterator
from typing import Any


class DynamicValue:
    """Internal mapping-and-attribute view for undocumented transport payloads."""

    _data: dict[str, Any] | list[Any]

    def __init__(self, data: dict[str, Any] | list[Any] | None = None) -> None:
        raw = {} if data is None else data
        if isinstance(raw, dict):
            self._data = {key: self._wrap(value) for key, value in raw.items()}
        else:
            self._data = [self._wrap(value) for value in raw]

    def __getattr__(self, name: str) -> Any:
        if isinstance(self._data, dict) and name in self._data:
            return self._data[name]
        raise AttributeError(name)

    def __getitem__(self, key: Any) -> Any:
        return self._data[key]

    def __iter__(self) -> Iterator[Any]:
        return iter(self._data)

    def __len__(self) -> int:
        return len(self._data)

    def to_dict(self) -> dict[str, Any] | list[Any]:
        value = self._unwrap(self._data)
        if not isinstance(value, (dict, list)):
            raise TypeError("dynamic value root must be an object or list")
        return value

    def _wrap(self, value: Any) -> Any:
        if isinstance(value, dict):
            return DynamicValue(value)
        if isinstance(value, list):
            return [self._wrap(item) for item in value]
        if isinstance(value, DynamicValue):
            return value
        return value

    def _unwrap(self, value: Any) -> Any:
        if isinstance(value, dict):
            return {key: self._unwrap(item) for key, item in value.items()}
        if isinstance(value, list):
            return [self._unwrap(item) for item in value]
        if isinstance(value, DynamicValue):
            return value.to_dict()
        return value
