"""CreateRequestProduct in the ``inttegro.purchase_intent`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class CreateRequestProduct(ApiRequest):
    """Product selection with optional variant-set configuration. Use this instead of product_id.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``CreatePurchaseIntentRequestProduct``.
    """
    variant_set_id: str | UnsetType = field(default=UNSET)
    """Optional variant set ID the hosted checkout may use for sibling product selection. Optional. Python type: ``str``; wire name: ``variant_set_id``; JSON type: string"""
    id: str
    """Product ID to sell through the Buy link. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
