"""Value in the ``inttegro.balance`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Value(ApiModel):
    """Typed value data in the balance resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``BalanceValue``.
    """
    amount: int = field(init=False)
    """Amount in the currency's smallest unit. Required. Python type: ``int``; wire name: ``amount``; JSON type: integer. Constraints: minimum 0"""
