"""SnapshotResponse in the ``inttegro.balance`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class SnapshotResponse(ApiModel):
    """Typed response returned by the snapshot operation.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``BalanceSnapshotResponse``.
    """
    balances: BalanceSnapshot = field(init=False)
    """The latest GHS balance snapshot for the application. Required. Python type: ``BalanceSnapshot``; wire name: ``balances``; JSON type: object (BalanceSnapshot)"""

from inttegro.balance.balance import Balance as BalanceSnapshot
