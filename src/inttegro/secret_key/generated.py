"""Generated in the ``inttegro.secret_key`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Generated(ApiModel):
    """Newly generated secret key. The token is returned once and cannot be retrieved later.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``GeneratedSecretKey``.
    """
    id: str = field(init=False)
    """Secret key identifier. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    label: str | None = field(init=False)
    """Optional human-readable label for the secret key. Optional; nullable. Python type: ``str | None``; wire name: ``label``; JSON type: string"""
    token_type: Literal['bearer'] = field(init=False)
    """The token type associated with this generated. Required. Python type: ``Literal['bearer']``; wire name: ``token_type``; JSON type: string. Constraints: allowed values ``bearer``"""
    issued_at: datetime = field(init=False)
    """Timestamp for issued at. Required. Python type: ``datetime``; wire name: ``issued_at``; JSON type: string (date-time)"""
    token: str = field(init=False)
    """One-time bearer token for the generated key. Required. Python type: ``str``; wire name: ``token``; JSON type: string"""
