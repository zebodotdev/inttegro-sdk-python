"""Status in the ``inttegro.payment`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class Status(WireEnum):
    """Payment state.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``PaymentStatus``.
    """
    INITIATED = "initiated"
    """Wire value ``initiated`` (initiated) for payment state"""
    REQUIRES_ACTION = "requires_action"
    """Wire value ``requires_action`` (requires action) for payment state"""
    OVERDUE = "overdue"
    """Wire value ``overdue`` (overdue) for payment state"""
    EXECUTED = "executed"
    """Wire value ``executed`` (executed) for payment state"""
    PAID = "paid"
    """Wire value ``paid`` (paid) for payment state"""
    CANCELED = "canceled"
    """Wire value ``canceled`` (canceled) for payment state"""
    EXPIRED = "expired"
    """Wire value ``expired`` (expired) for payment state"""
    FAILED = "failed"
    """Wire value ``failed`` (failed) for payment state"""
    UNKNOWN = "unknown"
    """Wire value ``unknown`` (unknown) for payment state"""
