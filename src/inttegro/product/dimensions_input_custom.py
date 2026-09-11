"""DimensionsInputCustom in the ``inttegro.product`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class DimensionsInputCustom(ApiRequest):
    """Parameters accepted by the dimensions input custom operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``ProductDimensionsInputCustom``.
    """
    size_unit: str | UnsetType = field(default=UNSET)
    """The size unit associated with this dimensions input custom. Optional. Python type: ``str``; wire name: ``size_unit``; JSON type: string"""
    size: float | UnsetType = field(default=UNSET)
    """Numeric size used by this operation. Optional. Python type: ``float``; wire name: ``size``; JSON type: number. Constraints: minimum 0"""
    details: dict[str, str] | UnsetType = field(default=UNSET)
    """Named string measurements or descriptors for a product dimension. Optional. Python type: ``dict[str, str]``; wire name: ``details``; JSON type: object (ProductDimensionDetails)"""
