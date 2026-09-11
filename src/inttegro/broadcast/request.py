"""Request in the ``inttegro.broadcast`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class Request(ApiRequest):
    """Parameters accepted by the request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``BroadcastRequest``.
    """
    request_meta: BroadcastRequestRequestMeta | UnsetType = field(default=UNSET)
    """The request meta associated with this request. Optional. Python type: ``BroadcastRequestRequestMeta``; wire name: ``request_meta``; JSON type: object"""
    message_template: str | MessageTemplateReferenceInput | UnsetType = field(default=UNSET)
    """Raw SMS content for SMS broadcasts, or a stored message template reference for SMS or email broadcasts. Optional. Python type: ``str | MessageTemplateReferenceInput``; wire name: ``message_template``; JSON type: one of the documented JSON shapes"""
    email: ChimeEmailMessageInput | UnsetType = field(default=UNSET)
    """Email content accepted for email chimes, broadcasts, and schedules. Optional. Python type: ``ChimeEmailMessageInput``; wire name: ``email``; JSON type: object (ChimeEmailMessageInput)"""
    purpose: str | UnsetType = field(default=UNSET)
    """Category or intent for this broadcast. Optional. Python type: ``str``; wire name: ``purpose``; JSON type: string"""
    sender: str | UnsetType = field(default=UNSET)
    """Sender identifier displayed to recipients. Optional. Python type: ``str``; wire name: ``sender``; JSON type: string"""
    recipients: list[ChimeRecipientInput]
    """Recipient objects for this broadcast. Each item must include `transport` and either inline contact details or `customer_id`. Required. Python type: ``list[ChimeRecipientInput]``; wire name: ``recipients``; JSON type: array of object (ChimeRecipient) values. Constraints: minimum items 1"""

from inttegro.broadcast.request_request_meta import RequestRequestMeta as BroadcastRequestRequestMeta
from inttegro.chime.email_message_input import EmailMessageInput as ChimeEmailMessageInput
from inttegro.chime.recipient_input import RecipientInput as ChimeRecipientInput
from inttegro.message_template.reference_input import ReferenceInput as MessageTemplateReferenceInput
