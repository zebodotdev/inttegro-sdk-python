"""UpdateRequestPaymentMethodData in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class UpdateRequestPaymentMethodData(ApiRequest):
    """Payment instrument details for tokenization.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``UpdateOrderRequestPaymentMethodData``.
    """
    mobile_money: UpdateOrderRequestPaymentMethodDataMobileMoney | UnsetType = field(default=UNSET)
    """Mobile money wallet details (required when type is mobile_money). Optional. Python type: ``UpdateOrderRequestPaymentMethodDataMobileMoney``; wire name: ``mobile_money``; JSON type: object"""
    type: Literal['mobile_money', PaymentMethodType.MOBILE_MONEY]
    """Payment rail type (currently only mobile_money supported). Required. Python type: ``Literal['mobile_money', PaymentMethodType.MOBILE_MONEY]``; wire name: ``type``; JSON type: string. Constraints: allowed values ``mobile_money``"""

from inttegro.payment_method.type import Type as PaymentMethodType
from inttegro.order.update_request_payment_method_data_mobile_money import UpdateRequestPaymentMethodDataMobileMoney as UpdateOrderRequestPaymentMethodDataMobileMoney
