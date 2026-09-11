"""Supplied in the ``inttegro.payment_method`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Supplied(ApiModel):
    """Public provenance for how the payment method was supplied.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PaymentMethodSupplied``.
    """
    attempt_id: str | None = field(init=False)
    """Identifier of the related attempt. Optional; nullable. Python type: ``str | None``; wire name: ``attempt_id``; JSON type: string"""
    by: str = field(init=False)
    """The by associated with this supplied. Required. Python type: ``str``; wire name: ``by``; JSON type: string"""
    channel: str | None = field(init=False)
    """The channel associated with this supplied. Optional; nullable. Python type: ``str | None``; wire name: ``channel``; JSON type: string"""
    resource_id: str | None = field(init=False)
    """Identifier of the related resource. Optional; nullable. Python type: ``str | None``; wire name: ``resource_id``; JSON type: string"""
    resource_type: str | None = field(init=False)
    """The resource type associated with this supplied. Optional; nullable. Python type: ``str | None``; wire name: ``resource_type``; JSON type: string"""
    supplied_at: datetime = field(init=False)
    """Timestamp for supplied at. Required. Python type: ``datetime``; wire name: ``supplied_at``; JSON type: string (date-time)"""
