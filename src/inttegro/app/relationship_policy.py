"""RelationshipPolicy in the ``inttegro.app`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class RelationshipPolicy(ApiModel):
    """Typed relationship policy data in the app resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``ApplicationRelationshipPolicy``.
    """
    child_standing: str = field(init=False)
    """The child standing associated with this relationship policy. Required. Python type: ``str``; wire name: ``child_standing``; JSON type: string"""
    management: Literal['parent', 'child'] = field(init=False)
    """The management associated with this relationship policy. Required. Python type: ``Literal['parent', 'child']``; wire name: ``management``; JSON type: string"""
    credentials: Literal['child', 'parent'] = field(init=False)
    """The credentials associated with this relationship policy. Required. Python type: ``Literal['child', 'parent']``; wire name: ``credentials``; JSON type: string"""
