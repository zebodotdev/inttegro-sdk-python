"""Models, requests, and enums for Inttegro checkout operations.

Import public types from the singular ``inttegro.checkout`` namespace. Related request types, response shapes, and string-backed enums are grouped here for discovery."""

from importlib import import_module
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .order_status import OrderStatus as OrderStatus
    from .payment_status import PaymentStatus as PaymentStatus


_EXPORTS: dict[str, tuple[str, str]] = {
    "OrderStatus": ("inttegro.checkout.order_status", "OrderStatus"),
    "PaymentStatus": ("inttegro.checkout.payment_status", "PaymentStatus"),
}

__all__ = [
    "OrderStatus",
    "PaymentStatus",
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
