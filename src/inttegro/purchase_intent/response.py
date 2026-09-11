"""Response in the ``inttegro.purchase_intent`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Response(ApiModel):
    """Typed response returned by the response operation.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PurchaseIntentResponse``.
    """
    purchase_intent: PurchaseIntent = field(init=False)
    """The purchase intent associated with this response. Required. Python type: ``PurchaseIntent``; wire name: ``purchase_intent``; JSON type: object (PurchaseIntent)"""

from inttegro.purchase_intent.purchase_intent import PurchaseIntent
