from __future__ import annotations

from pathlib import Path
from typing import Any

from .._models import File, FilePage
from ..http_client import HttpClient
from ..request_types import PageFilesRequest


class FileDownload:
    data: bytes
    headers: dict[str, str]

    def __init__(self, data: bytes, headers: dict[str, str] | None = None) -> None:
        self.data = data
        self.headers = headers or {}

    def save_to(self, path: str) -> None:
        Path(path).write_bytes(self.data)


class Files:
    def __init__(self, http: HttpClient):
        self.http = http

    def create(
        self,
        *,
        file: str,
        purpose: str,
        title: str | None = None,
        custom_data: dict[str, str] | None = None,
        idempotency_key: str | None = None,
    ) -> File:
        headers = {"Idempotency-Key": idempotency_key} if idempotency_key else {}
        return self.http.post_multipart(
            "/files/create",
            {"purpose": purpose, "title": title, "custom_data": custom_data},
            {"file": file},
            headers=headers,
        )

    def lookup(self, file_id: str) -> File:
        return self.http.post("/files/lookup", {"file_id": file_id})

    def page(self, payload: PageFilesRequest | None = None) -> FilePage:
        return self.http.post("/files/page", payload or {})

    def contents(self, *, file_id: str, disposition: str = "attachment") -> FileDownload:
        data, headers = self.http.post_binary_json(
            "/files/contents",
            {"file_id": file_id, "disposition": disposition},
        )
        return FileDownload(data, headers)

    def delete(self, file_id: str) -> File:
        return self.http.post("/files/delete", {"file_id": file_id})
