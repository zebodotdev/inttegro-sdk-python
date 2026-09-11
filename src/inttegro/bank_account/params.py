"""Params in the ``inttegro.bank_account`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Literal
from inttegro._request_base import ApiRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class Params(ApiRequest):
    """Parameters accepted by the params operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``FinancialAccountBankRequestBankAccount``.
    """
    type: Literal['ghana_bank_account', BankAccountType.GHANA_BANK_ACCOUNT]
    """Discriminator identifying the param type. Required. Python type: ``Literal['ghana_bank_account', BankAccountType.GHANA_BANK_ACCOUNT]``; wire name: ``type``; JSON type: string. Constraints: allowed values ``ghana_bank_account``"""
    ghana_bank_account: FinancialAccountBankRequestBankAccountGhanaBankAccount
    """The ghana bank account associated with this param. Required. Python type: ``FinancialAccountBankRequestBankAccountGhanaBankAccount``; wire name: ``ghana_bank_account``; JSON type: one of the documented JSON shapes"""

from inttegro.bank_account.type import Type as BankAccountType
from inttegro.bank_account.ghana_bank_account_params import GhanaBankAccountParams as FinancialAccountBankRequestBankAccountGhanaBankAccount
