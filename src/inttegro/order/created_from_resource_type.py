"""CreatedFromResourceType in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class CreatedFromResourceType(WireEnum):
    """Typed created from resource type data in the order resource namespace.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``OrderCreatedFromResourceType``.
    """
    PURCHASE_INTENT = "purchase_intent"
    """Wire value ``purchase_intent`` (purchase intent)"""
