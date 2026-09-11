"""Controlled-link operations for serving managed Inttegro files."""

from __future__ import annotations

from inttegro.file_link.file_link import FileLink
from inttegro.file_link.creation import Creation
from inttegro.file_link.page import Page
from ..http_client import HttpClient
from inttegro.file_link.create_request import CreateRequest
from inttegro.file_link.page_request import PageRequest
from inttegro.file_link.revoke_request import RevokeRequest
from .files import FileDownload


class FileLinks:
    """Create and manage controlled links to managed file content.

    Access this service as ``InttegroClient.file_links``. Methods use the client's shared transport and return the typed resource shapes documented below.
    """

    def __init__(self, http: HttpClient):
        """Bind file-link operations to the client's shared HTTP transport."""
        self.http = http

    def create(self, payload: CreateRequest, idempotency_key: str | None = None) -> Creation:
        """Create a controlled file link and return its one-time creation data.

        API endpoint: ``/file_links/create``.

        Args:
            payload (CreateRequest): Typed request object or equivalent request mapping for this operation.
            idempotency_key (str | None): Optional stable key to reuse when retrying the same logical write.

        Returns:
            ``Creation`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        headers = {"Idempotency-Key": idempotency_key} if idempotency_key else {}
        return self.http.post_with_headers("/file_links/create", payload, headers)

    def lookup(self, id: str) -> FileLink:
        """Return the file link identified by ``id``.

        API endpoint: ``/file_links/lookup``.

        Args:
            id (str): Unique identifier of the id.

        Returns:
            ``FileLink`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/file_links/lookup", {"id": id})

    def page(self, payload: PageRequest | None = None) -> Page:
        """Return a page of file links for the authenticated application.

        API endpoint: ``/file_links/page``.

        Args:
            payload (PageRequest | None): Typed request object or equivalent request mapping for this operation.

        Returns:
            ``Page`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/file_links/page", payload or {})

    def revoke(self, payload: RevokeRequest, idempotency_key: str | None = None) -> FileLink:
        """Revoke a file link so future attempts cannot use it.

        API endpoint: ``/file_links/revoke``.

        Args:
            payload (RevokeRequest): Typed request object or equivalent request mapping for this operation.
            idempotency_key (str | None): Optional stable key to reuse when retrying the same logical write.

        Returns:
            ``FileLink`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        headers = {"Idempotency-Key": idempotency_key} if idempotency_key else {}
        return self.http.post_with_headers("/file_links/revoke", payload, headers)

    def open(self, url: str, save_to: str | None = None) -> FileDownload:
        """Download a public file-link ``url`` and optionally save it to ``save_to``.

        Args:
            url (str): Inttegro-issued public URL; credentials are not attached to this request.
            save_to (str | None): Optional local path where the downloaded bytes are written.

        Returns:
            ``FileDownload`` decoded from the documented response shape.
        """
        data, headers = self.http.get_binary_public(url)
        download = FileDownload(data, headers)
        if save_to:
            download.save_to(save_to)
        return download
