"""Price in the ``inttegro.purchase_intent`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel
from inttegro.money import Amount


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Price(ApiModel):
    """Typed price data in the purchase intent resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PurchaseIntentPrice``.
    """
    active: bool = field(init=False)
    """Whether the resolved price can be used. Required. Python type: ``bool``; wire name: ``active``; JSON type: boolean"""
    id: str | None = field(init=False)
    """Catalog price ID when the offer price is not inline. Optional; nullable. Python type: ``str | None``; wire name: ``id``; JSON type: string"""
    label: str | None = field(init=False)
    """Catalog price label when available. Optional; nullable. Python type: ``str | None``; wire name: ``label``; JSON type: string"""
    nominal: Amount = field(init=False)
    """Monetary nominal, represented by a currency and an integer minor-unit value. Required. Python type: ``Amount``; wire name: ``nominal``; JSON type: object (Amount)"""
    original: PurchaseIntentOriginalPrice | None = field(init=False)
    """The original associated with this price. Optional; nullable. Python type: ``PurchaseIntentOriginalPrice | None``; wire name: ``original``; JSON type: object (PurchaseIntentOriginalPrice)"""

from inttegro.purchase_intent.original_price import OriginalPrice as PurchaseIntentOriginalPrice
