from __future__ import annotations

from dataclasses import dataclass
from collections.abc import Mapping
from typing import Generic, TypeVar, Any


T = TypeVar("T")


@dataclass(frozen=True)
class InttegroResponse(Generic[T]):
    """Decoded SDK value plus response-only HTTP metadata."""

    data: T
    status: int
    headers: Mapping[str, str]
    meta: Mapping[str, Any] | None = None

    @property
    def request_id(self) -> str | None:
        return _header(self.headers, "x-request-id")

    @property
    def retry_after(self) -> str | None:
        return _header(self.headers, "retry-after")


def _header(headers: Mapping[str, str], name: str) -> str | None:
    value = next((value for key, value in headers.items() if key.lower() == name), None)
    return value if isinstance(value, str) and value else None
