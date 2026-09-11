"""Models, requests, and enums for Inttegro file reference operations.

Import public types from the singular ``inttegro.file_reference`` namespace. Related request types, response shapes, and string-backed enums are grouped here for discovery."""

from importlib import import_module
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .input import Input as Input
    from .reconcile_request import ReconcileRequest as ReconcileRequest
    from .reconciliation import Reconciliation as Reconciliation


_EXPORTS: dict[str, tuple[str, str]] = {
    "Input": ("inttegro.file_reference.input", "Input"),
    "ReconcileRequest": ("inttegro.file_reference.reconcile_request", "ReconcileRequest"),
    "Reconciliation": ("inttegro.file_reference.reconciliation", "Reconciliation"),
}

__all__ = [
    "Input",
    "ReconcileRequest",
    "Reconciliation",
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
