"""EmailMessage in the ``inttegro.chime`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class EmailMessage(ApiModel):
    """Email content, safety scan result, and system-generated schema markup for email chimes.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``ChimeEmailMessage``.
    """
    subject: str | None = field(init=False)
    """Email subject. Optional; nullable. Python type: ``str | None``; wire name: ``subject``; JSON type: string"""
    text: str | None = field(init=False)
    """Plain-text email body. Optional; nullable. Python type: ``str | None``; wire name: ``text``; JSON type: string"""
    html: str | None = field(init=False)
    """Optional HTML email body before provider-specific rendering. Optional; nullable. Python type: ``str | None``; wire name: ``html``; JSON type: string"""
    from_: ChimeEmailMailbox | None = field(init=False, metadata={"wire_name": 'from'})
    """The from associated with this email message. Optional; nullable. Python type: ``ChimeEmailMailbox | None``; wire name: ``from_``; JSON type: object"""
    reply_to: ChimeEmailMailbox | None = field(init=False)
    """The reply to associated with this email message. Optional; nullable. Python type: ``ChimeEmailMailbox | None``; wire name: ``reply_to``; JSON type: object (ChimeEmailMailbox)"""
    headers: dict[str, str] | None = field(init=False)
    """Validated provider-neutral email headers. Optional; nullable. Python type: ``dict[str, str] | None``; wire name: ``headers``; JSON type: object (MessageHeaders)"""
    safety: ChimeEmailSafetyResult | None = field(init=False)
    """Result of the email safety scan. Optional; nullable. Python type: ``ChimeEmailSafetyResult | None``; wire name: ``safety``; JSON type: object (ChimeEmailSafetyResult)"""
    schema: ChimeEmailSchemaMarkup | None = field(init=False)
    """Schema.org JSON-LD markup generated at email send time. Optional; nullable. Python type: ``ChimeEmailSchemaMarkup | None``; wire name: ``schema``; JSON type: object (ChimeEmailSchemaMarkup)"""

from inttegro.chime.email_mailbox import EmailMailbox as ChimeEmailMailbox
from inttegro.chime.email_safety_result import EmailSafetyResult as ChimeEmailSafetyResult
from inttegro.chime.email_schema_markup import EmailSchemaMarkup as ChimeEmailSchemaMarkup
