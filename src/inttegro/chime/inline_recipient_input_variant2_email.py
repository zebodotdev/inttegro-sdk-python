"""InlineRecipientInputVariant2Email in the ``inttegro.chime`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass
from inttegro._request_base import ApiRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class InlineRecipientInputVariant2Email(ApiRequest):
    """Parameters accepted by the inline recipient input variant2 email operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``ChimeInlineRecipientInputVariant2Email``.
    """
    address: str
    """The address associated with this inline recipient input variant2 email. Required. Python type: ``str``; wire name: ``address``; JSON type: string (email)"""
