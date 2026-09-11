"""Models, requests, and enums for the Inttegro message template resource.

The primary returned object is ``inttegro.message_template.MessageTemplate``. Related request types, nested response shapes, and string-backed enums are exported from this singular namespace. Public members load lazily, so importing one resource does not eagerly import the entire SDK."""

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
