"""SecretKey in the ``inttegro.secret_key`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class SecretKey(ApiModel):
    """Public secret key metadata. The bearer token is never returned by read or mutation endpoints.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.
    """
    id: str = field(init=False)
    """Application-scoped secret key identifier. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    label: str | None = field(init=False)
    """Optional human-readable label for the secret key. Optional; nullable. Python type: ``str | None``; wire name: ``label``; JSON type: string"""
    token_type: Literal['bearer'] = field(init=False)
    """The token type associated with this secret key. Required. Python type: ``Literal['bearer']``; wire name: ``token_type``; JSON type: string. Constraints: allowed values ``bearer``"""
    issued_at: datetime = field(init=False)
    """Timestamp for issued at. Required. Python type: ``datetime``; wire name: ``issued_at``; JSON type: string (date-time)"""
    updated_at: datetime | None = field(init=False)
    """Omitted until the label is changed. Optional; nullable. Python type: ``datetime | None``; wire name: ``updated_at``; JSON type: string (date-time)"""
    expires_at: datetime | None = field(init=False)
    """Omitted for keys without a fixed expiry. Optional; nullable. Python type: ``datetime | None``; wire name: ``expires_at``; JSON type: string (date-time)"""
    status: Literal['active', 'revoked', 'expired'] = field(init=False)
    """Current lifecycle status of the secret key. Required. Python type: ``Literal['active', 'revoked', 'expired']``; wire name: ``status``; JSON type: string. Constraints: allowed values ``active``, ``revoked``, ``expired``"""
    active: bool = field(init=False)
    """Whether the secret key is active. Required. Python type: ``bool``; wire name: ``active``; JSON type: boolean"""
    revoked_at: datetime | None = field(init=False)
    """Omitted until the key is revoked. Optional; nullable. Python type: ``datetime | None``; wire name: ``revoked_at``; JSON type: string (date-time)"""
    last_used_at: datetime | None = field(init=False)
    """Most recent recorded authentication when available; otherwise omitted. Optional; nullable. Python type: ``datetime | None``; wire name: ``last_used_at``; JSON type: string (date-time)"""
    usage_count: int | None = field(init=False)
    """Number of recorded authentications when available; omitted when zero. Optional; nullable. Python type: ``int | None``; wire name: ``usage_count``; JSON type: integer. Constraints: minimum 0"""
