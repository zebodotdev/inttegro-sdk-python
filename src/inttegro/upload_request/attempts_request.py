"""AttemptsRequest in the ``inttegro.upload_request`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class AttemptsRequest(ApiRequest):
    """Parameters accepted by the attempts request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``UploadRequestAttemptsRequest``.
    """
    max_attempts: int | UnsetType = field(default=UNSET)
    """The max attempts associated with this attempts request. Optional. Python type: ``int``; wire name: ``max_attempts``; JSON type: integer (int64). Constraints: minimum 0"""
