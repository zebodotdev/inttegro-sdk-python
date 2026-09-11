"""CancelRequest in the ``inttegro.purchase_intent`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class CancelRequest(ApiRequest):
    """Parameters accepted by the cancel request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``CancelPurchaseIntentRequest``.
    """
    id: str | UnsetType = field(default=UNSET)
    """Purchase intent ID to cancel. Send this or purchase_intent_id. Optional. Python type: ``str``; wire name: ``id``; JSON type: string. Constraints: minimum length 1"""
    purchase_intent_id: str | UnsetType = field(default=UNSET)
    """Alias for id. If both are present, this value takes precedence. Optional. Python type: ``str``; wire name: ``purchase_intent_id``; JSON type: string. Constraints: minimum length 1"""
