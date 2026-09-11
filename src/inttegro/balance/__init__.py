"""Models, requests, and enums for the Inttegro balance resource.

The primary returned object is ``inttegro.balance.Balance``. Related request types, nested response shapes, and string-backed enums are exported from this singular namespace. Public members load lazily, so importing one resource does not eagerly import the entire SDK."""

from importlib import import_module
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .balance import Balance as Balance
    from .currency_snapshot import CurrencySnapshot as CurrencySnapshot
    from .currency_snapshot_refund import CurrencySnapshotRefund as CurrencySnapshotRefund
    from .currency_snapshot_reserved import CurrencySnapshotReserved as CurrencySnapshotReserved
    from .lookup_request import LookupRequest as LookupRequest
    from .snapshot_response import SnapshotResponse as SnapshotResponse
    from .value import Value as Value


_EXPORTS: dict[str, tuple[str, str]] = {
    "Balance": ("inttegro.balance.balance", "Balance"),
    "CurrencySnapshot": ("inttegro.balance.currency_snapshot", "CurrencySnapshot"),
    "CurrencySnapshotRefund": ("inttegro.balance.currency_snapshot_refund", "CurrencySnapshotRefund"),
    "CurrencySnapshotReserved": ("inttegro.balance.currency_snapshot_reserved", "CurrencySnapshotReserved"),
    "LookupRequest": ("inttegro.balance.lookup_request", "LookupRequest"),
    "SnapshotResponse": ("inttegro.balance.snapshot_response", "SnapshotResponse"),
    "Value": ("inttegro.balance.value", "Value"),
}

__all__ = [
    "Balance",
    "CurrencySnapshot",
    "CurrencySnapshotRefund",
    "CurrencySnapshotReserved",
    "LookupRequest",
    "SnapshotResponse",
    "Value",
]


def __getattr__(name: str) -> Any:
    """Load a public resource type on first access."""
    try:
        module_name, attribute_name = _EXPORTS[name]
    except KeyError:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}") from None
    value = getattr(import_module(module_name), attribute_name)
    globals()[name] = value
    return value
