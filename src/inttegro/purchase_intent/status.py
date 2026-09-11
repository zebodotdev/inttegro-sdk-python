"""Status in the ``inttegro.purchase_intent`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class Status(WireEnum):
    """Effective lifecycle state derived from expiry, cancellation, and single-use order creation.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``PurchaseIntentStatus``.
    """
    ACTIVE = "active"
    """Wire value ``active`` (active) for effective lifecycle state derived from expiry, cancellation, and single-use order creation"""
    EXPIRED = "expired"
    """Wire value ``expired`` (expired) for effective lifecycle state derived from expiry, cancellation, and single-use order creation"""
    INACTIVE = "inactive"
    """Wire value ``inactive`` (inactive) for effective lifecycle state derived from expiry, cancellation, and single-use order creation"""
    USED = "used"
    """Wire value ``used`` (used) for effective lifecycle state derived from expiry, cancellation, and single-use order creation"""
