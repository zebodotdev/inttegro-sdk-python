"""DeliveryChannel in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class DeliveryChannel(WireEnum):
    """Delivery channel.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.
    """
    EMAIL = "email"
    """Wire value ``email`` (email) for delivery channel"""
    SMS = "sms"
    """Wire value ``sms`` (sms) for delivery channel"""
