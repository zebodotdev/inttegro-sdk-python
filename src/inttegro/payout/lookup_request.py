"""LookupRequest in the ``inttegro.payout`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass
from inttegro._request_base import ApiRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class LookupRequest(ApiRequest):
    """Merchant balance entry caused by a payment or refund. `type` describes the semantic source, not direction. A payment transaction contains `payment_id`; a refund transaction contains `refund_id`. Exactly one matching reference is present.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``LookupPayoutRequest``.
    """
    payout_id: str
    """Identifier of the related payout. Required. Python type: ``str``; wire name: ``payout_id``; JSON type: string"""
