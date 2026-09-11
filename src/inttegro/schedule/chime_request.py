"""ChimeRequest in the ``inttegro.schedule`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class ChimeRequest(ApiRequest):
    """Parameters accepted by the chime request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``ScheduleChimeRequest``.
    """
    request_meta: ScheduleChimeRequestRequestMeta | UnsetType = field(default=UNSET)
    """The request meta associated with this chime request. Optional. Python type: ``ScheduleChimeRequestRequestMeta``; wire name: ``request_meta``; JSON type: object"""
    full_message: str | UnsetType = field(default=UNSET)
    """Complete SMS message content. Use only with SMS recipients. Optional. Python type: ``str``; wire name: ``full_message``; JSON type: string"""
    email: ChimeEmailMessageInput | UnsetType = field(default=UNSET)
    """Email content accepted for email chimes, broadcasts, and schedules. Optional. Python type: ``ChimeEmailMessageInput``; wire name: ``email``; JSON type: object (ChimeEmailMessageInput)"""
    message_template: MessageTemplateReferenceInput | UnsetType = field(default=UNSET)
    """The message template associated with this chime request. Optional. Python type: ``MessageTemplateReferenceInput``; wire name: ``message_template``; JSON type: object (MessageTemplateReference)"""
    sender_id: str | UnsetType = field(default=UNSET)
    """Sender identifier displayed to recipients. Optional. Python type: ``str``; wire name: ``sender_id``; JSON type: string"""
    purpose: str | UnsetType = field(default=UNSET)
    """Optional purpose or category for this scheduled chime. Optional. Python type: ``str``; wire name: ``purpose``; JSON type: string"""
    recipients: list[ChimeRecipientInput]
    """Recipient objects for this scheduled chime. Each item must include `transport` and either inline contact details or `customer_id`. Required. Python type: ``list[ChimeRecipientInput]``; wire name: ``recipients``; JSON type: array of object (ChimeRecipient) values. Constraints: minimum items 1"""
    send_after: datetime
    """ISO 8601 timestamp for when to send the chime (must be in the future). Required. Python type: ``datetime``; wire name: ``send_after``; JSON type: string (date-time)"""

from inttegro.chime.email_message_input import EmailMessageInput as ChimeEmailMessageInput
from inttegro.chime.recipient_input import RecipientInput as ChimeRecipientInput
from inttegro.message_template.reference_input import ReferenceInput as MessageTemplateReferenceInput
from inttegro.schedule.chime_request_request_meta import ChimeRequestRequestMeta as ScheduleChimeRequestRequestMeta
