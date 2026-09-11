"""Error in the ``inttegro.schedule`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Error(ApiModel):
    """Error encountered when scheduling a chime for a specific recipient.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``ScheduleError``.
    """
    recipient: str | None = field(init=False)
    """Recipient address that caused the error. Optional; nullable. Python type: ``str | None``; wire name: ``recipient``; JSON type: string"""
    fix_code: str | None = field(init=False)
    """Code indicating how to fix this error. Optional; nullable. Python type: ``str | None``; wire name: ``fix_code``; JSON type: string"""
    type: str | None = field(init=False)
    """Error type classification. Optional; nullable. Python type: ``str | None``; wire name: ``type``; JSON type: string"""
