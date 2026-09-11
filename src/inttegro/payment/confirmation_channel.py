"""ConfirmationChannel in the ``inttegro.payment`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class ConfirmationChannel(WireEnum):
    """Channel used to send the token.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``PaymentConfirmationChannel``.
    """
    SMS = "sms"
    """Wire value ``sms`` (sms) for channel used to send the token"""
    EMAIL = "email"
    """Wire value ``email`` (email) for channel used to send the token"""
    PUSH = "push"
    """Wire value ``push`` (push) for channel used to send the token"""
