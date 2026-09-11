"""Attempt in the ``inttegro.upload_request`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Attempt(ApiModel):
    """Typed attempt data in the upload request resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``UploadRequestAttempt``.
    """
    attempted_at: datetime = field(init=False)
    """Timestamp for attempted at. Required. Python type: ``datetime``; wire name: ``attempted_at``; JSON type: string (date-time)"""
    content_type: str | None = field(init=False)
    """The content type associated with this attempt. Optional; nullable. Python type: ``str | None``; wire name: ``content_type``; JSON type: string"""
    declared_size: int | None = field(init=False)
    """The declared size associated with this attempt. Optional; nullable. Python type: ``int | None``; wire name: ``declared_size``; JSON type: integer (int64). Constraints: minimum 0"""
    error: UploadRequestLatestError | None = field(init=False)
    """The error associated with this attempt. Optional; nullable. Python type: ``UploadRequestLatestError | None``; wire name: ``error``; JSON type: object (UploadRequestLatestError)"""
    failed_at: datetime | None = field(init=False)
    """When the attempt failed. Optional; nullable. Python type: ``datetime | None``; wire name: ``failed_at``; JSON type: string (date-time)"""
    file_id: str | None = field(init=False)
    """Identifier of the related file. Optional; nullable. Python type: ``str | None``; wire name: ``file_id``; JSON type: string"""
    filename: str | None = field(init=False)
    """The filename associated with this attempt. Optional; nullable. Python type: ``str | None``; wire name: ``filename``; JSON type: string"""
    id: str = field(init=False)
    """Unique identifier for this attempt. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    ordinal: int = field(init=False)
    """The ordinal associated with this attempt. Required. Python type: ``int``; wire name: ``ordinal``; JSON type: integer (int64). Constraints: minimum 1"""
    review: UploadRequestReview | None = field(init=False)
    """The review associated with this attempt. Optional; nullable. Python type: ``UploadRequestReview | None``; wire name: ``review``; JSON type: object (UploadRequestReview)"""
    status: str = field(init=False)
    """Current lifecycle status of the attempt. Required. Python type: ``str``; wire name: ``status``; JSON type: string"""
    succeeded_at: datetime | None = field(init=False)
    """Timestamp for succeeded at. Optional; nullable. Python type: ``datetime | None``; wire name: ``succeeded_at``; JSON type: string (date-time)"""
    upload_request_id: str = field(init=False)
    """Identifier of the related upload request. Required. Python type: ``str``; wire name: ``upload_request_id``; JSON type: string"""

from inttegro.upload_request.latest_error import LatestError as UploadRequestLatestError
from inttegro.upload_request.review import Review as UploadRequestReview
