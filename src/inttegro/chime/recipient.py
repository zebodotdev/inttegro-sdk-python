"""Recipient in the ``inttegro.chime`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Recipient(ApiModel):
    """Typed recipient data in the chime resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``ChimeRecipient``.
    """
    type: Literal['phone', 'email'] = field(init=False)
    """Discriminator identifying the recipient type. Required. Python type: ``Literal['phone', 'email']``; wire name: ``type``; JSON type: string"""
    name: str | None = field(init=False)
    """Human-readable name of the recipient. Optional; nullable. Python type: ``str | None``; wire name: ``name``; JSON type: string"""
    phone: ChimeRecipientPhone | None = field(init=False)
    """The phone associated with this recipient. Optional; nullable. Python type: ``ChimeRecipientPhone | None``; wire name: ``phone``; JSON type: object"""
    email: ChimeRecipientEmail | None = field(init=False)
    """The email associated with this recipient. Optional; nullable. Python type: ``ChimeRecipientEmail | None``; wire name: ``email``; JSON type: object"""

from inttegro.chime.recipient_email import RecipientEmail as ChimeRecipientEmail
from inttegro.chime.recipient_phone import RecipientPhone as ChimeRecipientPhone
