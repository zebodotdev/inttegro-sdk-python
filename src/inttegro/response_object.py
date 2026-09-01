from __future__ import annotations

from typing import Any, Iterator


class ResponseObject:
    """
    Lightweight wrapper that allows attribute and dict-style access.
    """

    def __init__(self, data: dict[str, Any] | list[Any] | None = None):
        raw = data or {}
        if isinstance(raw, dict):
            self._data = {k: self._wrap(v) for k, v in raw.items()}
        elif isinstance(raw, list):
            self._data = [self._wrap(v) for v in raw]
        else:
            self._data = raw

    def __getattr__(self, name: str) -> Any:
        if isinstance(self._data, dict) and name in self._data:
            return self._data[name]
        raise AttributeError(name)

    def __getitem__(self, key: Any) -> Any:
        return self._data[key]

    def __iter__(self) -> Iterator:
        if isinstance(self._data, dict):
            return iter(self._data)
        if isinstance(self._data, list):
            return iter(self._data)
        return iter([])

    def __len__(self) -> int:
        return len(self._data)

    def to_dict(self) -> Any:
        return self._unwrap(self._data)

    def _wrap(self, value: Any) -> Any:
        if isinstance(value, dict):
            return ResponseObject(value)
        if isinstance(value, list):
            return [self._wrap(v) for v in value]
        if isinstance(value, ResponseObject):
            return value
        return value

    def _unwrap(self, value: Any) -> Any:
        if isinstance(value, dict):
            return {k: self._unwrap(v) for k, v in value.items()}
        if isinstance(value, list):
            return [self._unwrap(v) for v in value]
        if isinstance(value, ResponseObject):
            return value.to_dict()
        return value
