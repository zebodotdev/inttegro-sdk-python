"""RelationshipKind in the ``inttegro.app`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class RelationshipKind(WireEnum):
    """Typed relationship kind data in the app resource namespace.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``AppRelationshipKind``.
    """
    PLACEMENT = "placement"
    """Wire value ``placement`` (placement)"""
