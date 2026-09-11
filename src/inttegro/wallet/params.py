"""Params in the ``inttegro.wallet`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Literal
from inttegro._request_base import ApiRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class Params(ApiRequest):
    """Parameters accepted by the params operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``FinancialAccountWalletRequestWallet``.
    """
    type: Literal['mobile_money', WalletType.MOBILE_MONEY]
    """Discriminator identifying the param type. Required. Python type: ``Literal['mobile_money', WalletType.MOBILE_MONEY]``; wire name: ``type``; JSON type: string. Constraints: allowed values ``mobile_money``"""
    mobile_money: FinancialAccountWalletRequestWalletMobileMoney
    """The mobile money associated with this param. Required. Python type: ``FinancialAccountWalletRequestWalletMobileMoney``; wire name: ``mobile_money``; JSON type: object"""

from inttegro.wallet.mobile_money_params import MobileMoneyParams as FinancialAccountWalletRequestWalletMobileMoney
from inttegro.wallet.type import Type as WalletType
