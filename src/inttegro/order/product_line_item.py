"""ProductLineItem in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ProductLineItem(ApiModel):
    """Typed product line item data in the order resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``OrderProductLineItem``.
    """
    type: Literal['product'] = field(init=False)
    """Discriminator identifying the product line item type. Required. Python type: ``Literal['product']``; wire name: ``type``; JSON type: string. Constraints: allowed values ``product``"""
    product: OrderProductLineItemProduct = field(init=False)
    """The product associated with this product line item. Required. Python type: ``OrderProductLineItemProduct``; wire name: ``product``; JSON type: object"""

from inttegro.order.product_line_item_product import ProductLineItemProduct as OrderProductLineItemProduct
