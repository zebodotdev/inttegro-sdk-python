"""CatalogWithPriceDataInput in the ``inttegro.product`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass
from inttegro._request_base import ApiRequest
from inttegro.price.inline_params import InlineParams as PriceParams


@dataclass(frozen=True, slots=True, kw_only=True)
class CatalogWithPriceDataInput(ApiRequest):
    """Parameters accepted by the catalog with price data input operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``CatalogProductWithPriceDataInput``.
    """
    price: PriceParams
    """An inline price supplied in a request. Required. Python type: ``PriceParams``; wire name: ``price``; JSON type: object (PriceParams)"""
    product_id: str
    """Existing catalog product ID to snapshot onto the order line item. Required. Python type: ``str``; wire name: ``product_id``; JSON type: string"""
    quantity: int
    """How many units of the catalog product the customer is purchasing. Required. Python type: ``int``; wire name: ``quantity``; JSON type: integer. Constraints: minimum 1"""
