"""CredentialOwner in the ``inttegro.app`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class CredentialOwner(WireEnum):
    """Typed credential owner data in the app resource namespace.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``AppCredentialOwner``.
    """
    CHILD = "child"
    """Wire value ``child`` (child)"""
    PARENT = "parent"
    """Wire value ``parent`` (parent)"""
