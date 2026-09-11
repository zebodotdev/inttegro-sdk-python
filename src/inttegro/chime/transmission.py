"""Transmission in the ``inttegro.chime`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Transmission(ApiModel):
    """Typed transmission data in the chime resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``ChimeTransmission``.
    """
    address: str = field(init=False)
    """The address associated with this transmission. Required. Python type: ``str``; wire name: ``address``; JSON type: string"""
    created_at: datetime = field(init=False)
    """When the transmission was created. Required. Python type: ``datetime``; wire name: ``created_at``; JSON type: string (date-time)"""
    delivered_at: datetime | None = field(init=False)
    """Timestamp for delivered at. Optional; nullable. Python type: ``datetime | None``; wire name: ``delivered_at``; JSON type: string (date-time)"""
    email_events: list[ChimeEmailEvent] | None = field(init=False)
    """The email events associated with this transmission. Optional; nullable. Python type: ``list[ChimeEmailEvent] | None``; wire name: ``email_events``; JSON type: array of object (ChimeEmailEvent) values"""
    email_failure_code: str | None = field(init=False)
    """The email failure code associated with this transmission. Optional; nullable. Python type: ``str | None``; wire name: ``email_failure_code``; JSON type: string"""
    email_failure_reason: str | None = field(init=False)
    """The email failure reason associated with this transmission. Optional; nullable. Python type: ``str | None``; wire name: ``email_failure_reason``; JSON type: string"""
    email_status: str | None = field(init=False)
    """The email status associated with this transmission. Optional; nullable. Python type: ``str | None``; wire name: ``email_status``; JSON type: string"""
    error: str | None = field(init=False)
    """The error associated with this transmission. Optional; nullable. Python type: ``str | None``; wire name: ``error``; JSON type: string"""
    failed_at: datetime | None = field(init=False)
    """When the transmission failed. Optional; nullable. Python type: ``datetime | None``; wire name: ``failed_at``; JSON type: string (date-time)"""
    gateway: str = field(init=False)
    """The gateway associated with this transmission. Required. Python type: ``str``; wire name: ``gateway``; JSON type: string"""
    gateway_message_id: str | None = field(init=False)
    """Identifier of the related gateway message. Optional; nullable. Python type: ``str | None``; wire name: ``gateway_message_id``; JSON type: string"""
    id: str = field(init=False)
    """Unique identifier for this transmission. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    initialized_at: datetime = field(init=False)
    """Timestamp for initialized at. Required. Python type: ``datetime``; wire name: ``initialized_at``; JSON type: string (date-time)"""
    last_email_event_at: datetime | None = field(init=False)
    """Timestamp for last email event at. Optional; nullable. Python type: ``datetime | None``; wire name: ``last_email_event_at``; JSON type: string (date-time)"""
    mechanism: Literal['sms', 'email'] = field(init=False)
    """The mechanism associated with this transmission. Required. Python type: ``Literal['sms', 'email']``; wire name: ``mechanism``; JSON type: string. Constraints: allowed values ``sms``, ``email``"""
    sent_at: datetime | None = field(init=False)
    """Timestamp for sent at. Optional; nullable. Python type: ``datetime | None``; wire name: ``sent_at``; JSON type: string (date-time)"""
    sent_via: Literal['sms', 'email'] | None = field(init=False)
    """The sent via associated with this transmission. Optional; nullable. Python type: ``Literal['sms', 'email'] | None``; wire name: ``sent_via``; JSON type: string. Constraints: allowed values ``sms``, ``email``"""
    status: str = field(init=False)
    """Current lifecycle status of the transmission. Required. Python type: ``str``; wire name: ``status``; JSON type: string"""
    suppressed_at: datetime | None = field(init=False)
    """Timestamp for suppressed at. Optional; nullable. Python type: ``datetime | None``; wire name: ``suppressed_at``; JSON type: string (date-time)"""
    suppression_reason: str | None = field(init=False)
    """The suppression reason associated with this transmission. Optional; nullable. Python type: ``str | None``; wire name: ``suppression_reason``; JSON type: string"""

from inttegro.chime.email_event import EmailEvent as ChimeEmailEvent
