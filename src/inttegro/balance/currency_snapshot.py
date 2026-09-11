"""CurrencySnapshot in the ``inttegro.balance`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class CurrencySnapshot(ApiModel):
    """Typed currency snapshot data in the balance resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``CurrencyBalanceSnapshot``.
    """
    available: BalanceValue = field(init=False)
    """The available associated with this currency snapshot. Required. Python type: ``BalanceValue``; wire name: ``available``; JSON type: object (BalanceValue)"""
    includes_transactions_before: datetime = field(init=False)
    """The snapshot includes transactions created before this timestamp. Required. Python type: ``datetime``; wire name: ``includes_transactions_before``; JSON type: string (date-time)"""
    pending: BalanceValue = field(init=False)
    """The pending associated with this currency snapshot. Required. Python type: ``BalanceValue``; wire name: ``pending``; JSON type: object (BalanceValue)"""
    refund: CurrencyBalanceSnapshotRefund = field(init=False)
    """Funds assigned to refund activity at the snapshot cutoff. Required. Python type: ``CurrencyBalanceSnapshotRefund``; wire name: ``refund``; JSON type: object"""
    reserved: CurrencyBalanceSnapshotReserved = field(init=False)
    """Funds held back from payout at the snapshot cutoff. Required. Python type: ``CurrencyBalanceSnapshotReserved``; wire name: ``reserved``; JSON type: object"""

from inttegro.balance.value import Value as BalanceValue
from inttegro.balance.currency_snapshot_refund import CurrencySnapshotRefund as CurrencyBalanceSnapshotRefund
from inttegro.balance.currency_snapshot_reserved import CurrencySnapshotReserved as CurrencyBalanceSnapshotReserved
