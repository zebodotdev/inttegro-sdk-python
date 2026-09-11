"""EmbeddedProductAttributesItem in the ``inttegro.price`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class EmbeddedProductAttributesItem(ApiModel):
    """Typed embedded product attributes item data in the price resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PriceEmbeddedProductAttributesItem``.
    """
    name: str = field(init=False)
    """Attribute name. Required. Python type: ``str``; wire name: ``name``; JSON type: string"""
    value: str = field(init=False)
    """Attribute value. Required. Python type: ``str``; wire name: ``value``; JSON type: string"""
