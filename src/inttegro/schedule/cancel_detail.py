"""CancelDetail in the ``inttegro.schedule`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class CancelDetail(ApiModel):
    """Typed cancel detail data in the schedule resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``ScheduleCancelDetail``.
    """
    chime_ids: list[str] | None = field(init=False)
    """The chime ids associated with this cancel detail. Optional; nullable. Python type: ``list[str] | None``; wire name: ``chime_ids``; JSON type: array of string values"""
    content: str = field(init=False)
    """The content associated with this cancel detail. Required. Python type: ``str``; wire name: ``content``; JSON type: string"""
    created_at: datetime = field(init=False)
    """When the cancel detail was created. Required. Python type: ``datetime``; wire name: ``created_at``; JSON type: string (date-time)"""
    customer_ids: list[str] | None = field(init=False)
    """The customer ids associated with this cancel detail. Optional; nullable. Python type: ``list[str] | None``; wire name: ``customer_ids``; JSON type: array of string values"""
    email: ChimeEmailMessage | None = field(init=False)
    """Email content, safety scan result, and system-generated schema markup for email chimes. Optional; nullable. Python type: ``ChimeEmailMessage | None``; wire name: ``email``; JSON type: object (ChimeEmailMessage)"""
    errors: list[ScheduleError] | None = field(init=False)
    """The errors associated with this cancel detail. Optional; nullable. Python type: ``list[ScheduleError] | None``; wire name: ``errors``; JSON type: array of object (ScheduleError) values"""
    executed_at: datetime | None = field(init=False)
    """When execution of the cancel detail began. Optional; nullable. Python type: ``datetime | None``; wire name: ``executed_at``; JSON type: string (date-time)"""
    id: str = field(init=False)
    """Unique identifier for this cancel detail. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    idempotency_key: str | None = field(init=False)
    """Stable key used to make retries of the same logical write safe. Optional; nullable. Python type: ``str | None``; wire name: ``idempotency_key``; JSON type: string"""
    purpose: str | None = field(init=False)
    """The purpose associated with this cancel detail. Optional; nullable. Python type: ``str | None``; wire name: ``purpose``; JSON type: string"""
    recipients: list[str] = field(init=False)
    """The recipients associated with this cancel detail. Required. Python type: ``list[str]``; wire name: ``recipients``; JSON type: array of string values"""
    send_after: datetime = field(init=False)
    """Timestamp for send after. Required. Python type: ``datetime``; wire name: ``send_after``; JSON type: string (date-time)"""
    sender_id: str = field(init=False)
    """Identifier of the related sender. Required. Python type: ``str``; wire name: ``sender_id``; JSON type: string"""
    canceled_at: datetime | None = field(init=False)
    """When the cancel detail was canceled. Optional; nullable. Python type: ``datetime | None``; wire name: ``canceled_at``; JSON type: string (date-time)"""

from inttegro.chime.email_message import EmailMessage as ChimeEmailMessage
from inttegro.schedule.error import Error as ScheduleError
