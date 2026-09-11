"""Relationship in the ``inttegro.app`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Relationship(ApiModel):
    """Typed relationship data in the app resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``ApplicationRelationship``.
    """
    id: str = field(init=False)
    """Order that consumed the Buy link. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    kind: Literal['placement'] = field(init=False)
    """The kind associated with this relationship. Optional. Python type: ``Literal['placement']``; wire name: ``kind``; JSON type: string"""
    policy_version: str = field(init=False)
    """The policy version associated with this relationship. Optional. Python type: ``str``; wire name: ``policy_version``; JSON type: string"""
    status: Literal['active', 'inactive', 'suspended', 'revoked'] = field(init=False)
    """Current lifecycle status of the relationship. Optional. Python type: ``Literal['active', 'inactive', 'suspended', 'revoked']``; wire name: ``status``; JSON type: string"""
    actor_app_id: str = field(init=False)
    """Identifier of the related actor app. Optional. Python type: ``str``; wire name: ``actor_app_id``; JSON type: string"""
    creator_app_id: str = field(init=False)
    """Identifier of the related creator app. Optional. Python type: ``str``; wire name: ``creator_app_id``; JSON type: string"""
    placement_parent_app_id: str = field(init=False)
    """Identifier of the related placement parent app. Optional. Python type: ``str``; wire name: ``placement_parent_app_id``; JSON type: string"""
    subject_app_id: str = field(init=False)
    """Identifier of the related subject app. Optional. Python type: ``str``; wire name: ``subject_app_id``; JSON type: string"""
    child_app_id: str = field(init=False)
    """Identifier of the related child app. Optional. Python type: ``str``; wire name: ``child_app_id``; JSON type: string"""
    child_standing: str = field(init=False)
    """The child standing associated with this relationship. Optional. Python type: ``str``; wire name: ``child_standing``; JSON type: string"""
    relationship_policy: ApplicationRelationshipPolicy = field(init=False)
    """The relationship policy associated with this relationship. Optional. Python type: ``ApplicationRelationshipPolicy``; wire name: ``relationship_policy``; JSON type: object"""
    retained_creator_authority_exists: bool = field(init=False)
    """Whether retained creator authority exists. Optional. Python type: ``bool``; wire name: ``retained_creator_authority_exists``; JSON type: boolean"""
    created_at: datetime = field(init=False)
    """When order creation consumed the single-use Buy link. Required. Python type: ``datetime``; wire name: ``created_at``; JSON type: string (date-time)"""

from inttegro.app.relationship_policy import RelationshipPolicy as ApplicationRelationshipPolicy
