"""InlineRecipientInputVariant1 in the ``inttegro.chime`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class InlineRecipientInputVariant1(ApiRequest):
    """Parameters accepted by the inline recipient input variant1 operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``ChimeInlineRecipientInputVariant1``.
    """
    name: str | UnsetType = field(default=UNSET)
    """Human-readable name of the inline recipient input variant1. Optional. Python type: ``str``; wire name: ``name``; JSON type: string"""
    phone: ChimeInlineRecipientInputVariant1Phone
    """The phone associated with this inline recipient input variant1. Required. Python type: ``ChimeInlineRecipientInputVariant1Phone``; wire name: ``phone``; JSON type: object"""
    type: Literal['phone', ChimeRecipientType.PHONE]
    """Discriminator identifying the inline recipient input variant1 type. Required. Python type: ``Literal['phone', ChimeRecipientType.PHONE]``; wire name: ``type``; JSON type: string. Constraints: allowed values ``phone``"""

from inttegro.chime.inline_recipient_input_variant1_phone import InlineRecipientInputVariant1Phone as ChimeInlineRecipientInputVariant1Phone
from inttegro.chime.recipient_type import RecipientType as ChimeRecipientType
