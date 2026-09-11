"""InlineRecipientInputVariant2 in the ``inttegro.chime`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class InlineRecipientInputVariant2(ApiRequest):
    """Parameters accepted by the inline recipient input variant2 operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``ChimeInlineRecipientInputVariant2``.
    """
    name: str | UnsetType = field(default=UNSET)
    """Human-readable name of the inline recipient input variant2. Optional. Python type: ``str``; wire name: ``name``; JSON type: string"""
    email: ChimeInlineRecipientInputVariant2Email
    """The email associated with this inline recipient input variant2. Required. Python type: ``ChimeInlineRecipientInputVariant2Email``; wire name: ``email``; JSON type: object"""
    type: Literal['email', ChimeRecipientType.EMAIL]
    """Discriminator identifying the inline recipient input variant2 type. Required. Python type: ``Literal['email', ChimeRecipientType.EMAIL]``; wire name: ``type``; JSON type: string. Constraints: allowed values ``email``"""

from inttegro.chime.inline_recipient_input_variant2_email import InlineRecipientInputVariant2Email as ChimeInlineRecipientInputVariant2Email
from inttegro.chime.recipient_type import RecipientType as ChimeRecipientType
