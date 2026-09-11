"""AddPriceResponse in the ``inttegro.product`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class AddPriceResponse(ApiModel):
    """Typed response returned by the add price operation.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``AddProductPriceResponse``.
    """
    price: CatalogPrice | None = field(init=False)
    """The price associated with this add price response. Optional; nullable. Python type: ``CatalogPrice | None``; wire name: ``price``; JSON type: object (CatalogPrice)"""
    error: Error | None = field(init=False)
    """Standard error response structure returned by all API endpoints. Provides machine-readable codes, human-readable messages, and actionable guidance for resolution. Optional; nullable. Python type: ``Error | None``; wire name: ``error``; JSON type: object (Error)"""

from inttegro.price.price import Price as CatalogPrice
from inttegro.shared.error import Error
