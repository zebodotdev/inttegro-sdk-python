from __future__ import annotations

from .._models import UploadFulfillment, UploadRequest, UploadRequestPage
from ..http_client import HttpClient
from ..request_types import (
    CancelUploadRequestRequest,
    CreateUploadRequestRequest,
    PageUploadRequestsRequest,
    ReviewUploadRequestAttemptByIDRequest,
    ReviewUploadRequestAttemptByOrdinalRequest,
)


class UploadRequests:
    def __init__(self, http: HttpClient):
        self.http = http

    def create(self, payload: CreateUploadRequestRequest, idempotency_key: str | None = None) -> UploadRequest:
        headers = {"Idempotency-Key": idempotency_key} if idempotency_key else {}
        return self.http.post_with_headers("/upload_requests/create", payload, headers)

    def lookup(self, id: str) -> UploadRequest:
        return self.http.post("/upload_requests/lookup", {"id": id})

    def page(self, payload: PageUploadRequestsRequest | None = None) -> UploadRequestPage:
        return self.http.post("/upload_requests/page", payload or {})

    def cancel(self, payload: CancelUploadRequestRequest, idempotency_key: str | None = None) -> UploadRequest:
        headers = {"Idempotency-Key": idempotency_key} if idempotency_key else {}
        return self.http.post_with_headers("/upload_requests/cancel", payload, headers)

    def review(
        self,
        payload: ReviewUploadRequestAttemptByIDRequest | ReviewUploadRequestAttemptByOrdinalRequest,
        idempotency_key: str | None = None,
    ) -> UploadRequest:
        headers = {"Idempotency-Key": idempotency_key} if idempotency_key else {}
        return self.http.post_with_headers("/upload_requests/review", payload, headers)

    def fulfill(self, *, upload_url: str, file: str) -> UploadFulfillment:
        return self.http.post_multipart(upload_url, {}, {"file": file}, authenticated=False)
