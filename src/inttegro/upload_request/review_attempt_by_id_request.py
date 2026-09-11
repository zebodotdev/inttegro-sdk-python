"""ReviewAttemptByIDRequest in the ``inttegro.upload_request`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class ReviewAttemptByIDRequest(ApiRequest):
    """Parameters accepted by the review attempt by idrequest operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``ReviewUploadRequestAttemptByIDRequest``.
    """
    public_message: str | UnsetType = field(default=UNSET)
    """The public message associated with this review attempt by idrequest. Optional. Python type: ``str``; wire name: ``public_message``; JSON type: string"""
    reasons: list[UploadRequestReviewReasonInput] | UnsetType = field(default=UNSET)
    """The reasons associated with this review attempt by idrequest. Optional. Python type: ``list[UploadRequestReviewReasonInput]``; wire name: ``reasons``; JSON type: array of object (UploadRequestReviewReasonInput) values"""
    attempt_id: str
    """Identifier of the related attempt. Required. Python type: ``str``; wire name: ``attempt_id``; JSON type: string. Constraints: minimum length 1"""
    decision: Literal['approved', 'rejected', UploadReviewDecision.APPROVED, UploadReviewDecision.REJECTED]
    """The decision associated with this review attempt by idrequest. Required. Python type: ``Literal['approved', 'rejected', UploadReviewDecision.APPROVED, UploadReviewDecision.REJECTED]``; wire name: ``decision``; JSON type: string. Constraints: allowed values ``approved``, ``rejected``"""
    id: str
    """Unique identifier for this review attempt by idrequest. Required. Python type: ``str``; wire name: ``id``; JSON type: string. Constraints: minimum length 1"""

from inttegro.upload_request.review_reason_input import ReviewReasonInput as UploadRequestReviewReasonInput
from inttegro.upload_request.review_decision import ReviewDecision as UploadReviewDecision
