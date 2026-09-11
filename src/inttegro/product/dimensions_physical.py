"""DimensionsPhysical in the ``inttegro.product`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class DimensionsPhysical(ApiModel):
    """Typed dimensions physical data in the product resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``ProductDimensionsPhysical``.
    """
    weight_unit: str | None = field(init=False)
    """The weight unit associated with this dimensions physical. Optional; nullable. Python type: ``str | None``; wire name: ``weight_unit``; JSON type: string"""
    weight: float | None = field(init=False)
    """The weight associated with this dimensions physical. Optional; nullable. Python type: ``float | None``; wire name: ``weight``; JSON type: number. Constraints: minimum 0"""
    size: float | None = field(init=False)
    """Legacy alias for weight in requests. Optional; nullable. Python type: ``float | None``; wire name: ``size``; JSON type: number. Constraints: minimum 0"""
    volume_unit: str | None = field(init=False)
    """The volume unit associated with this dimensions physical. Optional; nullable. Python type: ``str | None``; wire name: ``volume_unit``; JSON type: string"""
    volume: float | None = field(init=False)
    """The volume associated with this dimensions physical. Optional; nullable. Python type: ``float | None``; wire name: ``volume``; JSON type: number. Constraints: minimum 0"""
    length: float | None = field(init=False)
    """The length associated with this dimensions physical. Optional; nullable. Python type: ``float | None``; wire name: ``length``; JSON type: number. Constraints: minimum 0"""
    height: float | None = field(init=False)
    """The height associated with this dimensions physical. Optional; nullable. Python type: ``float | None``; wire name: ``height``; JSON type: number. Constraints: minimum 0"""
    width: float | None = field(init=False)
    """The width associated with this dimensions physical. Optional; nullable. Python type: ``float | None``; wire name: ``width``; JSON type: number. Constraints: minimum 0"""
