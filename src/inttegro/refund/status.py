"""Status in the ``inttegro.refund`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class Status(WireEnum):
    """Typed status data in the refund resource namespace.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``RefundStatus``.
    """
    CANCELED = "canceled"
    """Wire value ``canceled`` (canceled)"""
    FAILED = "failed"
    """Wire value ``failed`` (failed)"""
    PENDING = "pending"
    """Wire value ``pending`` (pending)"""
    PROCESSING = "processing"
    """Wire value ``processing`` (processing)"""
    SUCCEEDED = "succeeded"
    """Wire value ``succeeded`` (succeeded)"""
