"""EmailMessageInput in the ``inttegro.chime`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class EmailMessageInput(ApiRequest):
    """Email content accepted for email chimes, broadcasts, and schedules.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``ChimeEmailMessageInput``.
    """
    html: str | UnsetType = field(default=UNSET)
    """Optional HTML email body. Unsafe HTML is rejected or sanitized before delivery. Optional. Python type: ``str``; wire name: ``html``; JSON type: string"""
    reply_to: str | UnsetType = field(default=UNSET)
    """Optional reply-to email address. Optional. Python type: ``str``; wire name: ``reply_to``; JSON type: string (email)"""
    headers: dict[str, str] | UnsetType = field(default=UNSET)
    """Validated provider-neutral email headers. Optional. Python type: ``dict[str, str]``; wire name: ``headers``; JSON type: object (MessageHeaders)"""
    subject: str
    """Email subject. Required. Python type: ``str``; wire name: ``subject``; JSON type: string"""
    text: str
    """Plain-text email body. Required. Python type: ``str``; wire name: ``text``; JSON type: string"""
    from_: ChimeEmailMailboxInput = field(metadata={'wire_name': 'from'})
    """The from associated with this email message input. Required. Python type: ``ChimeEmailMailboxInput``; wire name: ``from_``; JSON type: object"""

from inttegro.chime.email_mailbox_input import EmailMailboxInput as ChimeEmailMailboxInput
