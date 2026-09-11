"""DimensionsInputPhysical in the ``inttegro.product`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class DimensionsInputPhysical(ApiRequest):
    """Parameters accepted by the dimensions input physical operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``ProductDimensionsInputPhysical``.
    """
    weight_unit: str | UnsetType = field(default=UNSET)
    """The weight unit associated with this dimensions input physical. Optional. Python type: ``str``; wire name: ``weight_unit``; JSON type: string"""
    weight: float | UnsetType = field(default=UNSET)
    """The weight associated with this dimensions input physical. Optional. Python type: ``float``; wire name: ``weight``; JSON type: number. Constraints: minimum 0"""
    size: float | UnsetType = field(default=UNSET)
    """Legacy alias for weight in requests. Optional. Python type: ``float``; wire name: ``size``; JSON type: number. Constraints: minimum 0"""
    volume_unit: str | UnsetType = field(default=UNSET)
    """The volume unit associated with this dimensions input physical. Optional. Python type: ``str``; wire name: ``volume_unit``; JSON type: string"""
    volume: float | UnsetType = field(default=UNSET)
    """The volume associated with this dimensions input physical. Optional. Python type: ``float``; wire name: ``volume``; JSON type: number. Constraints: minimum 0"""
    length: float | UnsetType = field(default=UNSET)
    """The length associated with this dimensions input physical. Optional. Python type: ``float``; wire name: ``length``; JSON type: number. Constraints: minimum 0"""
    height: float | UnsetType = field(default=UNSET)
    """The height associated with this dimensions input physical. Optional. Python type: ``float``; wire name: ``height``; JSON type: number. Constraints: minimum 0"""
    width: float | UnsetType = field(default=UNSET)
    """The width associated with this dimensions input physical. Optional. Python type: ``float``; wire name: ``width``; JSON type: number. Constraints: minimum 0"""
