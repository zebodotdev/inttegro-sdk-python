"""NextActionRedirect in the ``inttegro.payment`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class NextActionRedirect(ApiModel):
    """Details for redirect action.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PaymentNextActionRedirect``.
    """
    redirect_url: str = field(init=False)
    """URL to redirect the customer to. Required. Python type: ``str``; wire name: ``redirect_url``; JSON type: string (uri)"""
    valid_until: datetime = field(init=False)
    """When the redirect URL expires. Required. Python type: ``datetime``; wire name: ``valid_until``; JSON type: string (date-time)"""
    latest_visit: PaymentNextActionRedirectLatestVisit | None = field(init=False)
    """Latest redirect visit details. Optional; nullable. Python type: ``PaymentNextActionRedirectLatestVisit | None``; wire name: ``latest_visit``; JSON type: object"""

from inttegro.payment.next_action_redirect_latest_visit import NextActionRedirectLatestVisit as PaymentNextActionRedirectLatestVisit
