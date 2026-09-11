"""Reason in the ``inttegro.refund`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class Reason(WireEnum):
    """Typed reason data in the refund resource namespace.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``RefundReason``.
    """
    REQUESTED_BY_CUSTOMER = "requested_by_customer"
    """Wire value ``requested_by_customer`` (requested by customer)"""
    DUPLICATE = "duplicate"
    """Wire value ``duplicate`` (duplicate)"""
    FRAUDULENT = "fraudulent"
    """Wire value ``fraudulent`` (fraudulent)"""
    ORDER_CANCELED = "order_canceled"
    """Wire value ``order_canceled`` (order canceled)"""
    ITEM_RETURNED = "item_returned"
    """Wire value ``item_returned`` (item returned)"""
    ITEM_DAMAGED = "item_damaged"
    """Wire value ``item_damaged`` (item damaged)"""
    ITEM_NOT_RECEIVED = "item_not_received"
    """Wire value ``item_not_received`` (item not received)"""
    ITEM_NOT_AS_DESCRIBED = "item_not_as_described"
    """Wire value ``item_not_as_described`` (item not as described)"""
    CUSTOM = "custom"
    """Wire value ``custom`` (custom)"""
