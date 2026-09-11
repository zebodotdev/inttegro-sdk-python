"""Verification in the ``inttegro.payment_method`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Verification(ApiModel):
    """Most recent verification record when the payment method has entered a verification flow.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PaymentMethodVerification``.
    """
    completed_at: datetime | None = field(init=False)
    """When verification was completed. Optional; nullable. Python type: ``datetime | None``; wire name: ``completed_at``; JSON type: string (date-time)"""
    initiated_at: datetime = field(init=False)
    """When verification was initiated. Required. Python type: ``datetime``; wire name: ``initiated_at``; JSON type: string (date-time)"""
    mechanism: str | None = field(init=False)
    """Verification mechanism used. Optional; nullable. Python type: ``str | None``; wire name: ``mechanism``; JSON type: string"""
    request_id: str = field(init=False)
    """ID of the verification request. Required. Python type: ``str``; wire name: ``request_id``; JSON type: string"""
    type: str = field(init=False)
    """Verification type. Required. Python type: ``str``; wire name: ``type``; JSON type: string"""
