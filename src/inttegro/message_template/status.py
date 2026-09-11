"""Status in the ``inttegro.message_template`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class Status(WireEnum):
    """Typed status data in the message template resource namespace.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``MessageTemplateStatus``.
    """
    DRAFT = "draft"
    """Wire value ``draft`` (draft)"""
    PUBLISHED = "published"
    """Wire value ``published`` (published)"""
    ARCHIVED = "archived"
    """Wire value ``archived`` (archived)"""
