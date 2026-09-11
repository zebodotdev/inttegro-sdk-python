"""NextActionRequestConfirmation in the ``inttegro.payment`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class NextActionRequestConfirmation(ApiModel):
    """Details for requesting a fresh customer confirmation.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PaymentNextActionRequestConfirmation``.
    """
    last_request: PaymentNextActionConfirmPaymentRequest | None = field(init=False)
    """The last request associated with this next action request confirmation. Optional; nullable. Python type: ``PaymentNextActionConfirmPaymentRequest | None``; wire name: ``last_request``; JSON type: object"""
    after: datetime | None = field(init=False)
    """Timestamp for after. Optional; nullable. Python type: ``datetime | None``; wire name: ``after``; JSON type: string (date-time)"""

from inttegro.payment.next_action_confirm_payment_request import NextActionConfirmPaymentRequest as PaymentNextActionConfirmPaymentRequest
