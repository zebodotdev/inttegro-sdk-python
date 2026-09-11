"""MessageTemplate in the ``inttegro.message_template`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class MessageTemplate(ApiModel):
    """Typed message template data in the message template resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.
    """
    id: str = field(init=False)
    """API-generated unique template id. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    name: str = field(init=False)
    """Human-readable name of the message template. Required. Python type: ``str``; wire name: ``name``; JSON type: string"""
    about: str | None = field(init=False)
    """The about associated with this message template. Optional; nullable. Python type: ``str | None``; wire name: ``about``; JSON type: string"""
    channel: Literal['sms', 'email'] = field(init=False)
    """The channel associated with this message template. Required. Python type: ``Literal['sms', 'email']``; wire name: ``channel``; JSON type: string. Constraints: allowed values ``sms``, ``email``"""
    purpose: str = field(init=False)
    """The purpose associated with this message template. Required. Python type: ``str``; wire name: ``purpose``; JSON type: string"""
    locale: str = field(init=False)
    """The locale associated with this message template. Required. Python type: ``str``; wire name: ``locale``; JSON type: string"""
    status: Literal['draft', 'published', 'archived'] = field(init=False)
    """Current lifecycle status of the message template. Required. Python type: ``Literal['draft', 'published', 'archived']``; wire name: ``status``; JSON type: string. Constraints: allowed values ``draft``, ``published``, ``archived``"""
    version: int = field(init=False)
    """The version associated with this message template. Required. Python type: ``int``; wire name: ``version``; JSON type: integer"""
    published_version: int | None = field(init=False)
    """The published version associated with this message template. Optional; nullable. Python type: ``int | None``; wire name: ``published_version``; JSON type: integer"""
    draft_version: int = field(init=False)
    """The draft version associated with this message template. Required. Python type: ``int``; wire name: ``draft_version``; JSON type: integer"""
    has_unpublished_changes: bool = field(init=False)
    """Whether has unpublished changes. Required. Python type: ``bool``; wire name: ``has_unpublished_changes``; JSON type: boolean"""
    variables: list[MessageTemplateVariable] | None = field(init=False)
    """The variables associated with this message template. Optional; nullable. Python type: ``list[MessageTemplateVariable] | None``; wire name: ``variables``; JSON type: array of object (MessageTemplateVariable) values"""
    sms: MessageTemplateSMSContent | None = field(init=False)
    """The sms associated with this message template. Optional; nullable. Python type: ``MessageTemplateSMSContent | None``; wire name: ``sms``; JSON type: object (MessageTemplateSMSContent)"""
    email: MessageTemplateEmailContent | None = field(init=False)
    """The email associated with this message template. Optional; nullable. Python type: ``MessageTemplateEmailContent | None``; wire name: ``email``; JSON type: object (MessageTemplateEmailContent)"""
    attachments: MessageTemplateAttachmentIDs | None = field(init=False)
    """Stored file IDs returned by previews. Chime send, schedule, and broadcast currently reject stored-template attachments. Optional; nullable. Python type: ``MessageTemplateAttachmentIDs | None``; wire name: ``attachments``; JSON type: object (MessageTemplateAttachmentIDs)"""
    created_at: datetime = field(init=False)
    """When the message template was created. Required. Python type: ``datetime``; wire name: ``created_at``; JSON type: string (date-time)"""
    updated_at: datetime = field(init=False)
    """When the message template was last updated. Required. Python type: ``datetime``; wire name: ``updated_at``; JSON type: string (date-time)"""
    published_at: datetime | None = field(init=False)
    """When the message template was first published. Optional; nullable. Python type: ``datetime | None``; wire name: ``published_at``; JSON type: string (date-time)"""
    archived_at: datetime | None = field(init=False)
    """When the message template was archived. Optional; nullable. Python type: ``datetime | None``; wire name: ``archived_at``; JSON type: string (date-time)"""

from inttegro.message_template.attachment_ids import AttachmentIDs as MessageTemplateAttachmentIDs
from inttegro.message_template.email_content import EmailContent as MessageTemplateEmailContent
from inttegro.message_template.sms_content import SMSContent as MessageTemplateSMSContent
from inttegro.message_template.variable import Variable as MessageTemplateVariable
