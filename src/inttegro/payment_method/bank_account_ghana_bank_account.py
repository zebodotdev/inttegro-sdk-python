"""BankAccountGhanaBankAccount in the ``inttegro.payment_method`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class BankAccountGhanaBankAccount(ApiModel):
    """Ghana bank account details.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PaymentMethodBankAccountGhanaBankAccount``.
    """
    branch: str | None = field(init=False)
    """Branch name. Optional; nullable. Python type: ``str | None``; wire name: ``branch``; JSON type: string"""
    name: str | None = field(init=False)
    """Account holder name. Optional; nullable. Python type: ``str | None``; wire name: ``name``; JSON type: string"""
    account_number: str = field(init=False)
    """Account number. Required. Python type: ``str``; wire name: ``account_number``; JSON type: string"""
    sort_code: str | None = field(init=False)
    """Bank sort code. Optional; nullable. Python type: ``str | None``; wire name: ``sort_code``; JSON type: string"""
    swift_code: str | None = field(init=False)
    """SWIFT/BIC code. Optional; nullable. Python type: ``str | None``; wire name: ``swift_code``; JSON type: string"""
