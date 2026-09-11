"""VariantAxis in the ``inttegro.purchase_intent`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class VariantAxis(ApiModel):
    """Typed variant axis data in the purchase intent resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PurchaseIntentVariantAxis``.
    """
    key: str = field(init=False)
    """The key associated with this variant axi. Required. Python type: ``str``; wire name: ``key``; JSON type: string"""
    label: str = field(init=False)
    """The label associated with this variant axi. Required. Python type: ``str``; wire name: ``label``; JSON type: string"""
    position: int = field(init=False)
    """The position associated with this variant axi. Required. Python type: ``int``; wire name: ``position``; JSON type: integer"""
