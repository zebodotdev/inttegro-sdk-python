"""UpdateRequest in the ``inttegro.message_template`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class UpdateRequest(ApiRequest):
    """Parameters accepted by the update request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``UpdateMessageTemplateRequest``.
    """
    name: str | UnsetType = field(default=UNSET)
    """Human-readable template name. Optional. Python type: ``str``; wire name: ``name``; JSON type: string"""
    about: str | UnsetType = field(default=UNSET)
    """Optional description of when this template should be used. Optional. Python type: ``str``; wire name: ``about``; JSON type: string"""
    channel: Literal['sms', 'email', MessageTemplateChannel.SMS, MessageTemplateChannel.EMAIL] | UnsetType = field(default=UNSET)
    """Existing template channel. Channels cannot be changed. Optional. Python type: ``Literal['sms', 'email', MessageTemplateChannel.SMS, MessageTemplateChannel.EMAIL]``; wire name: ``channel``; JSON type: string. Constraints: allowed values ``sms``, ``email``"""
    purpose: str | UnsetType = field(default=UNSET)
    """Caller-defined purpose for filtering and analytics. Optional. Python type: ``str``; wire name: ``purpose``; JSON type: string"""
    locale: str | UnsetType = field(default=UNSET)
    """The locale associated with this update request. Optional. Python type: ``str``; wire name: ``locale``; JSON type: string"""
    variables: list[MessageTemplateVariableInput] | UnsetType = field(default=UNSET)
    """The variables associated with this update request. Optional. Python type: ``list[MessageTemplateVariableInput]``; wire name: ``variables``; JSON type: array of object (MessageTemplateVariableInput) values"""
    sms: MessageTemplateSMSContentInput | UnsetType = field(default=UNSET)
    """The sms associated with this update request. Optional. Python type: ``MessageTemplateSMSContentInput``; wire name: ``sms``; JSON type: object (MessageTemplateSMSContent)"""
    email: MessageTemplateEmailContentInput | UnsetType = field(default=UNSET)
    """The email associated with this update request. Optional. Python type: ``MessageTemplateEmailContentInput``; wire name: ``email``; JSON type: object (MessageTemplateEmailContent)"""
    attachments: MessageTemplateAttachmentIDsInput | UnsetType = field(default=UNSET)
    """Stored file IDs returned by previews. Chime send, schedule, and broadcast currently reject stored-template attachments. Optional. Python type: ``MessageTemplateAttachmentIDsInput``; wire name: ``attachments``; JSON type: object (MessageTemplateAttachmentIDs)"""
    id: str
    """API-generated message template id. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""

from inttegro.message_template.attachment_ids_input import AttachmentIDsInput as MessageTemplateAttachmentIDsInput
from inttegro.message_template.channel import Channel as MessageTemplateChannel
from inttegro.message_template.email_content_input import EmailContentInput as MessageTemplateEmailContentInput
from inttegro.message_template.sms_content_input import SMSContentInput as MessageTemplateSMSContentInput
from inttegro.message_template.variable_input import VariableInput as MessageTemplateVariableInput
