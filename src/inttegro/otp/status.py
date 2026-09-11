"""Status in the ``inttegro.otp`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class Status(WireEnum):
    """Typed status data in the otp resource namespace.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``OTPStatus``.
    """
    CANCELED = "canceled"
    """Wire value ``canceled`` (canceled)"""
    EXPIRED = "expired"
    """Wire value ``expired`` (expired)"""
    PENDING = "pending"
    """Wire value ``pending`` (pending)"""
    PENDING_DELIVERY = "pending_delivery"
    """Wire value ``pending_delivery`` (pending delivery)"""
    PENDING_VERIFICATION = "pending_verification"
    """Wire value ``pending_verification`` (pending verification)"""
    VERIFIED = "verified"
    """Wire value ``verified`` (verified)"""
