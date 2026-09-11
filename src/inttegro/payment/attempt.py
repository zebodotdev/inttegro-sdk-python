"""Attempt in the ``inttegro.payment`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Attempt(ApiModel):
    """Most recent payment attempt details.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PaymentAttempt``.
    """
    payment_method_type: str | None = field(init=False)
    """The payment method type associated with this attempt. Optional; nullable. Python type: ``str | None``; wire name: ``payment_method_type``; JSON type: string"""
    payment_method_id: str | None = field(init=False)
    """Identifier of the related payment method. Optional; nullable. Python type: ``str | None``; wire name: ``payment_method_id``; JSON type: string"""
    error: PaymentAttemptError | None = field(init=False)
    """The error associated with this attempt. Optional; nullable. Python type: ``PaymentAttemptError | None``; wire name: ``error``; JSON type: object"""
    reference: str | None = field(init=False)
    """External payment reference. Optional; nullable. Python type: ``str | None``; wire name: ``reference``; JSON type: string"""
    status: Literal['initiated', 'executed', 'succeeded', 'canceled', 'expired', 'failed', 'unknown'] = field(init=False)
    """Current lifecycle status of the attempt. Required. Python type: ``Literal['initiated', 'executed', 'succeeded', 'canceled', 'expired', 'failed', 'unknown']``; wire name: ``status``; JSON type: string. Constraints: allowed values ``initiated``, ``executed``, ``succeeded``, ``canceled``, ``expired``, ``failed``, ``unknown``"""
    initiated_at: datetime = field(init=False)
    """Timestamp for initiated at. Required. Python type: ``datetime``; wire name: ``initiated_at``; JSON type: string (date-time)"""
    succeeded_at: datetime | None = field(init=False)
    """Timestamp for succeeded at. Optional; nullable. Python type: ``datetime | None``; wire name: ``succeeded_at``; JSON type: string (date-time)"""

from inttegro.payment.attempt_error import AttemptError as PaymentAttemptError
