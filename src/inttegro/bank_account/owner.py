"""Owner in the ``inttegro.bank_account`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Owner(ApiModel):
    """Typed owner data in the bank account resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``FinancialAccountOwner``.
    """
    address: FinancialAccountAddress = field(init=False)
    """The address associated with this owner. Required. Python type: ``FinancialAccountAddress``; wire name: ``address``; JSON type: object"""
    name: str = field(init=False)
    """Human-readable name of the owner. Required. Python type: ``str``; wire name: ``name``; JSON type: string. Constraints: minimum length 1"""

from inttegro.bank_account.owner_address import OwnerAddress as FinancialAccountAddress
