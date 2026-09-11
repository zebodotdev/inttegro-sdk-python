"""Envelope in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Envelope(ApiModel):
    """Typed envelope data in the order resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``OrderEnvelope``.
    """
    order: Order = field(init=False)
    """Complete order record with line items, customer details, payment state, and fulfillment information. Required. Python type: ``Order``; wire name: ``order``; JSON type: object (Order)"""

from inttegro.order.order import Order
