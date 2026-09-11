"""Status in the ``inttegro.file`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class Status(WireEnum):
    """Typed status data in the file resource namespace.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``FileStatus``.
    """
    UPLOADING = "uploading"
    """Wire value ``uploading`` (uploading)"""
    PROCESSING = "processing"
    """Wire value ``processing`` (processing)"""
    AVAILABLE = "available"
    """Wire value ``available`` (available)"""
    FAILED = "failed"
    """Wire value ``failed`` (failed)"""
    DELETED = "deleted"
    """Wire value ``deleted`` (deleted)"""
