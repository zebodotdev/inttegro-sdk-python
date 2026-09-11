"""EnablePullRequest in the ``inttegro.financial_account`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class EnablePullRequest(ApiRequest):
    """Parameters accepted by the enable pull request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``FinancialAccountEnablePullRequest``.
    """
    ip_address: str | UnsetType = field(default=UNSET)
    """Client IP captured for the mandate. This is not inferred from the request. Optional. Python type: ``str``; wire name: ``ip_address``; JSON type: string"""
    user_agent: str | UnsetType = field(default=UNSET)
    """Client user agent captured for the mandate. This is not inferred from the request. Optional. Python type: ``str``; wire name: ``user_agent``; JSON type: string"""
    account_id: str
    """Identifier of the related account. Required. Python type: ``str``; wire name: ``account_id``; JSON type: string"""
