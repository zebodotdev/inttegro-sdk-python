"""DiscountLineItem in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class DiscountLineItem(ApiModel):
    """Typed discount line item data in the order resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``OrderDiscountLineItem``.
    """
    type: Literal['discount'] = field(init=False)
    """Discriminator identifying the discount line item type. Required. Python type: ``Literal['discount']``; wire name: ``type``; JSON type: string. Constraints: allowed values ``discount``"""
    discount: OrderDiscountLineItemDiscount = field(init=False)
    """The discount associated with this discount line item. Required. Python type: ``OrderDiscountLineItemDiscount``; wire name: ``discount``; JSON type: object (OrderDiscount)"""

from inttegro.order.discount_line_item_discount import DiscountLineItemDiscount as OrderDiscountLineItemDiscount
