"""Params in the ``inttegro.price`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType
from inttegro.money import AmountParams


@dataclass(frozen=True, slots=True, kw_only=True)
class Params(ApiRequest):
    """Parameters accepted by the params operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``CatalogPriceParams``.
    """
    product_id: str | UnsetType = field(default=UNSET)
    """Optional product ID to associate this price with. Once set, cannot be changed. Optional. Python type: ``str``; wire name: ``product_id``; JSON type: string"""
    label: str | UnsetType = field(default=UNSET)
    """Short label for this price (max 100 characters). Optional. Python type: ``str``; wire name: ``label``; JSON type: string"""
    about: str | UnsetType = field(default=UNSET)
    """Longer description of this price (max 500 characters). Optional. Python type: ``str``; wire name: ``about``; JSON type: string"""
    amount: AmountParams
    """Monetary amount, represented by a currency and an integer minor-unit value. Required. Python type: ``AmountParams``; wire name: ``amount``; JSON type: object (AmountParams)"""
