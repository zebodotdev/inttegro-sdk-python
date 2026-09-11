"""Usage in the ``inttegro.purchase_intent`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Usage(ApiModel):
    """Exactly one of multi_use or single_use is returned as true. Order is present after a single-use intent is consumed.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PurchaseIntentUsage``.
    """
    multi_use: bool | None = field(init=False)
    """Whether multi use. Optional; nullable. Python type: ``bool | None``; wire name: ``multi_use``; JSON type: boolean"""
    order: PurchaseIntentUsageOrder | None = field(init=False)
    """The order associated with this usage. Optional; nullable. Python type: ``PurchaseIntentUsageOrder | None``; wire name: ``order``; JSON type: object (PurchaseIntentUsageOrder)"""
    single_use: bool | None = field(init=False)
    """Whether single use. Optional; nullable. Python type: ``bool | None``; wire name: ``single_use``; JSON type: boolean"""

from inttegro.purchase_intent.usage_order import UsageOrder as PurchaseIntentUsageOrder
