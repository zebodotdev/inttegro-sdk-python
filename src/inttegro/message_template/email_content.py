"""EmailContent in the ``inttegro.message_template`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class EmailContent(ApiModel):
    """Typed email content data in the message template resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``MessageTemplateEmailContent``.
    """
    subject: str = field(init=False)
    """Email subject template. Required. Python type: ``str``; wire name: ``subject``; JSON type: string"""
    html: str = field(init=False)
    """HTML email body template. Required. Python type: ``str``; wire name: ``html``; JSON type: string"""
    from_: MessageTemplateMailbox | None = field(init=False, metadata={"wire_name": 'from'})
    """The from associated with this email content. Optional; nullable. Python type: ``MessageTemplateMailbox | None``; wire name: ``from_``; JSON type: object"""
    reply_to: MessageTemplateMailbox | None = field(init=False)
    """The reply to associated with this email content. Optional; nullable. Python type: ``MessageTemplateMailbox | None``; wire name: ``reply_to``; JSON type: object (MessageTemplateMailbox)"""
    headers: dict[str, str] | None = field(init=False)
    """Validated provider-neutral email headers. Optional; nullable. Python type: ``dict[str, str] | None``; wire name: ``headers``; JSON type: object (MessageHeaders)"""

from inttegro.message_template.mailbox import Mailbox as MessageTemplateMailbox
