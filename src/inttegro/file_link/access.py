"""Access in the ``inttegro.file_link`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Access(ApiModel):
    """Typed access data in the file link resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``FileLinkAccess``.
    """
    max_accesses: int | None = field(init=False)
    """The max accesses associated with this access. Optional; nullable. Python type: ``int | None``; wire name: ``max_accesses``; JSON type: integer (int64)"""
    access_count: int | None = field(init=False)
    """The access count associated with this access. Optional; nullable. Python type: ``int | None``; wire name: ``access_count``; JSON type: integer (int64)"""
    last_accessed_at: datetime | None = field(init=False)
    """Timestamp for last accessed at. Optional; nullable. Python type: ``datetime | None``; wire name: ``last_accessed_at``; JSON type: string (date-time)"""
    allow_download: bool | None = field(init=False)
    """Whether allow download. Optional; nullable. Python type: ``bool | None``; wire name: ``allow_download``; JSON type: boolean"""
    allowed_origins: list[str] | None = field(init=False)
    """The allowed origins associated with this access. Optional; nullable. Python type: ``list[str] | None``; wire name: ``allowed_origins``; JSON type: array of string values"""
