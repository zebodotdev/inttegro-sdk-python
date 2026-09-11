"""Type in the ``inttegro.financial_account`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class Type(WireEnum):
    """Typed type data in the financial account resource namespace.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``FinancialAccountType``.
    """
    WALLET = "wallet"
    """Wire value ``wallet`` (wallet)"""
    BANK_ACCOUNT = "bank_account"
    """Wire value ``bank_account`` (bank account)"""
    DOSH_ACCOUNT = "dosh_account"
    """Wire value ``dosh_account`` (dosh account)"""
