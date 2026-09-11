"""PayRequest in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class PayRequest(ApiRequest):
    """Parameters accepted by the pay request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``PayOrderRequest``.
    """
    payment_method_data: PaymentMethodDataInput | UnsetType = field(default=UNSET)
    """New payment method details supplied by the payer. Mutually exclusive with `payment_method_id`. Shipping details are not accepted here because checkout cannot change the Order's shipping address. Optional. Python type: ``PaymentMethodDataInput``; wire name: ``payment_method_data``; JSON type: object"""
    payment_method_id: str | UnsetType = field(default=UNSET)
    """A saved payment method owned by the Order's immutable customer. Mutually exclusive with `payment_method_data`. Optional. Python type: ``str``; wire name: ``payment_method_id``; JSON type: string. Constraints: minimum length 1"""
    paid_out_of_band: bool | UnsetType = field(default=UNSET)
    """Whether paid out of band. Optional. Python type: ``bool``; wire name: ``paid_out_of_band``; JSON type: boolean"""
    order_id: str
    """The finalized Order to pay. Required. Python type: ``str``; wire name: ``order_id``; JSON type: string. Constraints: minimum length 1"""

from inttegro.payment_method.data_input import DataInput as PaymentMethodDataInput
