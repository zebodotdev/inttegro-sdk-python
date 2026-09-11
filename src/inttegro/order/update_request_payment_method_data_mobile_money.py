"""UpdateRequestPaymentMethodDataMobileMoney in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Literal
from inttegro._request_base import ApiRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class UpdateRequestPaymentMethodDataMobileMoney(ApiRequest):
    """Mobile money wallet details (required when type is mobile_money).

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``UpdateOrderRequestPaymentMethodDataMobileMoney``.
    """
    network: Literal['airtel', 'mtn', 'telecel', 'vodafone', MobileMoneyNetwork.AIRTEL, MobileMoneyNetwork.MTN, MobileMoneyNetwork.TELECEL, MobileMoneyNetwork.VODAFONE]
    """Mobile money network provider. Required. Python type: ``Literal['airtel', 'mtn', 'telecel', 'vodafone', MobileMoneyNetwork.AIRTEL, MobileMoneyNetwork.MTN, MobileMoneyNetwork.TELECEL, MobileMoneyNetwork.VODAFONE]``; wire name: ``network``; JSON type: string. Constraints: allowed values ``airtel``, ``mtn``, ``telecel``, ``vodafone``"""
    account_number: str
    """Mobile money account number (international or local format). Required. Python type: ``str``; wire name: ``account_number``; JSON type: string. The value must contain 10 to 15 digits and may begin with ``+``."""

from inttegro.payment_method.mobile_money_network import MobileMoneyNetwork
