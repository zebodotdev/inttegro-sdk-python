"""Actor in the ``inttegro.upload_request`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Actor(ApiModel):
    """Typed actor data in the upload request resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``UploadRequestActor``.
    """
    email: str | None = field(init=False)
    """The email associated with this actor. Optional; nullable. Python type: ``str | None``; wire name: ``email``; JSON type: string"""
    id: str | None = field(init=False)
    """Unique identifier for this actor. Optional; nullable. Python type: ``str | None``; wire name: ``id``; JSON type: string"""
    name: str | None = field(init=False)
    """Human-readable name of the actor. Optional; nullable. Python type: ``str | None``; wire name: ``name``; JSON type: string"""
    type: str = field(init=False)
    """Discriminator identifying the actor type. Required. Python type: ``str``; wire name: ``type``; JSON type: string"""
