"""Transmission in the ``inttegro.otp`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Transmission(ApiModel):
    """Typed transmission data in the otp resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``OTPTransmission``.
    """
    recipient: str = field(init=False)
    """The recipient associated with this transmission. Required. Python type: ``str``; wire name: ``recipient``; JSON type: string"""
    sender_id: str = field(init=False)
    """Identifier of the related sender. Required. Python type: ``str``; wire name: ``sender_id``; JSON type: string"""
    sent_at: datetime | None = field(init=False)
    """Timestamp for sent at. Optional; nullable. Python type: ``datetime | None``; wire name: ``sent_at``; JSON type: string (date-time)"""
    sent_via: Literal['sms'] | None = field(init=False)
    """The sent via associated with this transmission. Optional; nullable. Python type: ``Literal['sms'] | None``; wire name: ``sent_via``; JSON type: string. Constraints: allowed values ``sms``"""
    status: Literal['delivered', 'failed', 'submitted'] | None = field(init=False)
    """Current lifecycle status of the transmission. Optional; nullable. Python type: ``Literal['delivered', 'failed', 'submitted'] | None``; wire name: ``status``; JSON type: string. Constraints: allowed values ``delivered``, ``failed``, ``submitted``"""
