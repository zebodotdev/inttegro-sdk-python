"""Models, requests, and enums for the Inttegro secret key resource.

The primary returned object is ``inttegro.secret_key.SecretKey``. Related request types, nested response shapes, and string-backed enums are exported from this singular namespace. Public members load lazily, so importing one resource does not eagerly import the entire SDK."""

from importlib import import_module
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .auth_result import AuthResult as AuthResult
    from .destroy_request import DestroyRequest as DestroyRequest
    from .destroy_response import DestroyResponse as DestroyResponse
    from .generate_request import GenerateRequest as GenerateRequest
    from .generate_response import GenerateResponse as GenerateResponse
    from .generated import Generated as Generated
    from .lookup_request import LookupRequest as LookupRequest
    from .lookup_response import LookupResponse as LookupResponse
    from .page import Page as Page
    from .page_request import PageRequest as PageRequest
    from .page_response import PageResponse as PageResponse
    from .secret_key import SecretKey as SecretKey
    from .status import Status as Status
    from .token_type import TokenType as TokenType
    from .update_request import UpdateRequest as UpdateRequest
    from .update_response import UpdateResponse as UpdateResponse
    from .usage import Usage as Usage
    from .usage_page import UsagePage as UsagePage
    from .usage_request import UsageRequest as UsageRequest
    from .usage_row import UsageRow as UsageRow


_EXPORTS: dict[str, tuple[str, str]] = {
    "AuthResult": ("inttegro.secret_key.auth_result", "AuthResult"),
    "DestroyRequest": ("inttegro.secret_key.destroy_request", "DestroyRequest"),
    "DestroyResponse": ("inttegro.secret_key.destroy_response", "DestroyResponse"),
    "GenerateRequest": ("inttegro.secret_key.generate_request", "GenerateRequest"),
    "GenerateResponse": ("inttegro.secret_key.generate_response", "GenerateResponse"),
    "Generated": ("inttegro.secret_key.generated", "Generated"),
    "LookupRequest": ("inttegro.secret_key.lookup_request", "LookupRequest"),
    "LookupResponse": ("inttegro.secret_key.lookup_response", "LookupResponse"),
    "Page": ("inttegro.secret_key.page", "Page"),
    "PageRequest": ("inttegro.secret_key.page_request", "PageRequest"),
    "PageResponse": ("inttegro.secret_key.page_response", "PageResponse"),
    "SecretKey": ("inttegro.secret_key.secret_key", "SecretKey"),
    "Status": ("inttegro.secret_key.status", "Status"),
    "TokenType": ("inttegro.secret_key.token_type", "TokenType"),
    "UpdateRequest": ("inttegro.secret_key.update_request", "UpdateRequest"),
    "UpdateResponse": ("inttegro.secret_key.update_response", "UpdateResponse"),
    "Usage": ("inttegro.secret_key.usage", "Usage"),
    "UsagePage": ("inttegro.secret_key.usage_page", "UsagePage"),
    "UsageRequest": ("inttegro.secret_key.usage_request", "UsageRequest"),
    "UsageRow": ("inttegro.secret_key.usage_row", "UsageRow"),
}

__all__ = [
    "AuthResult",
    "DestroyRequest",
    "DestroyResponse",
    "GenerateRequest",
    "GenerateResponse",
    "Generated",
    "LookupRequest",
    "LookupResponse",
    "Page",
    "PageRequest",
    "PageResponse",
    "SecretKey",
    "Status",
    "TokenType",
    "UpdateRequest",
    "UpdateResponse",
    "Usage",
    "UsagePage",
    "UsageRequest",
    "UsageRow",
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
