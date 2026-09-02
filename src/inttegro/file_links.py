"""Typed request objects for file-link operations."""

from .request_types import (
    CreateFileLinkRequest as CreateRequest,
    FileLinkAccessRequest as Access,
    FileLinkDeliveryInput as Delivery,
    PageFileLinksRequest as PageRequest,
    RevokeFileLinkRequest as RevokeRequest,
)

__all__ = ["Access", "CreateRequest", "Delivery", "PageRequest", "RevokeRequest"]
