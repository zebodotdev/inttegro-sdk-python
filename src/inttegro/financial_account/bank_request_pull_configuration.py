"""BankRequestPullConfiguration in the ``inttegro.financial_account`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class BankRequestPullConfiguration(ApiRequest):
    """Parameters accepted by the bank request pull configuration operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``FinancialAccountBankRequestPullConfiguration``.
    """
    enabled: bool | UnsetType = field(default=UNSET)
    """Whether enabled. Optional. Python type: ``bool``; wire name: ``enabled``; JSON type: boolean"""
