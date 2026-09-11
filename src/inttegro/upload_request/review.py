"""Review in the ``inttegro.upload_request`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Review(ApiModel):
    """Typed review data in the upload request resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``UploadRequestReview``.
    """
    created_at: datetime = field(init=False)
    """When the review was created. Required. Python type: ``datetime``; wire name: ``created_at``; JSON type: string (date-time)"""
    decision: Literal['approved', 'rejected'] = field(init=False)
    """The decision associated with this review. Required. Python type: ``Literal['approved', 'rejected']``; wire name: ``decision``; JSON type: string. Constraints: allowed values ``approved``, ``rejected``"""
    file_id: str | None = field(init=False)
    """Identifier of the related file. Optional; nullable. Python type: ``str | None``; wire name: ``file_id``; JSON type: string"""
    public_message: str | None = field(init=False)
    """The public message associated with this review. Optional; nullable. Python type: ``str | None``; wire name: ``public_message``; JSON type: string"""
    reasons: list[UploadRequestReviewReason] | None = field(init=False)
    """The reasons associated with this review. Optional; nullable. Python type: ``list[UploadRequestReviewReason] | None``; wire name: ``reasons``; JSON type: array of object (UploadRequestReviewReason) values"""
    reviewed_at: datetime = field(init=False)
    """Timestamp for reviewed at. Required. Python type: ``datetime``; wire name: ``reviewed_at``; JSON type: string (date-time)"""
    type: Literal['automatic', 'manual'] = field(init=False)
    """Discriminator identifying the review type. Required. Python type: ``Literal['automatic', 'manual']``; wire name: ``type``; JSON type: string. Constraints: allowed values ``automatic``, ``manual``"""

from inttegro.upload_request.review_reason import ReviewReason as UploadRequestReviewReason
