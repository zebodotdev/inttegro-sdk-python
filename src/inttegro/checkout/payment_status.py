"""PaymentStatus in the ``inttegro.checkout`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class PaymentStatus(WireEnum):
    """Payment status.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``CheckoutPaymentStatus``.
    """
    REQUIRES_ACTION = "requires_action"
    """Wire value ``requires_action`` (requires action) for payment status"""
    PROCESSING = "processing"
    """Wire value ``processing`` (processing) for payment status"""
    SUCCEEDED = "succeeded"
    """Wire value ``succeeded`` (succeeded) for payment status"""
    FAILED = "failed"
    """Wire value ``failed`` (failed) for payment status"""
    CANCELLED = "cancelled"
    """Wire value ``cancelled`` (cancelled) for payment status"""
