"""Typed request objects for message-template operations."""

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
    "CreateEmailRequest",
    "CreateSMSRequest",
    "EmailContent",
    "Mailbox",
    "PageRequest",
    "RenderPreviewRequest",
    "SMSContent",
    "UpdateRequest",
    "Variable",
    "VariableItem",
]
