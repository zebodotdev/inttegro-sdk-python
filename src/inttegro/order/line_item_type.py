"""LineItemType in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class LineItemType(WireEnum):
    """Type of line item.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.
    """
    PRODUCT = "product"
    """Wire value ``product`` (product) for type of line item"""
    FEE = "fee"
    """Wire value ``fee`` (fee) for type of line item"""
    SHIPPING = "shipping"
    """Wire value ``shipping`` (shipping) for type of line item"""
