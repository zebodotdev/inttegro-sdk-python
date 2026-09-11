"""GhanaBankAccount in the ``inttegro.bank_account`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class GhanaBankAccount(ApiModel):
    """Typed ghana bank account data in the bank account resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.
    """
    branch: str | None = field(init=False)
    """The branch associated with this ghana bank account. Optional; nullable. Python type: ``str | None``; wire name: ``branch``; JSON type: string"""
    holder: FinancialAccountOwner = field(init=False)
    """The holder associated with this ghana bank account. Required. Python type: ``FinancialAccountOwner``; wire name: ``holder``; JSON type: object (FinancialAccountOwnerResponse)"""
    name: str | None = field(init=False)
    """Human-readable name of the ghana bank account. Optional; nullable. Python type: ``str | None``; wire name: ``name``; JSON type: string"""
    number: str = field(init=False)
    """Human-readable number assigned to the ghana bank account. Required. Python type: ``str``; wire name: ``number``; JSON type: string"""
    sort_code: str | None = field(init=False)
    """The sort code associated with this ghana bank account. Optional; nullable. Python type: ``str | None``; wire name: ``sort_code``; JSON type: string"""
    swift_code: str | None = field(init=False)
    """The swift code associated with this ghana bank account. Optional; nullable. Python type: ``str | None``; wire name: ``swift_code``; JSON type: string"""

from inttegro.bank_account.owner import Owner as FinancialAccountOwner
