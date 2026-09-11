"""UpdateResponse in the ``inttegro.product`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UpdateResponse(ApiModel):
    """Typed response returned by the update operation.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``UpdateProductResponse``.
    """
    product: UpdatedProduct | None = field(init=False)
    """The product associated with this update response. Optional; nullable. Python type: ``UpdatedProduct | None``; wire name: ``product``; JSON type: object (UpdatedProduct)"""

from inttegro.product.updated import Updated as UpdatedProduct
