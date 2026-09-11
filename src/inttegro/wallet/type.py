"""Type in the ``inttegro.wallet`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class Type(WireEnum):
    """Typed type data in the wallet resource namespace.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``WalletType``.
    """
    MOBILE_MONEY = "mobile_money"
    """Wire value ``mobile_money`` (mobile money)"""
