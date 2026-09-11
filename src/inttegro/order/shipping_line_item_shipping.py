"""ShippingLineItemShipping in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel
from inttegro.money import Amount


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ShippingLineItemShipping(ApiModel):
    """Typed shipping line item shipping data in the order resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``OrderShippingLineItemShipping``.
    """
    id: str = field(init=False)
    """Immutable order-line identifier with the `oli_` prefix. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    tax_code: str | None = field(init=False)
    """The tax code associated with this shipping line item shipping. Optional; nullable. Python type: ``str | None``; wire name: ``tax_code``; JSON type: string"""
    label: str | None = field(init=False)
    """The label associated with this shipping line item shipping. Optional; nullable. Python type: ``str | None``; wire name: ``label``; JSON type: string"""
    fee: Amount = field(init=False)
    """Monetary fee, represented by a currency and an integer minor-unit value. Required. Python type: ``Amount``; wire name: ``fee``; JSON type: object (Amount)"""
