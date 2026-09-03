from __future__ import annotations

from .._models import FileLink, FileLinkCreation, FileLinkPage
from ..http_client import HttpClient
from ..request_types import CreateFileLinkRequest, PageFileLinksRequest, RevokeFileLinkRequest
from .files import FileDownload


class FileLinks:
    def __init__(self, http: HttpClient):
        self.http = http

    def create(self, payload: CreateFileLinkRequest, idempotency_key: str | None = None) -> FileLinkCreation:
        headers = {"Idempotency-Key": idempotency_key} if idempotency_key else {}
        return self.http.post_with_headers("/file_links/create", payload, headers)

    def lookup(self, id: str) -> FileLink:
        return self.http.post("/file_links/lookup", {"id": id})

    def page(self, payload: PageFileLinksRequest | None = None) -> FileLinkPage:
        return self.http.post("/file_links/page", payload or {})

    def revoke(self, payload: RevokeFileLinkRequest, idempotency_key: str | None = None) -> FileLink:
        headers = {"Idempotency-Key": idempotency_key} if idempotency_key else {}
        return self.http.post_with_headers("/file_links/revoke", payload, headers)

    def open(self, url: str, save_to: str | None = None) -> FileDownload:
        data, headers = self.http.get_binary_public(url)
        download = FileDownload(data, headers)
        if save_to:
            download.save_to(save_to)
        return download
