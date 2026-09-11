"""VerifyRequest in the ``inttegro.otp`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass
from inttegro._request_base import ApiRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class VerifyRequest(ApiRequest):
    """Parameters accepted by the verify request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``VerifyOTPRequest``.
    """
    transaction_id: str
    """ID of the OTP transaction to verify (with ot_ prefix). Required. Python type: ``str``; wire name: ``transaction_id``; JSON type: string"""
    recipient: str
    """Phone number that received the OTP. Required. Python type: ``str``; wire name: ``recipient``; JSON type: string"""
    token: str
    """OTP token submitted by the user. Required. Python type: ``str``; wire name: ``token``; JSON type: string"""
