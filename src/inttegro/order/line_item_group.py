"""LineItemGroup in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel
from inttegro.money import Amount


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class LineItemGroup(ApiModel):
    """Cart contents and totals.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``OrderLineItemGroup``.
    """
    line_items: list[OrderLineItem] = field(init=False)
    """Array of products, fees, and shipping charges. Required. Python type: ``list[OrderLineItem]``; wire name: ``line_items``; JSON type: array of object (OrderLineItem) values"""
    total: Amount = field(init=False)
    """Monetary total, represented by a currency and an integer minor-unit value. Required. Python type: ``Amount``; wire name: ``total``; JSON type: object (Amount)"""

from inttegro.order.line_item import LineItem as OrderLineItem
