"""GhanaBankAccountParams in the ``inttegro.bank_account`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class GhanaBankAccountParams(ApiRequest):
    """Parameters accepted by the ghana bank account params operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``FinancialAccountBankRequestBankAccountGhanaBankAccount``.
    """
    bank_name: str | UnsetType = field(default=UNSET)
    """The bank name associated with this ghana bank account param. Optional. Python type: ``str``; wire name: ``bank_name``; JSON type: string"""
    branch: str | UnsetType = field(default=UNSET)
    """The branch associated with this ghana bank account param. Optional. Python type: ``str``; wire name: ``branch``; JSON type: string"""
    sort_code: str | UnsetType = field(default=UNSET)
    """The sort code associated with this ghana bank account param. Optional. Python type: ``str``; wire name: ``sort_code``; JSON type: string. Constraints: minimum length 1"""
    swift_code: str | UnsetType = field(default=UNSET)
    """The swift code associated with this ghana bank account param. Optional. Python type: ``str``; wire name: ``swift_code``; JSON type: string. Constraints: minimum length 1"""
    holder: FinancialAccountOwnerInput | UnsetType = field(default=UNSET)
    """The holder associated with this ghana bank account param. Optional. Python type: ``FinancialAccountOwnerInput``; wire name: ``holder``; JSON type: object (FinancialAccountOwnerInput)"""
    number: str
    """Human-readable number assigned to the ghana bank account param. Required. Python type: ``str``; wire name: ``number``; JSON type: string. Constraints: minimum length 1"""

from inttegro.bank_account.owner_params import OwnerParams as FinancialAccountOwnerInput
