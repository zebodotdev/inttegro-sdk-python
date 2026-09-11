"""LineItemInput in the ``inttegro.product`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Literal
from inttegro._request_base import ApiRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class LineItemInput(ApiRequest):
    """Parameters accepted by the line item input operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``ProductLineItemInput``.
    """
    type: Literal['product', LineItemType.PRODUCT]
    """Line item type discriminator. Required. Python type: ``Literal['product', LineItemType.PRODUCT]``; wire name: ``type``; JSON type: string. Constraints: allowed values ``product``"""
    product: ProductDetailsInput
    """Provide either inline product data or a `product_id` reference to an existing catalog product. Catalog-backed product line items can use an explicit `price` or an existing `price_id`. Inttegro never falls back to a product's default unit price during order creation. Required. Python type: ``ProductDetailsInput``; wire name: ``product``; JSON type: object (ProductDetails)"""

from inttegro.order.line_item_type import LineItemType
from inttegro.product.details_input import DetailsInput as ProductDetailsInput
