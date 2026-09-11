"""LatestError in the ``inttegro.file`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class LatestError(ApiModel):
    """Typed latest error data in the file resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``FileLatestError``.
    """
    code: str | None = field(init=False)
    """The code associated with this latest error. Optional; nullable. Python type: ``str | None``; wire name: ``code``; JSON type: string"""
    message: str | None = field(init=False)
    """The message associated with this latest error. Optional; nullable. Python type: ``str | None``; wire name: ``message``; JSON type: string"""
    retryable: bool | None = field(init=False)
    """Whether retryable. Optional; nullable. Python type: ``bool | None``; wire name: ``retryable``; JSON type: boolean"""
    at: datetime | None = field(init=False)
    """Timestamp for at. Optional; nullable. Python type: ``datetime | None``; wire name: ``at``; JSON type: string (date-time)"""
