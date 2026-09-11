"""CountryBankDirectory in the ``inttegro.shared`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class CountryBankDirectory(ApiModel):
    """Bank reference data available for country-specific bank accounts.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.
    """
    bank_account_type: str = field(init=False)
    """Country-specific bank account subtype used by financial account APIs. Required. Python type: ``str``; wire name: ``bank_account_type``; JSON type: string"""
    code_scheme: str = field(init=False)
    """Identifier scheme used for bank branch codes. Required. Python type: ``str``; wire name: ``code_scheme``; JSON type: string"""
    items: list[CountryBank] = field(init=False)
    """Banking institutions available in this country. Required. Python type: ``list[CountryBank]``; wire name: ``items``; JSON type: array of object (CountryBank) values"""

from inttegro.shared.country_bank import CountryBank
