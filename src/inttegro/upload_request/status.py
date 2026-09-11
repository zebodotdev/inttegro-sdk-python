"""Status in the ``inttegro.upload_request`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class Status(WireEnum):
    """Typed status data in the upload request resource namespace.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``UploadRequestStatus``.
    """
    PENDING = "pending"
    """Wire value ``pending`` (pending)"""
    UPLOADING = "uploading"
    """Wire value ``uploading`` (uploading)"""
    FULFILLED = "fulfilled"
    """Wire value ``fulfilled`` (fulfilled)"""
    EXPIRED = "expired"
    """Wire value ``expired`` (expired)"""
    CANCELED = "canceled"
    """Wire value ``canceled`` (canceled)"""
    FAILED = "failed"
    """Wire value ``failed`` (failed)"""
