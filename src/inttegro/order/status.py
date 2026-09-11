"""Status in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class Status(WireEnum):
    """Current lifecycle state of the order.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``OrderStatus``.
    """
    PREPARING = "preparing"
    """Wire value ``preparing`` (preparing) for current lifecycle state of the order"""
    REQUIRES_PAYMENT = "requires_payment"
    """Wire value ``requires_payment`` (requires payment) for current lifecycle state of the order"""
    PAID = "paid"
    """Wire value ``paid`` (paid) for current lifecycle state of the order"""
    COMPLETED = "completed"
    """Wire value ``completed`` (completed) for current lifecycle state of the order"""
    CANCELED = "canceled"
    """Wire value ``canceled`` (canceled) for current lifecycle state of the order"""
    EXPIRED = "expired"
    """Wire value ``expired`` (expired) for current lifecycle state of the order"""
    UNKNOWN = "unknown"
    """Wire value ``unknown`` (unknown) for current lifecycle state of the order"""
