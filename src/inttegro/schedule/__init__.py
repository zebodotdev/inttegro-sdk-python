"""Models, requests, and enums for the Inttegro schedule resource.

The primary returned object is ``inttegro.schedule.Schedule``. Related request types, nested response shapes, and string-backed enums are exported from this singular namespace. Public members load lazily, so importing one resource does not eagerly import the entire SDK."""

from importlib import import_module
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .cancel_detail import CancelDetail as CancelDetail
    from .cancel_request import CancelRequest as CancelRequest
    from .cancel_response import CancelResponse as CancelResponse
    from .chime_request import ChimeRequest as ChimeRequest
    from .chime_request_request_meta import ChimeRequestRequestMeta as ChimeRequestRequestMeta
    from .creation_detail import CreationDetail as CreationDetail
    from .error import Error as Error
    from .lookup_request import LookupRequest as LookupRequest
    from .lookup_response import LookupResponse as LookupResponse
    from .payout_request import PayoutRequest as PayoutRequest
    from .payout_response import PayoutResponse as PayoutResponse
    from .response import Response as Response
    from .schedule import Schedule as Schedule


_EXPORTS: dict[str, tuple[str, str]] = {
    "CancelDetail": ("inttegro.schedule.cancel_detail", "CancelDetail"),
    "CancelRequest": ("inttegro.schedule.cancel_request", "CancelRequest"),
    "CancelResponse": ("inttegro.schedule.cancel_response", "CancelResponse"),
    "ChimeRequest": ("inttegro.schedule.chime_request", "ChimeRequest"),
    "ChimeRequestRequestMeta": ("inttegro.schedule.chime_request_request_meta", "ChimeRequestRequestMeta"),
    "CreationDetail": ("inttegro.schedule.creation_detail", "CreationDetail"),
    "Error": ("inttegro.schedule.error", "Error"),
    "LookupRequest": ("inttegro.schedule.lookup_request", "LookupRequest"),
    "LookupResponse": ("inttegro.schedule.lookup_response", "LookupResponse"),
    "PayoutRequest": ("inttegro.schedule.payout_request", "PayoutRequest"),
    "PayoutResponse": ("inttegro.schedule.payout_response", "PayoutResponse"),
    "Response": ("inttegro.schedule.response", "Response"),
    "Schedule": ("inttegro.schedule.schedule", "Schedule"),
}

__all__ = [
    "CancelDetail",
    "CancelRequest",
    "CancelResponse",
    "ChimeRequest",
    "ChimeRequestRequestMeta",
    "CreationDetail",
    "Error",
    "LookupRequest",
    "LookupResponse",
    "PayoutRequest",
    "PayoutResponse",
    "Response",
    "Schedule",
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
