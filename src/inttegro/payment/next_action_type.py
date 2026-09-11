"""NextActionType in the ``inttegro.payment`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class NextActionType(WireEnum):
    """Typed next action type data in the payment resource namespace.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``PaymentNextActionType``.
    """
    CONFIRM_PAYMENT = "confirm_payment"
    """Wire value ``confirm_payment`` (confirm payment)"""
    EXECUTE = "execute"
    """Wire value ``execute`` (execute)"""
    REDIRECT = "redirect"
    """Wire value ``redirect`` (redirect)"""
    AUTHORIZE = "authorize"
    """Wire value ``authorize`` (authorize)"""
    NONE = "none"
    """Wire value ``none`` (none)"""
