"""UsageRow in the ``inttegro.secret_key`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UsageRow(ApiModel):
    """Public authentication outcome associated with the selected key.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``SecretKeyUsageRow``.
    """
    secret_key_id: str = field(init=False)
    """Identifier of the related secret key. Required. Python type: ``str``; wire name: ``secret_key_id``; JSON type: string"""
    occurred_at: datetime = field(init=False)
    """Timestamp for occurred at. Required. Python type: ``datetime``; wire name: ``occurred_at``; JSON type: string (date-time)"""
    auth_result: Literal['succeeded', 'failed'] = field(init=False)
    """The auth result associated with this usage row. Required. Python type: ``Literal['succeeded', 'failed']``; wire name: ``auth_result``; JSON type: string. Constraints: allowed values ``succeeded``, ``failed``"""
