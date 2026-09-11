"""BalanceValue in the ``inttegro.customer`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from inttegro._model_base import ApiModel
from inttegro.money import Amount


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class BalanceValue(ApiModel):
    """Typed balance value data in the customer resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``CustomerBalanceValue``.
    """
    as_of: datetime = field(init=False)
    """Timestamp for as of. Required. Python type: ``datetime``; wire name: ``as_of``; JSON type: string (date-time)"""
    available: Amount = field(init=False)
    """Monetary available, represented by a currency and an integer minor-unit value. Required. Python type: ``Amount``; wire name: ``available``; JSON type: object (Amount)"""
