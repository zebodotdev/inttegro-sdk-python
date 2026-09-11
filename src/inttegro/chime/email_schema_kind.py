"""EmailSchemaKind in the ``inttegro.chime`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class EmailSchemaKind(WireEnum):
    """Classification for the generated markup.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``ChimeEmailSchemaKind``.
    """
    GMAIL_VIEW_ACTION = "gmail_view_action"
    """Wire value ``gmail_view_action`` (gmail view action) for classification for the generated markup"""
    SCHEMA_ORG_ORDER = "schema_org_order"
    """Wire value ``schema_org_order`` (schema org order) for classification for the generated markup"""
    SCHEMA_ORG_INVOICE = "schema_org_invoice"
    """Wire value ``schema_org_invoice`` (schema org invoice) for classification for the generated markup"""
