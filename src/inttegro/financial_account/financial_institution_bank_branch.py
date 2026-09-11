"""FinancialInstitutionBankBranch in the ``inttegro.financial_account`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FinancialInstitutionBankBranch(ApiModel):
    """Typed financial institution bank branch data in the financial account resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.
    """
    id: str = field(init=False)
    """Unique identifier for this financial institution bank branch. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    name: str = field(init=False)
    """Human-readable name of the financial institution bank branch. Required. Python type: ``str``; wire name: ``name``; JSON type: string"""
    sort_code: str = field(init=False)
    """The sort code associated with this financial institution bank branch. Required. Python type: ``str``; wire name: ``sort_code``; JSON type: string"""
