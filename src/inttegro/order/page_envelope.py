"""PageEnvelope in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PageEnvelope(ApiModel):
    """Typed page envelope data in the order resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PageOrdersEnvelope``.
    """
    page: OrderPage | None = field(init=False)
    """Numeric page used by this operation. Required; nullable. Python type: ``OrderPage | None``; wire name: ``page``; JSON type: object (MessageTemplatesPage)"""

from inttegro.order.page import Page as OrderPage
