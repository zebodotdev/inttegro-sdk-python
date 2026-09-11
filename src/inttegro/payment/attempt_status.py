"""AttemptStatus in the ``inttegro.payment`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class AttemptStatus(WireEnum):
    """Typed attempt status data in the payment resource namespace.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``PaymentAttemptStatus``.
    """
    INITIATED = "initiated"
    """Wire value ``initiated`` (initiated)"""
    EXECUTED = "executed"
    """Wire value ``executed`` (executed)"""
    SUCCEEDED = "succeeded"
    """Wire value ``succeeded`` (succeeded)"""
    CANCELED = "canceled"
    """Wire value ``canceled`` (canceled)"""
    EXPIRED = "expired"
    """Wire value ``expired`` (expired)"""
    FAILED = "failed"
    """Wire value ``failed`` (failed)"""
    UNKNOWN = "unknown"
    """Wire value ``unknown`` (unknown)"""
