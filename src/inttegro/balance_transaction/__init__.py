"""Models, requests, and enums for the Inttegro balance transaction resource.

The primary returned object is ``inttegro.balance_transaction.BalanceTransaction``. Related request types, nested response shapes, and string-backed enums are exported from this singular namespace. Public members load lazily, so importing one resource does not eagerly import the entire SDK."""

from importlib import import_module
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .amount import Amount as Amount
    from .balance_transaction import BalanceTransaction as BalanceTransaction
    from .lookup_request import LookupRequest as LookupRequest
    from .page import Page as Page
    from .page_request import PageRequest as PageRequest
    from .page_response import PageResponse as PageResponse
    from .response import Response as Response
    from .type import Type as Type


_EXPORTS: dict[str, tuple[str, str]] = {
    "Amount": ("inttegro.balance_transaction.amount", "Amount"),
    "BalanceTransaction": ("inttegro.balance_transaction.balance_transaction", "BalanceTransaction"),
    "LookupRequest": ("inttegro.balance_transaction.lookup_request", "LookupRequest"),
    "Page": ("inttegro.balance_transaction.page", "Page"),
    "PageRequest": ("inttegro.balance_transaction.page_request", "PageRequest"),
    "PageResponse": ("inttegro.balance_transaction.page_response", "PageResponse"),
    "Response": ("inttegro.balance_transaction.response", "Response"),
    "Type": ("inttegro.balance_transaction.type", "Type"),
}

__all__ = [
    "Amount",
    "BalanceTransaction",
    "LookupRequest",
    "Page",
    "PageRequest",
    "PageResponse",
    "Response",
    "Type",
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
