"""Models, requests, and enums for the Inttegro file link resource.

The primary returned object is ``inttegro.file_link.FileLink``. Related request types, nested response shapes, and string-backed enums are exported from this singular namespace. Public members load lazily, so importing one resource does not eagerly import the entire SDK."""

from importlib import import_module
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .access import Access as Access
    from .access_request import AccessRequest as AccessRequest
    from .actor import Actor as Actor
    from .create_request import CreateRequest as CreateRequest
    from .creation import Creation as Creation
    from .delivery import Delivery as Delivery
    from .delivery_input import DeliveryInput as DeliveryInput
    from .delivery_mode import DeliveryMode as DeliveryMode
    from .file_link import FileLink as FileLink
    from .kind import Kind as Kind
    from .lookup_request import LookupRequest as LookupRequest
    from .page import Page as Page
    from .page_request import PageRequest as PageRequest
    from .page_response import PageResponse as PageResponse
    from .response import Response as Response
    from .revoke_request import RevokeRequest as RevokeRequest
    from .status import Status as Status


_EXPORTS: dict[str, tuple[str, str]] = {
    "Access": ("inttegro.file_link.access", "Access"),
    "AccessRequest": ("inttegro.file_link.access_request", "AccessRequest"),
    "Actor": ("inttegro.file_link.actor", "Actor"),
    "CreateRequest": ("inttegro.file_link.create_request", "CreateRequest"),
    "Creation": ("inttegro.file_link.creation", "Creation"),
    "Delivery": ("inttegro.file_link.delivery", "Delivery"),
    "DeliveryInput": ("inttegro.file_link.delivery_input", "DeliveryInput"),
    "DeliveryMode": ("inttegro.file_link.delivery_mode", "DeliveryMode"),
    "FileLink": ("inttegro.file_link.file_link", "FileLink"),
    "Kind": ("inttegro.file_link.kind", "Kind"),
    "LookupRequest": ("inttegro.file_link.lookup_request", "LookupRequest"),
    "Page": ("inttegro.file_link.page", "Page"),
    "PageRequest": ("inttegro.file_link.page_request", "PageRequest"),
    "PageResponse": ("inttegro.file_link.page_response", "PageResponse"),
    "Response": ("inttegro.file_link.response", "Response"),
    "RevokeRequest": ("inttegro.file_link.revoke_request", "RevokeRequest"),
    "Status": ("inttegro.file_link.status", "Status"),
}

__all__ = [
    "Access",
    "AccessRequest",
    "Actor",
    "CreateRequest",
    "Creation",
    "Delivery",
    "DeliveryInput",
    "DeliveryMode",
    "FileLink",
    "Kind",
    "LookupRequest",
    "Page",
    "PageRequest",
    "PageResponse",
    "Response",
    "RevokeRequest",
    "Status",
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
