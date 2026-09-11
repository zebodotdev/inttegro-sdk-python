"""DimensionsInputDigital in the ``inttegro.product`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class DimensionsInputDigital(ApiRequest):
    """Parameters accepted by the dimensions input digital operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``ProductDimensionsInputDigital``.
    """
    bytes: float | UnsetType = field(default=UNSET)
    """The bytes associated with this dimensions input digital. Optional. Python type: ``float``; wire name: ``bytes``; JSON type: number. Constraints: minimum 0"""
    size_unit: str | UnsetType = field(default=UNSET)
    """The size unit associated with this dimensions input digital. Optional. Python type: ``str``; wire name: ``size_unit``; JSON type: string"""
    size: float | UnsetType = field(default=UNSET)
    """Numeric size used by this operation. Optional. Python type: ``float``; wire name: ``size``; JSON type: number. Constraints: minimum 0"""
