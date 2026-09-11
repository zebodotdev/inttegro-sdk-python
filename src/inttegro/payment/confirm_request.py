"""ConfirmRequest in the ``inttegro.payment`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass
from inttegro._request_base import ApiRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class ConfirmRequest(ApiRequest):
    """Parameters accepted by the confirm request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``ConfirmPaymentRequest``.
    """
    order_id: str
    """Identifier of the related order. Required. Python type: ``str``; wire name: ``order_id``; JSON type: string. Constraints: minimum length 1"""
    payment_id: str
    """Optional payment identifier when already known by the client. Required. Python type: ``str``; wire name: ``payment_id``; JSON type: string"""
    confirmation_id: str
    """Optional confirmation attempt identifier. Required. Python type: ``str``; wire name: ``confirmation_id``; JSON type: string"""
    token: str
    """Payer confirmation token. Required. Python type: ``str``; wire name: ``token``; JSON type: string. Constraints: minimum length 1"""
