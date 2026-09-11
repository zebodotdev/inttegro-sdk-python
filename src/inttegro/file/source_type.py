"""SourceType in the ``inttegro.file`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class SourceType(WireEnum):
    """Typed source type data in the file resource namespace.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``FileSourceType``.
    """
    DIRECT = "direct"
    """Wire value ``direct`` (direct)"""
    UPLOAD_REQUEST = "upload_request"
    """Wire value ``upload_request`` (upload request)"""
    SERVICE = "service"
    """Wire value ``service`` (service)"""
