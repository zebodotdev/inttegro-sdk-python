"""RecipientType in the ``inttegro.chime`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class RecipientType(WireEnum):
    """Contact type.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``ChimeRecipientType``.
    """
    PHONE = "phone"
    """Wire value ``phone`` (phone) for contact type"""
    EMAIL = "email"
    """Wire value ``email`` (email) for contact type"""
