"""DimensionsDigital in the ``inttegro.product`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class DimensionsDigital(ApiModel):
    """Typed dimensions digital data in the product resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``ProductDimensionsDigital``.
    """
    bytes: float | None = field(init=False)
    """The bytes associated with this dimensions digital. Optional; nullable. Python type: ``float | None``; wire name: ``bytes``; JSON type: number. Constraints: minimum 0"""
    size_unit: str | None = field(init=False)
    """The size unit associated with this dimensions digital. Optional; nullable. Python type: ``str | None``; wire name: ``size_unit``; JSON type: string"""
    size: float | None = field(init=False)
    """Numeric size used by this operation. Optional; nullable. Python type: ``float | None``; wire name: ``size``; JSON type: number. Constraints: minimum 0"""
