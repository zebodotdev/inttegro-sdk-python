"""DisableRequest in the ``inttegro.financial_account`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class DisableRequest(ApiRequest):
    """Parameters accepted by the disable request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``FinancialAccountDisableRequest``.
    """
    unset_as_payout_destination: bool | UnsetType = field(default=UNSET)
    """Remove this account from payout destinations before the state change. If false, a mapped account is rejected. Optional. Python type: ``bool``; wire name: ``unset_as_payout_destination``; JSON type: boolean"""
    account_id: str
    """Identifier of the related account. Required. Python type: ``str``; wire name: ``account_id``; JSON type: string"""
