"""PublicStorage in the ``inttegro.file`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PublicStorage(ApiModel):
    """Typed public storage data in the file resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PublicFileStorage``.
    """
    encoding: Literal['identity', 'br'] = field(init=False)
    """Encoding of the stored representation. Required. Python type: ``Literal['identity', 'br']``; wire name: ``encoding``; JSON type: string. Constraints: allowed values ``identity``, ``br``"""
    stored_size: int = field(init=False)
    """Stored byte size after any lossless encoding. Required. Python type: ``int``; wire name: ``stored_size``; JSON type: integer (int64)"""
