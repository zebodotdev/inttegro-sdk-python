"""BankAccount in the ``inttegro.payment_method`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class BankAccount(ApiModel):
    """Bank account details (present when type is bank_account).

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PaymentMethodBankAccount``.
    """
    ghana_bank_account: PaymentMethodBankAccountGhanaBankAccount | None = field(init=False)
    """Ghana bank account details. Optional; nullable. Python type: ``PaymentMethodBankAccountGhanaBankAccount | None``; wire name: ``ghana_bank_account``; JSON type: object"""
    type: Literal['ghana_bank_account'] = field(init=False)
    """Bank account sub-type. Required. Python type: ``Literal['ghana_bank_account']``; wire name: ``type``; JSON type: string. Constraints: allowed values ``ghana_bank_account``"""

from inttegro.payment_method.bank_account_ghana_bank_account import BankAccountGhanaBankAccount as PaymentMethodBankAccountGhanaBankAccount
