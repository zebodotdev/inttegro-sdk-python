"""Attempts in the ``inttegro.upload_request`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Attempts(ApiModel):
    """Typed attempts data in the upload request resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``UploadRequestAttempts``.
    """
    max_attempts: int | None = field(init=False)
    """The max attempts associated with this attempt. Optional; nullable. Python type: ``int | None``; wire name: ``max_attempts``; JSON type: integer (int64)"""
    attempt_count: int = field(init=False)
    """The attempt count associated with this attempt. Required. Python type: ``int``; wire name: ``attempt_count``; JSON type: integer (int64)"""
    failed_attempt_count: int = field(init=False)
    """The failed attempt count associated with this attempt. Required. Python type: ``int``; wire name: ``failed_attempt_count``; JSON type: integer (int64)"""
    last_attempted_at: datetime | None = field(init=False)
    """Timestamp for last attempted at. Optional; nullable. Python type: ``datetime | None``; wire name: ``last_attempted_at``; JSON type: string (date-time)"""
