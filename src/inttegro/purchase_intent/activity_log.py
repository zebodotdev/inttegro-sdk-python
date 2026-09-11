"""ActivityLog in the ``inttegro.purchase_intent`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ActivityLog(ApiModel):
    """Recent authenticated-owner activity for the purchase intent.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PurchaseIntentActivityLog``.
    """
    recent: list[PurchaseIntentActivity] | None = field(init=False)
    """The recent associated with this activity log. Optional; nullable. Python type: ``list[PurchaseIntentActivity] | None``; wire name: ``recent``; JSON type: array of object (PurchaseIntentActivity) values"""

from inttegro.purchase_intent.activity import Activity as PurchaseIntentActivity
