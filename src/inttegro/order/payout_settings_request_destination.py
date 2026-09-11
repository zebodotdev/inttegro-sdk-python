"""PayoutSettingsRequestDestination in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass
from inttegro._request_base import ApiRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class PayoutSettingsRequestDestination(ApiRequest):
    """Parameters accepted by the payout settings request destination operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``OrderPayoutSettingsRequestDestination``.
    """
    financial_account_id: str
    """Same-currency financial account with push capability enabled. Required. Python type: ``str``; wire name: ``financial_account_id``; JSON type: string"""
