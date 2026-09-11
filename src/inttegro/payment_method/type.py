"""Type in the ``inttegro.payment_method`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class Type(WireEnum):
    """Payment method type.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``PaymentMethodType``.
    """
    MOBILE_MONEY = "mobile_money"
    """Wire value ``mobile_money`` (mobile money) for payment method type"""
    BANK_ACCOUNT = "bank_account"
    """Wire value ``bank_account`` (bank account) for payment method type"""
    CARD = "card"
    """Wire value ``card`` (card) for payment method type"""
    MOTITO = "motito"
    """Wire value ``motito`` (motito) for payment method type"""
