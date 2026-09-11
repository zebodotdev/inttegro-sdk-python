"""NextActionAuthorize in the ``inttegro.payment`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class NextActionAuthorize(ApiModel):
    """Details for authorization action.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PaymentNextActionAuthorize``.
    """
    beneficiary: str = field(init=False)
    """Beneficiary requiring authorization. Required. Python type: ``str``; wire name: ``beneficiary``; JSON type: string"""
    scheme: str = field(init=False)
    """Authorization scheme. Required. Python type: ``str``; wire name: ``scheme``; JSON type: string"""
    expires_at: datetime = field(init=False)
    """When the authorization request expires. Required. Python type: ``datetime``; wire name: ``expires_at``; JSON type: string (date-time)"""
