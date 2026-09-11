"""Quantity in the ``inttegro.purchase_intent`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Quantity(ApiModel):
    """Quantity bounds enforced by the hosted checkout. max is omitted when the offer has no upper bound.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PurchaseIntentQuantity``.
    """
    min: int = field(init=False)
    """Minimum quantity the hosted checkout allows. Required. Python type: ``int``; wire name: ``min``; JSON type: integer. Constraints: minimum 1"""
    max: int | None = field(init=False)
    """Optional maximum quantity the hosted checkout allows. It is always greater than or equal to min when present. Optional; nullable. Python type: ``int | None``; wire name: ``max``; JSON type: integer. Constraints: minimum 1"""
