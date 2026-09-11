"""Type in the ``inttegro.bank_account`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class Type(WireEnum):
    """Typed type data in the bank account resource namespace.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``BankAccountType``.
    """
    GHANA_BANK_ACCOUNT = "ghana_bank_account"
    """Wire value ``ghana_bank_account`` (ghana bank account)"""
