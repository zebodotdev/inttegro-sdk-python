"""LookupResponse in the ``inttegro.broadcast`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class LookupResponse(ApiModel):
    """Typed response returned by the lookup operation.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``LookupBroadcastResponse``.
    """
    broadcast: BroadcastDetail | None = field(init=False)
    """The broadcast associated with this lookup response. Optional; nullable. Python type: ``BroadcastDetail | None``; wire name: ``broadcast``; JSON type: object (BroadcastDetail)"""

from inttegro.broadcast.broadcast import Broadcast as BroadcastDetail
