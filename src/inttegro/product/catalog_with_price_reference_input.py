"""CatalogWithPriceReferenceInput in the ``inttegro.product`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass
from inttegro._request_base import ApiRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class CatalogWithPriceReferenceInput(ApiRequest):
    """Parameters accepted by the catalog with price reference input operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``CatalogProductWithPriceReferenceInput``.
    """
    price_id: str
    """Existing product price to snapshot onto the order line item. It must belong to the same application and product. Required. Python type: ``str``; wire name: ``price_id``; JSON type: string"""
    product_id: str
    """Existing catalog product ID to snapshot onto the order line item. Required. Python type: ``str``; wire name: ``product_id``; JSON type: string"""
    quantity: int
    """How many units of the catalog product the customer is purchasing. Required. Python type: ``int``; wire name: ``quantity``; JSON type: integer. Constraints: minimum 1"""
