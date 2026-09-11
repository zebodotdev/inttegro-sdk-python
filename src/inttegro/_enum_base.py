"""Base class for string-backed Inttegro API enums."""

from enum import Enum


class WireEnum(str, Enum):
    """A JSON-compatible string enum used on the Inttegro API wire."""

    def __str__(self) -> str:
        return str(self.value)
