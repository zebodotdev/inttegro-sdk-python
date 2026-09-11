"""Models, requests, and enums for the Inttegro message template resource.

The primary returned object is ``inttegro.message_template.MessageTemplate``. Related request types, nested response shapes, and string-backed enums are exported from this singular namespace. Public members load lazily, so importing one resource does not eagerly import the entire SDK."""

from importlib import import_module
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .attachment_ids import AttachmentIDs as AttachmentIDs
    from .attachment_ids_input import AttachmentIDsInput as AttachmentIDsInput
    from .channel import Channel as Channel
    from .create_email_request import CreateEmailRequest as CreateEmailRequest
    from .create_request import CreateRequest as CreateRequest
    from .create_sms_request import CreateSMSRequest as CreateSMSRequest
    from .email_content import EmailContent as EmailContent
    from .email_content_input import EmailContentInput as EmailContentInput
    from .envelope import Envelope as Envelope
    from .id_request import IDRequest as IDRequest
    from .mailbox import Mailbox as Mailbox
    from .mailbox_input import MailboxInput as MailboxInput
    from .message_template import MessageTemplate as MessageTemplate
    from .page import Page as Page
    from .page_envelope import PageEnvelope as PageEnvelope
    from .page_request import PageRequest as PageRequest
    from .preview import Preview as Preview
    from .reference_input import ReferenceInput as ReferenceInput
    from .render_preview_request import RenderPreviewRequest as RenderPreviewRequest
    from .rendered import Rendered as Rendered
    from .rendered_email import RenderedEmail as RenderedEmail
    from .rendered_sms import RenderedSMS as RenderedSMS
    from .sms_content import SMSContent as SMSContent
    from .sms_content_input import SMSContentInput as SMSContentInput
    from .safety_result import SafetyResult as SafetyResult
    from .scanned_link import ScannedLink as ScannedLink
    from .status import Status as Status
    from .update_request import UpdateRequest as UpdateRequest
    from .variable import Variable as Variable
    from .variable_input import VariableInput as VariableInput
    from .variable_item import VariableItem as VariableItem
    from .variable_item_input import VariableItemInput as VariableItemInput
    from .variable_item_type import VariableItemType as VariableItemType
    from .variable_type import VariableType as VariableType
    from .variables_input import VariablesInput as VariablesInput


_EXPORTS: dict[str, tuple[str, str]] = {
    "AttachmentIDs": ("inttegro.message_template.attachment_ids", "AttachmentIDs"),
    "AttachmentIDsInput": ("inttegro.message_template.attachment_ids_input", "AttachmentIDsInput"),
    "Channel": ("inttegro.message_template.channel", "Channel"),
    "CreateEmailRequest": ("inttegro.message_template.create_email_request", "CreateEmailRequest"),
    "CreateRequest": ("inttegro.message_template.create_request", "CreateRequest"),
    "CreateSMSRequest": ("inttegro.message_template.create_sms_request", "CreateSMSRequest"),
    "EmailContent": ("inttegro.message_template.email_content", "EmailContent"),
    "EmailContentInput": ("inttegro.message_template.email_content_input", "EmailContentInput"),
    "Envelope": ("inttegro.message_template.envelope", "Envelope"),
    "IDRequest": ("inttegro.message_template.id_request", "IDRequest"),
    "Mailbox": ("inttegro.message_template.mailbox", "Mailbox"),
    "MailboxInput": ("inttegro.message_template.mailbox_input", "MailboxInput"),
    "MessageTemplate": ("inttegro.message_template.message_template", "MessageTemplate"),
    "Page": ("inttegro.message_template.page", "Page"),
    "PageEnvelope": ("inttegro.message_template.page_envelope", "PageEnvelope"),
    "PageRequest": ("inttegro.message_template.page_request", "PageRequest"),
    "Preview": ("inttegro.message_template.preview", "Preview"),
    "ReferenceInput": ("inttegro.message_template.reference_input", "ReferenceInput"),
    "RenderPreviewRequest": ("inttegro.message_template.render_preview_request", "RenderPreviewRequest"),
    "Rendered": ("inttegro.message_template.rendered", "Rendered"),
    "RenderedEmail": ("inttegro.message_template.rendered_email", "RenderedEmail"),
    "RenderedSMS": ("inttegro.message_template.rendered_sms", "RenderedSMS"),
    "SMSContent": ("inttegro.message_template.sms_content", "SMSContent"),
    "SMSContentInput": ("inttegro.message_template.sms_content_input", "SMSContentInput"),
    "SafetyResult": ("inttegro.message_template.safety_result", "SafetyResult"),
    "ScannedLink": ("inttegro.message_template.scanned_link", "ScannedLink"),
    "Status": ("inttegro.message_template.status", "Status"),
    "UpdateRequest": ("inttegro.message_template.update_request", "UpdateRequest"),
    "Variable": ("inttegro.message_template.variable", "Variable"),
    "VariableInput": ("inttegro.message_template.variable_input", "VariableInput"),
    "VariableItem": ("inttegro.message_template.variable_item", "VariableItem"),
    "VariableItemInput": ("inttegro.message_template.variable_item_input", "VariableItemInput"),
    "VariableItemType": ("inttegro.message_template.variable_item_type", "VariableItemType"),
    "VariableType": ("inttegro.message_template.variable_type", "VariableType"),
    "VariablesInput": ("inttegro.message_template.variables_input", "VariablesInput"),
}

__all__ = [
    "AttachmentIDs",
    "AttachmentIDsInput",
    "Channel",
    "CreateEmailRequest",
    "CreateRequest",
    "CreateSMSRequest",
    "EmailContent",
    "EmailContentInput",
    "Envelope",
    "IDRequest",
    "Mailbox",
    "MailboxInput",
    "MessageTemplate",
    "Page",
    "PageEnvelope",
    "PageRequest",
    "Preview",
    "ReferenceInput",
    "RenderPreviewRequest",
    "Rendered",
    "RenderedEmail",
    "RenderedSMS",
    "SMSContent",
    "SMSContentInput",
    "SafetyResult",
    "ScannedLink",
    "Status",
    "UpdateRequest",
    "Variable",
    "VariableInput",
    "VariableItem",
    "VariableItemInput",
    "VariableItemType",
    "VariableType",
    "VariablesInput",
]


def __getattr__(name: str) -> Any:
    """Load a public resource type on first access."""
    try:
        module_name, attribute_name = _EXPORTS[name]
    except KeyError:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}") from None
    value = getattr(import_module(module_name), attribute_name)
    globals()[name] = value
    return value
