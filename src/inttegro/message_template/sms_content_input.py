"""SMSContentInput in the ``inttegro.message_template`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass
from inttegro._request_base import ApiRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class SMSContentInput(ApiRequest):
    """Parameters accepted by the smscontent input operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``MessageTemplateSMSContentInput``.
    """
    message_template: str
    """SMS body template. Required. Python type: ``str``; wire name: ``message_template``; JSON type: string"""
