"""Transaction in the ``inttegro.otp`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Transaction(ApiModel):
    """OTP transaction object returned by initiate, verify, and lookup endpoints.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``OTPTransaction``.
    """
    cancel_reason: str | None = field(init=False)
    """Omitted unless the transaction was canceled. Optional; nullable. Python type: ``str | None``; wire name: ``cancel_reason``; JSON type: string"""
    canceled_at: datetime | None = field(init=False)
    """Omitted unless the transaction was canceled. Optional; nullable. Python type: ``datetime | None``; wire name: ``canceled_at``; JSON type: string (date-time)"""
    expires_at: datetime = field(init=False)
    """Timestamp for expires at. Required. Python type: ``datetime``; wire name: ``expires_at``; JSON type: string (date-time)"""
    full_message: str = field(init=False)
    """Message text with the `{token}` placeholder preserved; no generated token is returned. Required. Python type: ``str``; wire name: ``full_message``; JSON type: string"""
    id: str = field(init=False)
    """Unique identifier with ot_ prefix. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    initiated_at: datetime = field(init=False)
    """Timestamp for initiated at. Required. Python type: ``datetime``; wire name: ``initiated_at``; JSON type: string (date-time)"""
    status: Literal['canceled', 'expired', 'pending', 'pending_delivery', 'pending_verification', 'verified'] = field(init=False)
    """Current lifecycle status of the transaction. Required. Python type: ``Literal['canceled', 'expired', 'pending', 'pending_delivery', 'pending_verification', 'verified']``; wire name: ``status``; JSON type: string. Constraints: allowed values ``canceled``, ``expired``, ``pending``, ``pending_delivery``, ``pending_verification``, ``verified``"""
    transmission: OTPTransmission | None = field(init=False)
    """The transmission associated with this transaction. Optional; nullable. Python type: ``OTPTransmission | None``; wire name: ``transmission``; JSON type: object (OTPTransmission)"""

from inttegro.otp.transmission import Transmission as OTPTransmission
