"""UsageOrder in the ``inttegro.purchase_intent`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UsageOrder(ApiModel):
    """Typed usage order data in the purchase intent resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PurchaseIntentUsageOrder``.
    """
    created_at: datetime = field(init=False)
    """When order creation consumed the single-use Buy link. Required. Python type: ``datetime``; wire name: ``created_at``; JSON type: string (date-time)"""
    id: str = field(init=False)
    """Order that consumed the Buy link. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
