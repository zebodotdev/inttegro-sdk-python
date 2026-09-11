"""DeliveryMode in the ``inttegro.file_link`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class DeliveryMode(WireEnum):
    """Typed delivery mode data in the file link resource namespace.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``FileLinkDeliveryMode``.
    """
    REDIRECT = "redirect"
    """Wire value ``redirect`` (redirect)"""
    DOWNLOAD = "download"
    """Wire value ``download`` (download)"""
    INLINE = "inline"
    """Wire value ``inline`` (inline)"""
