"""Typed request objects for message-template operations."""

from ._enums import (
    ContentSafetyStatus,
    MessageTemplateChannel,
    MessageTemplateStatus,
    MessageTemplateVariableItemType,
    MessageTemplateVariableType,
)
from .request_types import (
    CreateEmailMessageTemplateRequest as CreateEmailRequest,
    CreateSMSMessageTemplateRequest as CreateSMSRequest,
    MessageTemplateEmailContentInput as EmailContent,
    MessageTemplateMailboxInput as Mailbox,
    MessageTemplateSMSContentInput as SMSContent,
    MessageTemplateVariableInput as Variable,
    MessageTemplateVariableItemInput as VariableItem,
    PageMessageTemplatesRequest as PageRequest,
    RenderMessageTemplatePreviewRequest as RenderPreviewRequest,
    UpdateMessageTemplateRequest as UpdateRequest,
)

__all__ = [
    "ContentSafetyStatus",
    "CreateEmailRequest",
    "CreateSMSRequest",
    "EmailContent",
    "Mailbox",
    "MessageTemplateChannel",
    "MessageTemplateStatus",
    "MessageTemplateVariableItemType",
    "MessageTemplateVariableType",
    "PageRequest",
    "RenderPreviewRequest",
    "SMSContent",
    "UpdateRequest",
    "Variable",
    "VariableItem",
]
