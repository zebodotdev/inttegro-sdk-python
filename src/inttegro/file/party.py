"""Party in the ``inttegro.file`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Party(ApiModel):
    """Typed party data in the file resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``FileParty``.
    """
    type: str | None = field(init=False)
    """Discriminator identifying the party type. Optional; nullable. Python type: ``str | None``; wire name: ``type``; JSON type: string"""
    id: str | None = field(init=False)
    """Unique identifier for this party. Optional; nullable. Python type: ``str | None``; wire name: ``id``; JSON type: string"""
    name: str | None = field(init=False)
    """Human-readable name of the party. Optional; nullable. Python type: ``str | None``; wire name: ``name``; JSON type: string"""
    email: str | None = field(init=False)
    """The email associated with this party. Optional; nullable. Python type: ``str | None``; wire name: ``email``; JSON type: string (email)"""
