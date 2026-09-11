"""EmailSchemaMarkup in the ``inttegro.chime`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class EmailSchemaMarkup(ApiModel):
    """Schema.org JSON-LD markup generated at email send time.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``ChimeEmailSchemaMarkup``.
    """
    kind: Literal['gmail_view_action', 'schema_org_order', 'schema_org_invoice'] | None = field(init=False)
    """Classification for the generated markup. Optional; nullable. Python type: ``Literal['gmail_view_action', 'schema_org_order', 'schema_org_invoice'] | None``; wire name: ``kind``; JSON type: string. Constraints: allowed values ``gmail_view_action``, ``schema_org_order``, ``schema_org_invoice``"""
    json_ld: dict[str, Any] | None = field(init=False)
    """Deliberately extensible JSON object whose keys and values are defined by the selected integration or resource subtype. Optional; nullable. Python type: ``dict[str, Any] | None``; wire name: ``json_ld``; JSON type: object (JSONData)"""
