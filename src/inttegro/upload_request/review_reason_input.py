"""ReviewReasonInput in the ``inttegro.upload_request`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class ReviewReasonInput(ApiRequest):
    """Parameters accepted by the review reason input operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``UploadRequestReviewReasonInput``.
    """
    param: str | UnsetType = field(default=UNSET)
    """The param associated with this review reason input. Optional. Python type: ``str``; wire name: ``param``; JSON type: string"""
    code: str
    """The code associated with this review reason input. Required. Python type: ``str``; wire name: ``code``; JSON type: string. Constraints: minimum length 1"""
    message: str
    """The message associated with this review reason input. Required. Python type: ``str``; wire name: ``message``; JSON type: string. Constraints: minimum length 1"""
