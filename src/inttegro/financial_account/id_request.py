"""IDRequest in the ``inttegro.financial_account`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass
from inttegro._request_base import ApiRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class IDRequest(ApiRequest):
    """Parameters accepted by the idrequest operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``FinancialAccountIDRequest``.
    """
    account_id: str
    """Identifier of the related account. Required. Python type: ``str``; wire name: ``account_id``; JSON type: string"""
