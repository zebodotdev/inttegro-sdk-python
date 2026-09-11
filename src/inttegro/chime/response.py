"""Response in the ``inttegro.chime`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Response(ApiModel):
    """Response containing chime details.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``ChimeResponse``.
    """
    chime: Chime | None = field(init=False)
    """A notification sent to one recipient. Optional; nullable. Python type: ``Chime | None``; wire name: ``chime``; JSON type: object (Chime)"""

from inttegro.chime.chime import Chime
