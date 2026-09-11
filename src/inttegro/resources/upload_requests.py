"""Direct-upload authorization, fulfillment, and review operations."""

from __future__ import annotations

from inttegro.shared.upload_fulfillment import UploadFulfillment
from inttegro.upload_request.upload_request import UploadRequest
from inttegro.upload_request.page import Page
from ..http_client import HttpClient
from inttegro.upload_request.cancel_request import CancelRequest
from inttegro.upload_request.create_request import CreateRequest
from inttegro.upload_request.page_request import PageRequest
from inttegro.upload_request.review_attempt_by_id_request import ReviewAttemptByIDRequest
from inttegro.upload_request.review_attempt_by_ordinal_request import ReviewAttemptByOrdinalRequest


class UploadRequests:
    """Manage direct-upload authorization and the resulting file review flow.

    Access this service as ``InttegroClient.upload_requests``. Methods use the client's shared transport and return the typed resource shapes documented below.
    """

    def __init__(self, http: HttpClient):
        """Bind upload-request operations to the client's shared HTTP transport."""
        self.http = http

    def create(self, payload: CreateRequest, idempotency_key: str | None = None) -> UploadRequest:
        """Create an upload request and return its typed upload instructions.

        API endpoint: ``/upload_requests/create``.

        Args:
            payload (CreateRequest): Typed request object or equivalent request mapping for this operation.
            idempotency_key (str | None): Optional stable key to reuse when retrying the same logical write.

        Returns:
            ``UploadRequest`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        headers = {"Idempotency-Key": idempotency_key} if idempotency_key else {}
        return self.http.post_with_headers("/upload_requests/create", payload, headers)

    def lookup(self, id: str) -> UploadRequest:
        """Return the upload request identified by ``id``.

        API endpoint: ``/upload_requests/lookup``.

        Args:
            id (str): Unique identifier of the id.

        Returns:
            ``UploadRequest`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/upload_requests/lookup", {"id": id})

    def page(self, payload: PageRequest | None = None) -> Page:
        """Return a page of upload requests for the authenticated application.

        API endpoint: ``/upload_requests/page``.

        Args:
            payload (PageRequest | None): Typed request object or equivalent request mapping for this operation.

        Returns:
            ``Page`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/upload_requests/page", payload or {})

    def cancel(self, payload: CancelRequest, idempotency_key: str | None = None) -> UploadRequest:
        """Cancel a pending upload request so it can no longer be fulfilled.

        API endpoint: ``/upload_requests/cancel``.

        Args:
            payload (CancelRequest): Typed request object or equivalent request mapping for this operation.
            idempotency_key (str | None): Optional stable key to reuse when retrying the same logical write.

        Returns:
            ``UploadRequest`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        headers = {"Idempotency-Key": idempotency_key} if idempotency_key else {}
        return self.http.post_with_headers("/upload_requests/cancel", payload, headers)

    def review(
        self,
        payload: ReviewAttemptByIDRequest | ReviewAttemptByOrdinalRequest,
        idempotency_key: str | None = None,
    ) -> UploadRequest:
        """Record an approved or rejected review decision for an upload attempt.

        API endpoint: ``/upload_requests/review``.

        Args:
            payload (ReviewAttemptByIDRequest | ReviewAttemptByOrdinalRequest): Typed request object or equivalent request mapping for this operation.
            idempotency_key (str | None): Optional stable key to reuse when retrying the same logical write.

        Returns:
            ``UploadRequest`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        headers = {"Idempotency-Key": idempotency_key} if idempotency_key else {}
        return self.http.post_with_headers("/upload_requests/review", payload, headers)

    def fulfill(self, *, upload_url: str, file: str) -> UploadFulfillment:
        """Upload ``file`` to the one-time public ``upload_url``.

        Args:
            upload_url (str): Documented upload url value for this operation.
            file (str): Local path of the file content to upload.

        Returns:
            ``UploadFulfillment`` decoded from the documented response shape.
        """
        return self.http.post_multipart(
            upload_url,
            {},
            {"file": file},
            authenticated=False,
            operation="upload_requests.upload",
        )
