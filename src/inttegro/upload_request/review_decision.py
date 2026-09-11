"""ReviewDecision in the ``inttegro.upload_request`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class ReviewDecision(WireEnum):
    """Typed review decision data in the upload request resource namespace.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``UploadReviewDecision``.
    """
    APPROVED = "approved"
    """Wire value ``approved`` (approved)"""
    REJECTED = "rejected"
    """Wire value ``rejected`` (rejected)"""
