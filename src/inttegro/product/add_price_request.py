"""AddPriceRequest in the ``inttegro.product`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType
from inttegro.money import AmountParams


@dataclass(frozen=True, slots=True, kw_only=True)
class AddPriceRequest(ApiRequest):
    """Parameters accepted by the add price request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``AddProductPriceRequest``.
    """
    label: str | UnsetType = field(default=UNSET)
    """Optional short label for the new price. Optional. Python type: ``str``; wire name: ``label``; JSON type: string. Constraints: maximum length 100"""
    about: str | UnsetType = field(default=UNSET)
    """Optional internal description for the new price. Optional. Python type: ``str``; wire name: ``about``; JSON type: string. Constraints: maximum length 500"""
    product_id: str
    """Product ID to attach the new price to. Required. Python type: ``str``; wire name: ``product_id``; JSON type: string"""
    amount: AmountParams
    """Monetary amount, represented by a currency and an integer minor-unit value. Required. Python type: ``AmountParams``; wire name: ``amount``; JSON type: object (AmountParams)"""
