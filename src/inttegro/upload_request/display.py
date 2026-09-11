"""Display in the ``inttegro.upload_request`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Display(ApiModel):
    """Typed display data in the upload request resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``UploadRequestDisplay``.
    """
    title: str | None = field(init=False)
    """The title associated with this display. Optional; nullable. Python type: ``str | None``; wire name: ``title``; JSON type: string"""
    description: str | None = field(init=False)
    """Human-readable description of the display. Optional; nullable. Python type: ``str | None``; wire name: ``description``; JSON type: string"""
    help_text: str | None = field(init=False)
    """The help text associated with this display. Optional; nullable. Python type: ``str | None``; wire name: ``help_text``; JSON type: string"""
