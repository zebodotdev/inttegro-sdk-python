"""Channel in the ``inttegro.message_template`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class Channel(WireEnum):
    """Typed channel data in the message template resource namespace.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``MessageTemplateChannel``.
    """
    SMS = "sms"
    """Wire value ``sms`` (sms)"""
    EMAIL = "email"
    """Wire value ``email`` (email)"""
