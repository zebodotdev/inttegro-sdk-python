"""ActivityType in the ``inttegro.purchase_intent`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class ActivityType(WireEnum):
    """Typed activity type data in the purchase intent resource namespace.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``PurchaseIntentActivityType``.
    """
    EXPIRED_VIEWED = "expired_viewed"
    """Wire value ``expired_viewed`` (expired viewed)"""
    ORDER_CREATED = "order_created"
    """Wire value ``order_created`` (order created)"""
    PAYMENT_FAILED = "payment_failed"
    """Wire value ``payment_failed`` (payment failed)"""
    PAYMENT_STARTED = "payment_started"
    """Wire value ``payment_started`` (payment started)"""
    VIEWED = "viewed"
    """Wire value ``viewed`` (viewed)"""
