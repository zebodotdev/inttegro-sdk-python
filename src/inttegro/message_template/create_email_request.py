"""CreateEmailRequest in the ``inttegro.message_template`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class CreateEmailRequest(ApiRequest):
    """Parameters accepted by the create email request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``CreateEmailMessageTemplateRequest``.
    """
    about: str | UnsetType = field(default=UNSET)
    """The about associated with this create email request. Optional. Python type: ``str``; wire name: ``about``; JSON type: string"""
    attachments: MessageTemplateAttachmentIDsInput | UnsetType = field(default=UNSET)
    """Stored file IDs returned by previews. Chime send, schedule, and broadcast currently reject stored-template attachments. Optional. Python type: ``MessageTemplateAttachmentIDsInput``; wire name: ``attachments``; JSON type: object (MessageTemplateAttachmentIDs)"""
    locale: str | UnsetType = field(default=UNSET)
    """The locale associated with this create email request. Optional. Python type: ``str``; wire name: ``locale``; JSON type: string"""
    variables: list[MessageTemplateVariableInput] | UnsetType = field(default=UNSET)
    """The variables associated with this create email request. Optional. Python type: ``list[MessageTemplateVariableInput]``; wire name: ``variables``; JSON type: array of object (MessageTemplateVariableInput) values"""
    channel: Literal['email', MessageTemplateChannel.EMAIL]
    """The channel associated with this create email request. Required. Python type: ``Literal['email', MessageTemplateChannel.EMAIL]``; wire name: ``channel``; JSON type: string. Constraints: allowed values ``email``"""
    email: MessageTemplateEmailContentInput
    """The email associated with this create email request. Required. Python type: ``MessageTemplateEmailContentInput``; wire name: ``email``; JSON type: object (MessageTemplateEmailContent)"""
    name: str
    """Human-readable name of the create email request. Required. Python type: ``str``; wire name: ``name``; JSON type: string"""
    purpose: str
    """The purpose associated with this create email request. Required. Python type: ``str``; wire name: ``purpose``; JSON type: string"""

from inttegro.message_template.attachment_ids_input import AttachmentIDsInput as MessageTemplateAttachmentIDsInput
from inttegro.message_template.channel import Channel as MessageTemplateChannel
from inttegro.message_template.email_content_input import EmailContentInput as MessageTemplateEmailContentInput
from inttegro.message_template.variable_input import VariableInput as MessageTemplateVariableInput
