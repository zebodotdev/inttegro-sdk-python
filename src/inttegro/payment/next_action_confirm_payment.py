"""NextActionConfirmPayment in the ``inttegro.payment`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class NextActionConfirmPayment(ApiModel):
    """Details for customer payment confirmation.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PaymentNextActionConfirmPayment``.
    """
    expires_at: datetime = field(init=False)
    """When the confirmation request expires. Required. Python type: ``datetime``; wire name: ``expires_at``; JSON type: string (date-time)"""
    scheme: str = field(init=False)
    """Authentication scheme used. Required. Python type: ``str``; wire name: ``scheme``; JSON type: string"""
    request: PaymentNextActionConfirmPaymentRequest | None = field(init=False)
    """Confirmation request details. Optional; nullable. Python type: ``PaymentNextActionConfirmPaymentRequest | None``; wire name: ``request``; JSON type: object"""
    attempt: PaymentNextActionConfirmPaymentAttempt | None = field(init=False)
    """Latest confirmation attempt. Optional; nullable. Python type: ``PaymentNextActionConfirmPaymentAttempt | None``; wire name: ``attempt``; JSON type: object"""
    confirmed: bool = field(init=False)
    """Whether the payment confirmation has completed. Required. Python type: ``bool``; wire name: ``confirmed``; JSON type: boolean"""
    status: str = field(init=False)
    """Confirmation status. Required. Python type: ``str``; wire name: ``status``; JSON type: string"""

from inttegro.payment.next_action_confirm_payment_attempt import NextActionConfirmPaymentAttempt as PaymentNextActionConfirmPaymentAttempt
from inttegro.payment.next_action_confirm_payment_request import NextActionConfirmPaymentRequest as PaymentNextActionConfirmPaymentRequest
