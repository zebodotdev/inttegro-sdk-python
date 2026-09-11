"""CreatedFrom in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class CreatedFrom(ApiModel):
    """Attribution for the public resource that created this order, when available.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``OrderCreatedFrom``.
    """
    source: str | None = field(init=False)
    """The source associated with this created from. Optional; nullable. Python type: ``str | None``; wire name: ``source``; JSON type: string"""
    resource_type: Literal['purchase_intent'] | None = field(init=False)
    """The resource type associated with this created from. Optional; nullable. Python type: ``Literal['purchase_intent'] | None``; wire name: ``resource_type``; JSON type: string. Constraints: allowed values ``purchase_intent``"""
    resource_id: str | None = field(init=False)
    """Identifier of the related resource. Optional; nullable. Python type: ``str | None``; wire name: ``resource_id``; JSON type: string"""
