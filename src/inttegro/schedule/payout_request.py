"""PayoutRequest in the ``inttegro.schedule`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class PayoutRequest(ApiRequest):
    """A payout scheduled from your Inttegro balance to a destination financial account.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``SchedulePayoutRequest``.
    """
    execute_after: datetime | UnsetType = field(default=UNSET)
    """Earliest moment payout execution may begin. Optional. Python type: ``datetime``; wire name: ``execute_after``; JSON type: string (date-time)"""
    max_amount: int | UnsetType = field(default=UNSET)
    """Monetary max amount, represented by a currency and an integer minor-unit value. Optional. Python type: ``int``; wire name: ``max_amount``; JSON type: object (Amount)"""
    destination_id: str
    """Financial account receiving the funds. Required. Python type: ``str``; wire name: ``destination_id``; JSON type: string"""
    reference: str
    """Merchant reference carried on the payout. Required. Python type: ``str``; wire name: ``reference``; JSON type: string"""
