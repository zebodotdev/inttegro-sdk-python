"""NextActionConfirmPaymentRequest in the ``inttegro.payment`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class NextActionConfirmPaymentRequest(ApiModel):
    """Confirmation request details.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PaymentNextActionConfirmPaymentRequest``.
    """
    id: str = field(init=False)
    """Unique identifier for the confirmation request. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    recipient: str = field(init=False)
    """Recipient of the confirmation token. Required. Python type: ``str``; wire name: ``recipient``; JSON type: string"""
    sent_via: Literal['sms', 'email', 'push'] = field(init=False)
    """Channel used to send the token. Required. Python type: ``Literal['sms', 'email', 'push']``; wire name: ``sent_via``; JSON type: string. Constraints: allowed values ``sms``, ``email``, ``push``"""
    token_size: int = field(init=False)
    """Number of digits in the token. Required. Python type: ``int``; wire name: ``token_size``; JSON type: integer"""
    sender_id: str = field(init=False)
    """Sender ID for the message. Required. Python type: ``str``; wire name: ``sender_id``; JSON type: string"""
    status: str | None = field(init=False)
    """Current request status. Optional; nullable. Python type: ``str | None``; wire name: ``status``; JSON type: string"""
