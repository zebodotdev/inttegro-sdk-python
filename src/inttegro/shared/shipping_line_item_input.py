"""ShippingLineItemInput in the ``inttegro.shared`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Literal
from inttegro._request_base import ApiRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class ShippingLineItemInput(ApiRequest):
    """Parameters accepted by the shipping line item input operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.
    """
    type: Literal['shipping', LineItemType.SHIPPING]
    """Line item type discriminator. Required. Python type: ``Literal['shipping', LineItemType.SHIPPING]``; wire name: ``type``; JSON type: string. Constraints: allowed values ``shipping``"""
    shipping: ShippingDetailsInput
    """The shipping associated with this shipping line item input. Required. Python type: ``ShippingDetailsInput``; wire name: ``shipping``; JSON type: object (ShippingDetails)"""

from inttegro.order.line_item_type import LineItemType
from inttegro.shared.shipping_details_input import ShippingDetailsInput
