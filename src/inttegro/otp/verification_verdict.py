"""VerificationVerdict in the ``inttegro.otp`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class VerificationVerdict(WireEnum):
    """Typed verification verdict data in the otp resource namespace.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``OTPVerificationVerdict``.
    """
    FAIL = "fail"
    """Wire value ``fail`` (fail)"""
    PASS = "pass"
    """Wire value ``pass`` (pass)"""
