"""Attribute in the ``inttegro.product`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Attribute(ApiModel):
    """Typed attribute data in the product resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``ProductAttribute``.
    """
    name: str = field(init=False)
    """Human-readable name of the attribute. Required. Python type: ``str``; wire name: ``name``; JSON type: string. Constraints: maximum length 100"""
    value: str = field(init=False)
    """The value associated with this attribute. Required. Python type: ``str``; wire name: ``value``; JSON type: string. Constraints: maximum length 500"""
