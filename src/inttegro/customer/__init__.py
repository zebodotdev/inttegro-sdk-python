"""Models, requests, and enums for the Inttegro customer resource.

The primary returned object is ``inttegro.customer.Customer``. Related request types, nested response shapes, and string-backed enums are exported from this singular namespace. Public members load lazily, so importing one resource does not eagerly import the entire SDK."""

from importlib import import_module
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .address import Address as Address
    from .address_input import AddressInput as AddressInput
    from .balance_value import BalanceValue as BalanceValue
    from .create_request import CreateRequest as CreateRequest
    from .customer import Customer as Customer
    from .data_input import DataInput as DataInput
    from .lookup_request import LookupRequest as LookupRequest
    from .page import Page as Page
    from .page_request import PageRequest as PageRequest
    from .page_response import PageResponse as PageResponse
    from .response import Response as Response
    from .update_request import UpdateRequest as UpdateRequest


_EXPORTS: dict[str, tuple[str, str]] = {
    "Address": ("inttegro.customer.address", "Address"),
    "AddressInput": ("inttegro.customer.address_input", "AddressInput"),
    "BalanceValue": ("inttegro.customer.balance_value", "BalanceValue"),
    "CreateRequest": ("inttegro.customer.create_request", "CreateRequest"),
    "Customer": ("inttegro.customer.customer", "Customer"),
    "DataInput": ("inttegro.customer.data_input", "DataInput"),
    "LookupRequest": ("inttegro.customer.lookup_request", "LookupRequest"),
    "Page": ("inttegro.customer.page", "Page"),
    "PageRequest": ("inttegro.customer.page_request", "PageRequest"),
    "PageResponse": ("inttegro.customer.page_response", "PageResponse"),
    "Response": ("inttegro.customer.response", "Response"),
    "UpdateRequest": ("inttegro.customer.update_request", "UpdateRequest"),
}

__all__ = [
    "Address",
    "AddressInput",
    "BalanceValue",
    "CreateRequest",
    "Customer",
    "DataInput",
    "LookupRequest",
    "Page",
    "PageRequest",
    "PageResponse",
    "Response",
    "UpdateRequest",
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
