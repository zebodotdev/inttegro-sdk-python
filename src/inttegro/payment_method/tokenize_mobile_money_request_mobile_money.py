"""TokenizeMobileMoneyRequestMobileMoney in the ``inttegro.payment_method`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Literal
from inttegro._request_base import ApiRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class TokenizeMobileMoneyRequestMobileMoney(ApiRequest):
    """Parameters accepted by the tokenize mobile money request mobile money operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``TokenizeMobileMoneyPaymentMethodRequestMobileMoney``.
    """
    account_number: str
    """Mobile-money number in a valid local or international phone-number format. Required. Python type: ``str``; wire name: ``account_number``; JSON type: string. Constraints: minimum length 1"""
    network: Literal['airtel', 'mtn', 'telecel', 'vodafone', MobileMoneyNetwork.AIRTEL, MobileMoneyNetwork.MTN, MobileMoneyNetwork.TELECEL, MobileMoneyNetwork.VODAFONE]
    """The network associated with this tokenize mobile money request mobile money. Required. Python type: ``Literal['airtel', 'mtn', 'telecel', 'vodafone', MobileMoneyNetwork.AIRTEL, MobileMoneyNetwork.MTN, MobileMoneyNetwork.TELECEL, MobileMoneyNetwork.VODAFONE]``; wire name: ``network``; JSON type: string. Constraints: allowed values ``airtel``, ``mtn``, ``telecel``, ``vodafone``"""

from inttegro.payment_method.mobile_money_network import MobileMoneyNetwork
