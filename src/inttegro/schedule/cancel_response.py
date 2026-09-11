"""CancelResponse in the ``inttegro.schedule`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class CancelResponse(ApiModel):
    """Typed response returned by the cancel operation.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``ScheduleCancelResponse``.
    """
    scheduled_chime: ScheduleCancelDetail | None = field(init=False)
    """The scheduled chime associated with this cancel response. Optional; nullable. Python type: ``ScheduleCancelDetail | None``; wire name: ``scheduled_chime``; JSON type: object (ScheduleCancelDetail)"""

from inttegro.schedule.cancel_detail import CancelDetail as ScheduleCancelDetail
