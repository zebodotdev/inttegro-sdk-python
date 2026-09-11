"""AuthResult in the ``inttegro.secret_key`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class AuthResult(WireEnum):
    """Typed auth result data in the secret key resource namespace.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``SecretKeyAuthResult``.
    """
    SUCCEEDED = "succeeded"
    """Wire value ``succeeded`` (succeeded)"""
    FAILED = "failed"
    """Wire value ``failed`` (failed)"""
