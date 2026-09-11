"""BankAccount in the ``inttegro.bank_account`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class BankAccount(ApiModel):
    """Typed bank account data in the bank account resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``FinancialAccountBank``.
    """
    type: Literal['ghana_bank_account'] = field(init=False)
    """Discriminator identifying the bank account type. Required. Python type: ``Literal['ghana_bank_account']``; wire name: ``type``; JSON type: string. Constraints: allowed values ``ghana_bank_account``"""
    ghana_bank_account: GhanaBankAccount | None = field(init=False)
    """The ghana bank account associated with this bank account. Required; nullable. Python type: ``GhanaBankAccount | None``; wire name: ``ghana_bank_account``; JSON type: one of the documented JSON shapes"""

from inttegro.bank_account.ghana_bank_account import GhanaBankAccount
