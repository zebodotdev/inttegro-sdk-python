"""Verification in the ``inttegro.otp`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Verification(ApiModel):
    """Typed verification data in the otp resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``OTPVerification``.
    """
    transaction: OTPTransaction = field(init=False)
    """OTP transaction object returned by initiate, verify, and lookup endpoints. Required. Python type: ``OTPTransaction``; wire name: ``transaction``; JSON type: object (OTPTransaction)"""
    verification_attempt: OTPVerificationAttempt = field(init=False)
    """Details of a verification attempt. Required. Python type: ``OTPVerificationAttempt``; wire name: ``verification_attempt``; JSON type: object (OTPVerificationAttempt)"""

from inttegro.otp.transaction import Transaction as OTPTransaction
from inttegro.otp.verification_attempt import VerificationAttempt as OTPVerificationAttempt
