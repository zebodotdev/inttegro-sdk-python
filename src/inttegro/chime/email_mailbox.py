"""EmailMailbox in the ``inttegro.chime`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class EmailMailbox(ApiModel):
    """Typed email mailbox data in the chime resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``ChimeEmailMailbox``.
    """
    name: str | None = field(init=False)
    """Optional display name. Optional; nullable. Python type: ``str | None``; wire name: ``name``; JSON type: string"""
    address: str | None = field(init=False)
    """Email address. Optional; nullable. Python type: ``str | None``; wire name: ``address``; JSON type: string (email)"""
