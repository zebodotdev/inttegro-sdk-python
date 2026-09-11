"""MobileMoneyNetwork in the ``inttegro.payment_method`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class MobileMoneyNetwork(WireEnum):
    """Mobile money service provider.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.
    """
    AIRTEL = "airtel"
    """Wire value ``airtel`` (airtel) for mobile money service provider"""
    MTN = "mtn"
    """Wire value ``mtn`` (mtn) for mobile money service provider"""
    TELECEL = "telecel"
    """Wire value ``telecel`` (telecel) for mobile money service provider"""
    VODAFONE = "vodafone"
    """Wire value ``vodafone`` (vodafone) for mobile money service provider"""
