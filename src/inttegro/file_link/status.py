"""Status in the ``inttegro.file_link`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class Status(WireEnum):
    """Typed status data in the file link resource namespace.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``FileLinkStatus``.
    """
    ACTIVE = "active"
    """Wire value ``active`` (active)"""
    REVOKED = "revoked"
    """Wire value ``revoked`` (revoked)"""
    EXPIRED = "expired"
    """Wire value ``expired`` (expired)"""
    DISABLED = "disabled"
    """Wire value ``disabled`` (disabled)"""
