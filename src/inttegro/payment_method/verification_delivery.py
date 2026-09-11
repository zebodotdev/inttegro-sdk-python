"""VerificationDelivery in the ``inttegro.payment_method`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class VerificationDelivery(ApiModel):
    """Confirmation request details.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PaymentMethodVerificationDelivery``.
    """
    recipient: str | None = field(init=False)
    """Recipient of the confirmation token. Required; nullable. Python type: ``str | None``; wire name: ``recipient``; JSON type: string"""
    channel: str | None = field(init=False)
    """The channel associated with this verification delivery. Optional; nullable. Python type: ``str | None``; wire name: ``channel``; JSON type: string"""
    sender_id: str | None = field(init=False)
    """Sender ID for the message. Required; nullable. Python type: ``str | None``; wire name: ``sender_id``; JSON type: string"""
