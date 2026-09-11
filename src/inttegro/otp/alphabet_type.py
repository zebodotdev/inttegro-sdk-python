"""AlphabetType in the ``inttegro.otp`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class AlphabetType(WireEnum):
    """Predefined alphabet type (mutually exclusive with token_alphabet).

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``OTPAlphabetType``.
    """
    NUMERIC = "numeric"
    """Wire value ``numeric`` (numeric) for predefined alphabet type (mutually exclusive with token_alphabet)"""
    ALPHA = "alpha"
    """Wire value ``alpha`` (alpha) for predefined alphabet type (mutually exclusive with token_alphabet)"""
    ALPHANUMERIC = "alphanumeric"
    """Wire value ``alphanumeric`` (alphanumeric) for predefined alphabet type (mutually exclusive with token_alphabet)"""
