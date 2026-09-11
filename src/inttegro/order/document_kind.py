"""DocumentKind in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class DocumentKind(WireEnum):
    """Hosted document that was delivered.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``OrderDocumentKind``.
    """
    INVOICE = "invoice"
    """Wire value ``invoice`` (invoice) for hosted document that was delivered"""
    RECEIPT = "receipt"
    """Wire value ``receipt`` (receipt) for hosted document that was delivered"""
