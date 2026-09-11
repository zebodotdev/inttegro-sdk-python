"""EmailContentInput in the ``inttegro.message_template`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class EmailContentInput(ApiRequest):
    """Parameters accepted by the email content input operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``MessageTemplateEmailContentInput``.
    """
    from_: MessageTemplateMailboxInput | UnsetType = field(default=UNSET, metadata={'wire_name': 'from'})
    """The from associated with this email content input. Optional. Python type: ``MessageTemplateMailboxInput``; wire name: ``from_``; JSON type: object"""
    reply_to: MessageTemplateMailboxInput | UnsetType = field(default=UNSET)
    """The reply to associated with this email content input. Optional. Python type: ``MessageTemplateMailboxInput``; wire name: ``reply_to``; JSON type: object (MessageTemplateMailbox)"""
    headers: dict[str, str] | UnsetType = field(default=UNSET)
    """Validated provider-neutral email headers. Optional. Python type: ``dict[str, str]``; wire name: ``headers``; JSON type: object (MessageHeaders)"""
    subject: str
    """Email subject template. Required. Python type: ``str``; wire name: ``subject``; JSON type: string"""
    html: str
    """HTML email body template. Required. Python type: ``str``; wire name: ``html``; JSON type: string"""

from inttegro.message_template.mailbox_input import MailboxInput as MessageTemplateMailboxInput
