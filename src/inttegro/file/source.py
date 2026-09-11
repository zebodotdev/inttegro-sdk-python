"""Source in the ``inttegro.file`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Source(ApiModel):
    """Typed source data in the file resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``FileSource``.
    """
    type: Literal['direct', 'upload_request', 'service'] | None = field(init=False)
    """Discriminator identifying the source type. Optional; nullable. Python type: ``Literal['direct', 'upload_request', 'service'] | None``; wire name: ``type``; JSON type: string. Constraints: allowed values ``direct``, ``upload_request``, ``service``"""
    service: str | None = field(init=False)
    """The service associated with this source. Optional; nullable. Python type: ``str | None``; wire name: ``service``; JSON type: string"""
    upload_request_id: str | None = field(init=False)
    """Identifier of the related upload request. Optional; nullable. Python type: ``str | None``; wire name: ``upload_request_id``; JSON type: string"""
