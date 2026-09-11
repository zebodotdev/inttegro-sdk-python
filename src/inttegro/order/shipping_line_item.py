"""ShippingLineItem in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ShippingLineItem(ApiModel):
    """Typed shipping line item data in the order resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``OrderShippingLineItem``.
    """
    type: Literal['shipping'] = field(init=False)
    """Discriminator identifying the shipping line item type. Required. Python type: ``Literal['shipping']``; wire name: ``type``; JSON type: string. Constraints: allowed values ``shipping``"""
    shipping: OrderShippingLineItemShipping = field(init=False)
    """The shipping associated with this shipping line item. Required. Python type: ``OrderShippingLineItemShipping``; wire name: ``shipping``; JSON type: object"""

from inttegro.order.shipping_line_item_shipping import ShippingLineItemShipping as OrderShippingLineItemShipping
