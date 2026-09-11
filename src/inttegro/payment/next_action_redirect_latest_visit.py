"""NextActionRedirectLatestVisit in the ``inttegro.payment`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class NextActionRedirectLatestVisit(ApiModel):
    """Latest redirect visit details.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PaymentNextActionRedirectLatestVisit``.
    """
    user_agent: str = field(init=False)
    """The user agent associated with this next action redirect latest visit. Required. Python type: ``str``; wire name: ``user_agent``; JSON type: string"""
    ip_address: str = field(init=False)
    """The ip address associated with this next action redirect latest visit. Required. Python type: ``str``; wire name: ``ip_address``; JSON type: string"""
    at: datetime = field(init=False)
    """Timestamp for at. Required. Python type: ``datetime``; wire name: ``at``; JSON type: string (date-time)"""
