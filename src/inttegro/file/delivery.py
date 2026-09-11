"""Delivery in the ``inttegro.file`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class Delivery(WireEnum):
    """Typed delivery data in the file resource namespace.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``FileDelivery``.
    """
    STREAM = "stream"
    """Wire value ``stream`` (stream)"""
    REDIRECT = "redirect"
    """Wire value ``redirect`` (redirect)"""
