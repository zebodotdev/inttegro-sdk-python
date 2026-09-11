"""RelationshipStatus in the ``inttegro.app`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class RelationshipStatus(WireEnum):
    """Typed relationship status data in the app resource namespace.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``AppRelationshipStatus``.
    """
    ACTIVE = "active"
    """Wire value ``active`` (active)"""
    INACTIVE = "inactive"
    """Wire value ``inactive`` (inactive)"""
    SUSPENDED = "suspended"
    """Wire value ``suspended`` (suspended)"""
    REVOKED = "revoked"
    """Wire value ``revoked`` (revoked)"""
