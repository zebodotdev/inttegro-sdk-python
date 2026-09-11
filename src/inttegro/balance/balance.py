"""Balance in the ``inttegro.balance`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Balance(ApiModel):
    """The latest GHS balance snapshot for the application.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``BalanceSnapshot``.
    """
    ghs: CurrencyBalanceSnapshot = field(init=False)
    """The ghs associated with this balance. Required. Python type: ``CurrencyBalanceSnapshot``; wire name: ``ghs``; JSON type: object (CurrencyBalanceSnapshot)"""

from inttegro.balance.currency_snapshot import CurrencySnapshot as CurrencyBalanceSnapshot
