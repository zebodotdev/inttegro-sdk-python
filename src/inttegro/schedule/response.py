"""Response in the ``inttegro.schedule`` resource namespace.

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

    API contract schema: ``ScheduleResponse``.
    """
    scheduled_chime: ScheduleCreationDetail | None = field(init=False)
    """The scheduled chime associated with this response. Optional; nullable. Python type: ``ScheduleCreationDetail | None``; wire name: ``scheduled_chime``; JSON type: object (ScheduleCreationDetail)"""

from inttegro.schedule.creation_detail import CreationDetail as ScheduleCreationDetail
