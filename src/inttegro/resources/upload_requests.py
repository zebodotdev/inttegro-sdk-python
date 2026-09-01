from __future__ import annotations

from typing import Any

from ..http_client import HttpClient
from ..response_object import ResponseObject


class UploadRequests:
    def __init__(self, http: HttpClient):
        self.http = http

    def create(self, payload: dict[str, Any], idempotency_key: str | None = None) -> ResponseObject:
        headers = {"Idempotency-Key": idempotency_key} if idempotency_key else {}
        return self.http.post_with_headers("/upload_requests/create", payload, headers)

    def lookup(self, id: str) -> ResponseObject:
        return self.http.post("/upload_requests/lookup", {"id": id})

    def page(self, payload: dict[str, Any] | None = None) -> ResponseObject:
        return self.http.post("/upload_requests/page", payload or {})

    def cancel(self, payload: dict[str, Any], idempotency_key: str | None = None) -> ResponseObject:
        headers = {"Idempotency-Key": idempotency_key} if idempotency_key else {}
        return self.http.post_with_headers("/upload_requests/cancel", payload, headers)

    def review(self, payload: dict[str, Any], idempotency_key: str | None = None) -> ResponseObject:
        headers = {"Idempotency-Key": idempotency_key} if idempotency_key else {}
        return self.http.post_with_headers("/upload_requests/review", payload, headers)

    def fulfill(self, *, upload_url: str, file: str) -> ResponseObject:
        return self.http.post_multipart(upload_url, {}, {"file": file}, authenticated=False)
