"""CreateSMSRequest in the ``inttegro.message_template`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class CreateSMSRequest(ApiRequest):
    """Parameters accepted by the create smsrequest operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``CreateSMSMessageTemplateRequest``.
    """
    about: str | UnsetType = field(default=UNSET)
    """The about associated with this create smsrequest. Optional. Python type: ``str``; wire name: ``about``; JSON type: string"""
    locale: str | UnsetType = field(default=UNSET)
    """The locale associated with this create smsrequest. Optional. Python type: ``str``; wire name: ``locale``; JSON type: string"""
    variables: list[MessageTemplateVariableInput] | UnsetType = field(default=UNSET)
    """The variables associated with this create smsrequest. Optional. Python type: ``list[MessageTemplateVariableInput]``; wire name: ``variables``; JSON type: array of object (MessageTemplateVariableInput) values"""
    channel: Literal['sms', MessageTemplateChannel.SMS]
    """The channel associated with this create smsrequest. Required. Python type: ``Literal['sms', MessageTemplateChannel.SMS]``; wire name: ``channel``; JSON type: string. Constraints: allowed values ``sms``"""
    name: str
    """Human-readable name of the create smsrequest. Required. Python type: ``str``; wire name: ``name``; JSON type: string"""
    purpose: str
    """The purpose associated with this create smsrequest. Required. Python type: ``str``; wire name: ``purpose``; JSON type: string"""
    sms: MessageTemplateSMSContentInput
    """The sms associated with this create smsrequest. Required. Python type: ``MessageTemplateSMSContentInput``; wire name: ``sms``; JSON type: object (MessageTemplateSMSContent)"""

from inttegro.message_template.channel import Channel as MessageTemplateChannel
from inttegro.message_template.sms_content_input import SMSContentInput as MessageTemplateSMSContentInput
from inttegro.message_template.variable_input import VariableInput as MessageTemplateVariableInput
