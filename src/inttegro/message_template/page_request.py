"""PageRequest in the ``inttegro.message_template`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class PageRequest(ApiRequest):
    """Parameters accepted by the page request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``PageMessageTemplatesRequest``.
    """
    page: int | UnsetType = field(default=UNSET)
    """Numeric page used by this operation. Optional. Python type: ``int``; wire name: ``page``; JSON type: integer. Constraints: minimum 1"""
    size: int | UnsetType = field(default=UNSET)
    """Numeric size used by this operation. Optional. Python type: ``int``; wire name: ``size``; JSON type: integer. Constraints: minimum 1"""
    status: Literal['draft', 'published', 'archived', MessageTemplateStatus.DRAFT, MessageTemplateStatus.PUBLISHED, MessageTemplateStatus.ARCHIVED] | UnsetType = field(default=UNSET)
    """Current lifecycle status of the page request. Optional. Python type: ``Literal['draft', 'published', 'archived', MessageTemplateStatus.DRAFT, MessageTemplateStatus.PUBLISHED, MessageTemplateStatus.ARCHIVED]``; wire name: ``status``; JSON type: string. Constraints: allowed values ``draft``, ``published``, ``archived``"""
    channel: Literal['sms', 'email', MessageTemplateChannel.SMS, MessageTemplateChannel.EMAIL] | UnsetType = field(default=UNSET)
    """The channel associated with this page request. Optional. Python type: ``Literal['sms', 'email', MessageTemplateChannel.SMS, MessageTemplateChannel.EMAIL]``; wire name: ``channel``; JSON type: string. Constraints: allowed values ``sms``, ``email``"""
    purpose: str | UnsetType = field(default=UNSET)
    """The purpose associated with this page request. Optional. Python type: ``str``; wire name: ``purpose``; JSON type: string"""
    locale: str | UnsetType = field(default=UNSET)
    """The locale associated with this page request. Optional. Python type: ``str``; wire name: ``locale``; JSON type: string"""

from inttegro.message_template.channel import Channel as MessageTemplateChannel
from inttegro.message_template.status import Status as MessageTemplateStatus
