"""Models, requests, and enums for the Inttegro price resource.

The primary returned object is ``inttegro.price.Price``. Related request types, nested response shapes, and string-backed enums are exported from this singular namespace. Public members load lazily, so importing one resource does not eagerly import the entire SDK."""

from importlib import import_module
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .action_request import ActionRequest as ActionRequest
    from .embedded_product import EmbeddedProduct as EmbeddedProduct
    from .embedded_product_attributes_item import EmbeddedProductAttributesItem as EmbeddedProductAttributesItem
    from .lookup_request import LookupRequest as LookupRequest
    from .page import Page as Page
    from .page_item import PageItem as PageItem
    from .page_request import PageRequest as PageRequest
    from .page_response import PageResponse as PageResponse
    from .params import Params as Params
    from .price import Price as Price
    from .response import Response as Response
    from .update_request import UpdateRequest as UpdateRequest


_EXPORTS: dict[str, tuple[str, str]] = {
    "ActionRequest": ("inttegro.price.action_request", "ActionRequest"),
    "EmbeddedProduct": ("inttegro.price.embedded_product", "EmbeddedProduct"),
    "EmbeddedProductAttributesItem": ("inttegro.price.embedded_product_attributes_item", "EmbeddedProductAttributesItem"),
    "Inline": ("inttegro.price.inline", "Inline"),
    "InlineParams": ("inttegro.price.inline_params", "InlineParams"),
    "LookupRequest": ("inttegro.price.lookup_request", "LookupRequest"),
    "Page": ("inttegro.price.page", "Page"),
    "PageItem": ("inttegro.price.page_item", "PageItem"),
    "PageRequest": ("inttegro.price.page_request", "PageRequest"),
    "PageResponse": ("inttegro.price.page_response", "PageResponse"),
    "Params": ("inttegro.price.params", "Params"),
    "Price": ("inttegro.price.price", "Price"),
    "Response": ("inttegro.price.response", "Response"),
    "UpdateRequest": ("inttegro.price.update_request", "UpdateRequest"),
}

__all__ = [
    "ActionRequest",
    "EmbeddedProduct",
    "EmbeddedProductAttributesItem",
    "Inline",
    "InlineParams",
    "LookupRequest",
    "Page",
    "PageItem",
    "PageRequest",
    "PageResponse",
    "Params",
    "Price",
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
