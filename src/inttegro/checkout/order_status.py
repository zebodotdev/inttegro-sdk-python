"""OrderStatus in the ``inttegro.checkout`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class OrderStatus(WireEnum):
    """Current status of the order.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``CheckoutOrderStatus``.
    """
    PREPARING = "preparing"
    """Wire value ``preparing`` (preparing) for current status of the order"""
    REQUIRES_PAYMENT = "requires_payment"
    """Wire value ``requires_payment`` (requires payment) for current status of the order"""
    COMPLETED = "completed"
    """Wire value ``completed`` (completed) for current status of the order"""
    CANCELED = "canceled"
    """Wire value ``canceled`` (canceled) for current status of the order"""
    EXPIRED = "expired"
    """Wire value ``expired`` (expired) for current status of the order"""
