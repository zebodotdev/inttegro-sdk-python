"""ContentSafetyStatus in the ``inttegro.shared`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class ContentSafetyStatus(WireEnum):
    """Safety decision for the email content.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.
    """
    ALLOWED = "allowed"
    """Wire value ``allowed`` (allowed) for safety decision for the email content"""
    REJECTED = "rejected"
    """Wire value ``rejected`` (rejected) for safety decision for the email content"""
    QUARANTINED = "quarantined"
    """Wire value ``quarantined`` (quarantined) for safety decision for the email content"""
