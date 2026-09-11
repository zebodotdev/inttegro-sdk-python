"""RenderedEmail in the ``inttegro.message_template`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class RenderedEmail(ApiModel):
    """Typed rendered email data in the message template resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``RenderedEmailMessageTemplate``.
    """
    subject: str = field(init=False)
    """The subject associated with this rendered email. Required. Python type: ``str``; wire name: ``subject``; JSON type: string"""
    text: str = field(init=False)
    """The text associated with this rendered email. Required. Python type: ``str``; wire name: ``text``; JSON type: string"""
    html: str | None = field(init=False)
    """The html associated with this rendered email. Optional; nullable. Python type: ``str | None``; wire name: ``html``; JSON type: string"""
    from_: MessageTemplateMailbox | None = field(init=False, metadata={"wire_name": 'from'})
    """The from associated with this rendered email. Optional; nullable. Python type: ``MessageTemplateMailbox | None``; wire name: ``from_``; JSON type: object"""
    reply_to: MessageTemplateMailbox | None = field(init=False)
    """The reply to associated with this rendered email. Optional; nullable. Python type: ``MessageTemplateMailbox | None``; wire name: ``reply_to``; JSON type: object (MessageTemplateMailbox)"""
    headers: dict[str, str] | None = field(init=False)
    """Validated provider-neutral email headers. Optional; nullable. Python type: ``dict[str, str] | None``; wire name: ``headers``; JSON type: object (MessageHeaders)"""
    safety: MessageTemplateSafetyResult | None = field(init=False)
    """Result of the email safety scan. Optional; nullable. Python type: ``MessageTemplateSafetyResult | None``; wire name: ``safety``; JSON type: object (MessageTemplateSafetyResult)"""

from inttegro.message_template.mailbox import Mailbox as MessageTemplateMailbox
from inttegro.message_template.safety_result import SafetyResult as MessageTemplateSafetyResult
