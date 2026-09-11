"""NextAction in the ``inttegro.payment`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class NextAction(ApiModel):
    """Next action required to complete a payment.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PaymentNextAction``.
    """
    type: Literal['confirm_payment', 'execute', 'redirect', 'authorize_payment', 'request_confirmation'] = field(init=False)
    """Type of action required. Required. Python type: ``Literal['confirm_payment', 'execute', 'redirect', 'authorize_payment', 'request_confirmation']``; wire name: ``type``; JSON type: string. Constraints: allowed values ``confirm_payment``, ``execute``, ``redirect``, ``authorize_payment``, ``request_confirmation``"""
    confirm_payment: PaymentNextActionConfirmPayment | None = field(init=False)
    """Details for customer payment confirmation. Optional; nullable. Python type: ``PaymentNextActionConfirmPayment | None``; wire name: ``confirm_payment``; JSON type: object"""
    redirect: PaymentNextActionRedirect | None = field(init=False)
    """Details for redirect action. Optional; nullable. Python type: ``PaymentNextActionRedirect | None``; wire name: ``redirect``; JSON type: object"""
    authorize: PaymentNextActionAuthorize | None = field(init=False)
    """Details for authorization action. Optional; nullable. Python type: ``PaymentNextActionAuthorize | None``; wire name: ``authorize``; JSON type: object"""
    request_confirmation: PaymentNextActionRequestConfirmation | None = field(init=False)
    """Details for requesting a fresh customer confirmation. Optional; nullable. Python type: ``PaymentNextActionRequestConfirmation | None``; wire name: ``request_confirmation``; JSON type: object"""

from inttegro.payment.next_action_authorize import NextActionAuthorize as PaymentNextActionAuthorize
from inttegro.payment.next_action_confirm_payment import NextActionConfirmPayment as PaymentNextActionConfirmPayment
from inttegro.payment.next_action_redirect import NextActionRedirect as PaymentNextActionRedirect
from inttegro.payment.next_action_request_confirmation import NextActionRequestConfirmation as PaymentNextActionRequestConfirmation
