"""PullConfigurationMandate in the ``inttegro.financial_account`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PullConfigurationMandate(ApiModel):
    """Typed pull configuration mandate data in the financial account resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``FinancialAccountPullConfigurationMandate``.
    """
    created_at: datetime = field(init=False)
    """When the pull configuration mandate was created. Required. Python type: ``datetime``; wire name: ``created_at``; JSON type: string (date-time)"""
    id: str = field(init=False)
    """Unique identifier for this pull configuration mandate. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    ip_address: str = field(init=False)
    """The ip address associated with this pull configuration mandate. Required. Python type: ``str``; wire name: ``ip_address``; JSON type: string"""
    user_agent: str = field(init=False)
    """The user agent associated with this pull configuration mandate. Required. Python type: ``str``; wire name: ``user_agent``; JSON type: string"""
