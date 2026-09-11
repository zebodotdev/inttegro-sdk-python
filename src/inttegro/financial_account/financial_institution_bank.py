"""FinancialInstitutionBank in the ``inttegro.financial_account`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FinancialInstitutionBank(ApiModel):
    """Typed financial institution bank data in the financial account resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.
    """
    bank_account_type: str = field(init=False)
    """The bank account type associated with this financial institution bank. Required. Python type: ``str``; wire name: ``bank_account_type``; JSON type: string"""
    branch: FinancialInstitutionBankBranch | None = field(init=False)
    """The branch associated with this financial institution bank. Optional; nullable. Python type: ``FinancialInstitutionBankBranch | None``; wire name: ``branch``; JSON type: object"""
    code_scheme: str = field(init=False)
    """The code scheme associated with this financial institution bank. Required. Python type: ``str``; wire name: ``code_scheme``; JSON type: string"""
    sort_code_prefix: str | None = field(init=False)
    """The sort code prefix associated with this financial institution bank. Optional; nullable. Python type: ``str | None``; wire name: ``sort_code_prefix``; JSON type: string"""
    swift_code: str | None = field(init=False)
    """The swift code associated with this financial institution bank. Optional; nullable. Python type: ``str | None``; wire name: ``swift_code``; JSON type: string"""

from inttegro.financial_account.financial_institution_bank_branch import FinancialInstitutionBankBranch
