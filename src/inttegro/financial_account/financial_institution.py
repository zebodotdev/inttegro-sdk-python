"""FinancialInstitution in the ``inttegro.financial_account`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FinancialInstitution(ApiModel):
    """Typed financial institution data in the financial account resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.
    """
    bank: FinancialInstitutionBank | None = field(init=False)
    """The bank associated with this financial institution. Optional; nullable. Python type: ``FinancialInstitutionBank | None``; wire name: ``bank``; JSON type: object"""
    country: str = field(init=False)
    """The country associated with this financial institution. Required. Python type: ``str``; wire name: ``country``; JSON type: string"""
    id: str = field(init=False)
    """Unique identifier for this financial institution. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    mobile_money_provider: FinancialInstitutionMobileMoneyProvider | None = field(init=False)
    """The mobile money provider associated with this financial institution. Optional; nullable. Python type: ``FinancialInstitutionMobileMoneyProvider | None``; wire name: ``mobile_money_provider``; JSON type: object"""
    name: str = field(init=False)
    """Human-readable name of the financial institution. Required. Python type: ``str``; wire name: ``name``; JSON type: string"""
    type: str = field(init=False)
    """Discriminator identifying the financial institution type. Required. Python type: ``str``; wire name: ``type``; JSON type: string"""

from inttegro.financial_account.financial_institution_bank import FinancialInstitutionBank
from inttegro.financial_account.financial_institution_mobile_money_provider import FinancialInstitutionMobileMoneyProvider
