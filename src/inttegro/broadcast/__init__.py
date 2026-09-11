"""Models, requests, and enums for the Inttegro broadcast resource.

The primary returned object is ``inttegro.broadcast.Broadcast``. Related request types, nested response shapes, and string-backed enums are exported from this singular namespace. Public members load lazily, so importing one resource does not eagerly import the entire SDK."""

from importlib import import_module
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .broadcast import Broadcast as Broadcast
    from .cancel_detail import CancelDetail as CancelDetail
    from .cancel_request import CancelRequest as CancelRequest
    from .cancel_response import CancelResponse as CancelResponse
    from .creation_detail import CreationDetail as CreationDetail
    from .error import Error as Error
    from .lookup_request import LookupRequest as LookupRequest
    from .lookup_response import LookupResponse as LookupResponse
    from .request import Request as Request
    from .request_request_meta import RequestRequestMeta as RequestRequestMeta
    from .response import Response as Response


_EXPORTS: dict[str, tuple[str, str]] = {
    "Broadcast": ("inttegro.broadcast.broadcast", "Broadcast"),
    "CancelDetail": ("inttegro.broadcast.cancel_detail", "CancelDetail"),
    "CancelRequest": ("inttegro.broadcast.cancel_request", "CancelRequest"),
    "CancelResponse": ("inttegro.broadcast.cancel_response", "CancelResponse"),
    "CreationDetail": ("inttegro.broadcast.creation_detail", "CreationDetail"),
    "Error": ("inttegro.broadcast.error", "Error"),
    "LookupRequest": ("inttegro.broadcast.lookup_request", "LookupRequest"),
    "LookupResponse": ("inttegro.broadcast.lookup_response", "LookupResponse"),
    "Request": ("inttegro.broadcast.request", "Request"),
    "RequestRequestMeta": ("inttegro.broadcast.request_request_meta", "RequestRequestMeta"),
    "Response": ("inttegro.broadcast.response", "Response"),
}

__all__ = [
    "Broadcast",
    "CancelDetail",
    "CancelRequest",
    "CancelResponse",
    "CreationDetail",
    "Error",
    "LookupRequest",
    "LookupResponse",
    "Request",
    "RequestRequestMeta",
    "Response",
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
