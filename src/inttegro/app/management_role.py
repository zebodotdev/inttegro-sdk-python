"""ManagementRole in the ``inttegro.app`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class ManagementRole(WireEnum):
    """Typed management role data in the app resource namespace.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``AppManagementRole``.
    """
    PARENT = "parent"
    """Wire value ``parent`` (parent)"""
    CHILD = "child"
    """Wire value ``child`` (child)"""
