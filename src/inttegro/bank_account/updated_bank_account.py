"""UpdatedBankAccount in the ``inttegro.bank_account`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UpdatedBankAccount(ApiModel):
    """Typed updated bank account data in the bank account resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``FinancialAccountBankUpdateResponse``.
    """
    id: str = field(init=False)
    """Unique identifier for this updated bank account. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    type: Literal['ghana_bank_account'] = field(init=False)
    """Discriminator identifying the updated bank account type. Required. Python type: ``Literal['ghana_bank_account']``; wire name: ``type``; JSON type: string. Constraints: allowed values ``ghana_bank_account``"""
    ghana_bank_account: GhanaBankAccountUpdateResponse | None = field(init=False)
    """The ghana bank account associated with this updated bank account. Optional; nullable. Python type: ``GhanaBankAccountUpdateResponse | None``; wire name: ``ghana_bank_account``; JSON type: object (GhanaBankAccountUpdateResponse)"""

from inttegro.bank_account.updated_ghana_bank_account import UpdatedGhanaBankAccount as GhanaBankAccountUpdateResponse
