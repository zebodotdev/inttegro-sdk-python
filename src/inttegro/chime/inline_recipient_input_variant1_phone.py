"""InlineRecipientInputVariant1Phone in the ``inttegro.chime`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass
from inttegro._request_base import ApiRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class InlineRecipientInputVariant1Phone(ApiRequest):
    """Parameters accepted by the inline recipient input variant1 phone operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``ChimeInlineRecipientInputVariant1Phone``.
    """
    number: str
    """Human-readable number assigned to the inline recipient input variant1 phone. Required. Python type: ``str``; wire name: ``number``; JSON type: string"""
