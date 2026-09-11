"""Transport in the ``inttegro.chime`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class Transport(WireEnum):
    """Typed transport data in the chime resource namespace.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``ChimeTransport``.
    """
    SMS = "sms"
    """Wire value ``sms`` (sms)"""
    EMAIL = "email"
    """Wire value ``email`` (email)"""
