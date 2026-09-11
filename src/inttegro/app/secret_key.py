"""SecretKey in the ``inttegro.app`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class SecretKey(ApiModel):
    """Newly generated secret key. The token is returned once and cannot be retrieved later.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``ApplicationSecretKey``.
    """
    id: str | None = field(init=False)
    """Secret key identifier. Required; nullable. Python type: ``str | None``; wire name: ``id``; JSON type: string"""
    token_type: str | None = field(init=False)
    """The token type associated with this secret key. Required; nullable. Python type: ``str | None``; wire name: ``token_type``; JSON type: string. Constraints: allowed values ``bearer``"""
    issued_at: datetime | None = field(init=False)
    """Timestamp for issued at. Required; nullable. Python type: ``datetime | None``; wire name: ``issued_at``; JSON type: string (date-time)"""
    token: str | None = field(init=False)
    """One-time bearer token for the generated key. Required; nullable. Python type: ``str | None``; wire name: ``token``; JSON type: string"""
