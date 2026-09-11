"""TransmissionStatus in the ``inttegro.otp`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class TransmissionStatus(WireEnum):
    """Typed transmission status data in the otp resource namespace.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``OTPTransmissionStatus``.
    """
    DELIVERED = "delivered"
    """Wire value ``delivered`` (delivered)"""
    FAILED = "failed"
    """Wire value ``failed`` (failed)"""
    SUBMITTED = "submitted"
    """Wire value ``submitted`` (submitted)"""
