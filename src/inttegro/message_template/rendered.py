"""Rendered in the ``inttegro.message_template`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Rendered(ApiModel):
    """Typed rendered data in the message template resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``RenderedMessageTemplate``.
    """
    channel: Literal['sms', 'email'] = field(init=False)
    """The channel associated with this rendered. Required. Python type: ``Literal['sms', 'email']``; wire name: ``channel``; JSON type: string. Constraints: allowed values ``sms``, ``email``"""
    attachments: MessageTemplateAttachmentIDs | None = field(init=False)
    """Stored file IDs returned by previews. Chime send, schedule, and broadcast currently reject stored-template attachments. Optional; nullable. Python type: ``MessageTemplateAttachmentIDs | None``; wire name: ``attachments``; JSON type: object (MessageTemplateAttachmentIDs)"""
    sms: RenderedSMSMessageTemplate | None = field(init=False)
    """The sms associated with this rendered. Optional; nullable. Python type: ``RenderedSMSMessageTemplate | None``; wire name: ``sms``; JSON type: object (RenderedSMSMessageTemplate)"""
    email: RenderedEmailMessageTemplate | None = field(init=False)
    """The email associated with this rendered. Optional; nullable. Python type: ``RenderedEmailMessageTemplate | None``; wire name: ``email``; JSON type: object (RenderedEmailMessageTemplate)"""

from inttegro.message_template.attachment_ids import AttachmentIDs as MessageTemplateAttachmentIDs
from inttegro.message_template.rendered_email import RenderedEmail as RenderedEmailMessageTemplate
from inttegro.message_template.rendered_sms import RenderedSMS as RenderedSMSMessageTemplate
