"""VerificationAttempt in the ``inttegro.otp`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class VerificationAttempt(ApiModel):
    """Details of a verification attempt.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``OTPVerificationAttempt``.
    """
    attempted_at: datetime = field(init=False)
    """Timestamp for attempted at. Required. Python type: ``datetime``; wire name: ``attempted_at``; JSON type: string (date-time)"""
    id: str = field(init=False)
    """Unique identifier for this verification attempt. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    presented_token: str = field(init=False)
    """Token submitted for this verification attempt. Required. Python type: ``str``; wire name: ``presented_token``; JSON type: string"""
    recipient: str = field(init=False)
    """The recipient associated with this verification attempt. Required. Python type: ``str``; wire name: ``recipient``; JSON type: string"""
    result: OTPVerificationAttemptResult = field(init=False)
    """The result associated with this verification attempt. Required. Python type: ``OTPVerificationAttemptResult``; wire name: ``result``; JSON type: object"""

from inttegro.otp.verification_attempt_result import VerificationAttemptResult as OTPVerificationAttemptResult
