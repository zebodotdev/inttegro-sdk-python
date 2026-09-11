"""CreateRequestQuantity in the ``inttegro.purchase_intent`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class CreateRequestQuantity(ApiRequest):
    """Quantity bounds the Buy link should enforce. Omit max when the Buy link has no upper quantity bound. When present, max must be greater than or equal to min.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``CreatePurchaseIntentRequestQuantity``.
    """
    max: int | UnsetType = field(default=UNSET)
    """Optional maximum quantity the customer can buy. It must be greater than or equal to min. Optional. Python type: ``int``; wire name: ``max``; JSON type: integer. Constraints: minimum 1"""
    min: int
    """Minimum quantity the customer can buy. Required. Python type: ``int``; wire name: ``min``; JSON type: integer. Constraints: minimum 1"""
