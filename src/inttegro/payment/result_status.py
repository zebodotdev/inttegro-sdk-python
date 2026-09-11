"""ResultStatus in the ``inttegro.payment`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class ResultStatus(WireEnum):
    """Payment status.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``PaymentResultStatus``.
    """
    PENDING = "pending"
    """Wire value ``pending`` (pending) for payment status"""
    REQUIRES_CONFIRMATION = "requires_confirmation"
    """Wire value ``requires_confirmation`` (requires confirmation) for payment status"""
    PROCESSING = "processing"
    """Wire value ``processing`` (processing) for payment status"""
    SUCCEEDED = "succeeded"
    """Wire value ``succeeded`` (succeeded) for payment status"""
    FAILED = "failed"
    """Wire value ``failed`` (failed) for payment status"""
