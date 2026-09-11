"""ShipmentInputType in the ``inttegro.product`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class ShipmentInputType(WireEnum):
    """Typed shipment input type data in the product resource namespace.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``ProductShipmentInputType``.
    """
    DELIVERY = "delivery"
    """Wire value ``delivery`` (delivery)"""
    DOWNLOAD = "download"
    """Wire value ``download`` (download)"""
    RENDER = "render"
    """Wire value ``render`` (render)"""
    STREAM = "stream"
    """Wire value ``stream`` (stream)"""
