"""Models, requests, and enums for the Inttegro file resource.

The primary returned object is ``inttegro.file.File``. Related request types, nested response shapes, and string-backed enums are exported from this singular namespace. Public members load lazily, so importing one resource does not eagerly import the entire SDK."""

from importlib import import_module
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .actor import Actor as Actor
    from .actor_input import ActorInput as ActorInput
    from .contents_request import ContentsRequest as ContentsRequest
    from .delete_request import DeleteRequest as DeleteRequest
    from .delivery import Delivery as Delivery
    from .delivery_details import DeliveryDetails as DeliveryDetails
    from .disposition import Disposition as Disposition
    from .file import File as File
    from .latest_error import LatestError as LatestError
    from .lookup_request import LookupRequest as LookupRequest
    from .media import Media as Media
    from .page import Page as Page
    from .page_request import PageRequest as PageRequest
    from .page_response import PageResponse as PageResponse
    from .party import Party as Party
    from .party_input import PartyInput as PartyInput
    from .public_storage import PublicStorage as PublicStorage
    from .resource import Resource as Resource
    from .resource_input import ResourceInput as ResourceInput
    from .response import Response as Response
    from .scan_status import ScanStatus as ScanStatus
    from .source import Source as Source
    from .source_type import SourceType as SourceType
    from .status import Status as Status
    from .storage_encoding import StorageEncoding as StorageEncoding
    from .upload_receipt import UploadReceipt as UploadReceipt


_EXPORTS: dict[str, tuple[str, str]] = {
    "Actor": ("inttegro.file.actor", "Actor"),
    "ActorInput": ("inttegro.file.actor_input", "ActorInput"),
    "ContentsRequest": ("inttegro.file.contents_request", "ContentsRequest"),
    "DeleteRequest": ("inttegro.file.delete_request", "DeleteRequest"),
    "Delivery": ("inttegro.file.delivery", "Delivery"),
    "DeliveryDetails": ("inttegro.file.delivery_details", "DeliveryDetails"),
    "Disposition": ("inttegro.file.disposition", "Disposition"),
    "File": ("inttegro.file.file", "File"),
    "LatestError": ("inttegro.file.latest_error", "LatestError"),
    "LookupRequest": ("inttegro.file.lookup_request", "LookupRequest"),
    "Media": ("inttegro.file.media", "Media"),
    "Page": ("inttegro.file.page", "Page"),
    "PageRequest": ("inttegro.file.page_request", "PageRequest"),
    "PageResponse": ("inttegro.file.page_response", "PageResponse"),
    "Party": ("inttegro.file.party", "Party"),
    "PartyInput": ("inttegro.file.party_input", "PartyInput"),
    "PublicStorage": ("inttegro.file.public_storage", "PublicStorage"),
    "Resource": ("inttegro.file.resource", "Resource"),
    "ResourceInput": ("inttegro.file.resource_input", "ResourceInput"),
    "Response": ("inttegro.file.response", "Response"),
    "ScanStatus": ("inttegro.file.scan_status", "ScanStatus"),
    "Source": ("inttegro.file.source", "Source"),
    "SourceType": ("inttegro.file.source_type", "SourceType"),
    "Status": ("inttegro.file.status", "Status"),
    "StorageEncoding": ("inttegro.file.storage_encoding", "StorageEncoding"),
    "UploadReceipt": ("inttegro.file.upload_receipt", "UploadReceipt"),
}

__all__ = [
    "Actor",
    "ActorInput",
    "ContentsRequest",
    "DeleteRequest",
    "Delivery",
    "DeliveryDetails",
    "Disposition",
    "File",
    "LatestError",
    "LookupRequest",
    "Media",
    "Page",
    "PageRequest",
    "PageResponse",
    "Party",
    "PartyInput",
    "PublicStorage",
    "Resource",
    "ResourceInput",
    "Response",
    "ScanStatus",
    "Source",
    "SourceType",
    "Status",
    "StorageEncoding",
    "UploadReceipt",
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
