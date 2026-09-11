"""DimensionsInput in the ``inttegro.product`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class DimensionsInput(ApiRequest):
    """At most one of `physical`, `digital`, or `custom`.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``ProductDimensionsInput``.
    """
    physical: ProductDimensionsInputPhysical | UnsetType = field(default=UNSET)
    """The physical associated with this dimensions input. Optional. Python type: ``ProductDimensionsInputPhysical``; wire name: ``physical``; JSON type: object"""
    digital: ProductDimensionsInputDigital | UnsetType = field(default=UNSET)
    """The digital associated with this dimensions input. Optional. Python type: ``ProductDimensionsInputDigital``; wire name: ``digital``; JSON type: object"""
    custom: ProductDimensionsInputCustom | UnsetType = field(default=UNSET)
    """The custom associated with this dimensions input. Optional. Python type: ``ProductDimensionsInputCustom``; wire name: ``custom``; JSON type: object"""

from inttegro.product.dimensions_input_custom import DimensionsInputCustom as ProductDimensionsInputCustom
from inttegro.product.dimensions_input_digital import DimensionsInputDigital as ProductDimensionsInputDigital
from inttegro.product.dimensions_input_physical import DimensionsInputPhysical as ProductDimensionsInputPhysical
