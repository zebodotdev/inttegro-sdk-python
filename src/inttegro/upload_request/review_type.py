"""ReviewType in the ``inttegro.upload_request`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class ReviewType(WireEnum):
    """Typed review type data in the upload request resource namespace.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``UploadReviewType``.
    """
    AUTOMATIC = "automatic"
    """Wire value ``automatic`` (automatic)"""
    MANUAL = "manual"
    """Wire value ``manual`` (manual)"""
