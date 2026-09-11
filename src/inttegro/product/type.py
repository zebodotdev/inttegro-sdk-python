"""Type in the ``inttegro.product`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class Type(WireEnum):
    """Product type.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``ProductType``.
    """
    PHYSICAL = "physical"
    """Wire value ``physical`` (physical) for product type"""
    DIGITAL = "digital"
    """Wire value ``digital`` (digital) for product type"""
    SERVICE = "service"
    """Wire value ``service`` (service) for product type"""
    VOUCHER = "voucher"
    """Wire value ``voucher`` (voucher) for product type"""
    CUSTOM = "custom"
    """Wire value ``custom`` (custom) for product type"""
    CAUSE = "cause"
    """Wire value ``cause`` (cause) for product type"""
