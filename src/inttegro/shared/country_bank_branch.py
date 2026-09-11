"""CountryBankBranch in the ``inttegro.shared`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class CountryBankBranch(ApiModel):
    """A bank branch in a country bank directory.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.
    """
    id: str = field(init=False)
    """Stable branch identifier. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    name: str = field(init=False)
    """Branch display name. Required. Python type: ``str``; wire name: ``name``; JSON type: string"""
    sort_code: str = field(init=False)
    """Ghana bank branch sort code. Required. Python type: ``str``; wire name: ``sort_code``; JSON type: string"""
