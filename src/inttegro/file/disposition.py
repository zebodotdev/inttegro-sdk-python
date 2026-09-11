"""Disposition in the ``inttegro.file`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class Disposition(WireEnum):
    """Typed disposition data in the file resource namespace.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``FileDisposition``.
    """
    ATTACHMENT = "attachment"
    """Wire value ``attachment`` (attachment)"""
    INLINE = "inline"
    """Wire value ``inline`` (inline)"""
