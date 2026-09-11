"""TokenType in the ``inttegro.secret_key`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class TokenType(WireEnum):
    """Typed token type data in the secret key resource namespace.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``SecretKeyTokenType``.
    """
    BEARER = "bearer"
    """Wire value ``bearer`` (bearer)"""
