"""NextActionConfirmPaymentAttempt in the ``inttegro.payment`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class NextActionConfirmPaymentAttempt(ApiModel):
    """Latest confirmation attempt.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PaymentNextActionConfirmPaymentAttempt``.
    """
    status: str = field(init=False)
    """Attempt status. Required. Python type: ``str``; wire name: ``status``; JSON type: string"""
    confirmed: bool = field(init=False)
    """Whether the confirmation has succeeded. Required. Python type: ``bool``; wire name: ``confirmed``; JSON type: boolean"""
    reason: str = field(init=False)
    """Reason for the current attempt state. Required. Python type: ``str``; wire name: ``reason``; JSON type: string"""
    executed_at: datetime | None = field(init=False)
    """When the attempt was executed. Optional; nullable. Python type: ``datetime | None``; wire name: ``executed_at``; JSON type: string (date-time)"""
    created_at: datetime = field(init=False)
    """When the attempt was created. Required. Python type: ``datetime``; wire name: ``created_at``; JSON type: string (date-time)"""
