"""Error in the ``inttegro.payout`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Error(ApiModel):
    """Public failure details when execution fails.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PayoutError``.
    """
    cause: str = field(init=False)
    """The cause associated with this error. Required. Python type: ``str``; wire name: ``cause``; JSON type: string"""
    message: str = field(init=False)
    """The message associated with this error. Required. Python type: ``str``; wire name: ``message``; JSON type: string"""
    occurred_at: datetime = field(init=False)
    """Timestamp for occurred at. Required. Python type: ``datetime``; wire name: ``occurred_at``; JSON type: string (date-time)"""
    type: str = field(init=False)
    """Discriminator identifying the error type. Required. Python type: ``str``; wire name: ``type``; JSON type: string"""
