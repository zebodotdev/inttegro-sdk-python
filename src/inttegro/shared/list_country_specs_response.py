"""ListCountrySpecsResponse in the ``inttegro.shared`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ListCountrySpecsResponse(ApiModel):
    """Typed response returned by the list country specs operation.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.
    """
    countries: dict[str, CountrySpecification] = field(init=False)
    """The countries associated with this list country specs response. Required. Python type: ``dict[str, CountrySpecification]``; wire name: ``countries``; JSON type: object"""

from inttegro.shared.country_specification import CountrySpecification
