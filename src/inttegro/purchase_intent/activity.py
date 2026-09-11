"""Activity in the ``inttegro.purchase_intent`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal
from inttegro._model_base import ApiModel
from inttegro.money import Amount


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Activity(ApiModel):
    """Typed activity data in the purchase intent resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PurchaseIntentActivity``.
    """
    amount: Amount | None = field(init=False)
    """Monetary amount, represented by a currency and an integer minor-unit value. Optional; nullable. Python type: ``Amount | None``; wire name: ``amount``; JSON type: object (Amount)"""
    attribution: PurchaseIntentActivityAttribution | None = field(init=False)
    """The attribution associated with this activity. Optional; nullable. Python type: ``PurchaseIntentActivityAttribution | None``; wire name: ``attribution``; JSON type: object (PurchaseIntentActivityAttribution)"""
    created_at: datetime = field(init=False)
    """When the activity was created. Required. Python type: ``datetime``; wire name: ``created_at``; JSON type: string (date-time)"""
    error_code: str | None = field(init=False)
    """The error code associated with this activity. Optional; nullable. Python type: ``str | None``; wire name: ``error_code``; JSON type: string"""
    id: str = field(init=False)
    """Activity event ID with saleevt_ prefix. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    order_id: str | None = field(init=False)
    """Identifier of the related order. Optional; nullable. Python type: ``str | None``; wire name: ``order_id``; JSON type: string"""
    payment_id: str | None = field(init=False)
    """Identifier of the related payment. Optional; nullable. Python type: ``str | None``; wire name: ``payment_id``; JSON type: string"""
    product_id: str | None = field(init=False)
    """Identifier of the related product. Optional; nullable. Python type: ``str | None``; wire name: ``product_id``; JSON type: string"""
    purchase_intent_id: str = field(init=False)
    """Purchase intent ID with sale_ prefix. Required. Python type: ``str``; wire name: ``purchase_intent_id``; JSON type: string"""
    quantity: int | None = field(init=False)
    """Numeric quantity used by this operation. Optional; nullable. Python type: ``int | None``; wire name: ``quantity``; JSON type: integer. Constraints: minimum 0"""
    source: str | None = field(init=False)
    """The source associated with this activity. Optional; nullable. Python type: ``str | None``; wire name: ``source``; JSON type: string"""
    type: Literal['expired_viewed', 'order_created', 'payment_failed', 'payment_started', 'viewed'] = field(init=False)
    """Discriminator identifying the activity type. Required. Python type: ``Literal['expired_viewed', 'order_created', 'payment_failed', 'payment_started', 'viewed']``; wire name: ``type``; JSON type: string. Constraints: allowed values ``expired_viewed``, ``order_created``, ``payment_failed``, ``payment_started``, ``viewed``"""
    variant_product_id: str | None = field(init=False)
    """Identifier of the related variant product. Optional; nullable. Python type: ``str | None``; wire name: ``variant_product_id``; JSON type: string"""
    visitor: PurchaseIntentActivityVisitor | None = field(init=False)
    """The visitor associated with this activity. Optional; nullable. Python type: ``PurchaseIntentActivityVisitor | None``; wire name: ``visitor``; JSON type: object (PurchaseIntentActivityVisitor)"""

from inttegro.purchase_intent.activity_attribution import ActivityAttribution as PurchaseIntentActivityAttribution
from inttegro.purchase_intent.activity_visitor import ActivityVisitor as PurchaseIntentActivityVisitor
