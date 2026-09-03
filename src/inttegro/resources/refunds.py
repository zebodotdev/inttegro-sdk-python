"""Refunds resource for managing order refunds."""

from __future__ import annotations

from .._models import Refund, RefundPage
from ..http_client import HttpClient
from ..request_types import CreateRefundRequest, PageRefundsRequest


class Refunds:
    """Create, cancel, look up, and page through refunds."""

    def __init__(self, http: HttpClient):
        self.http = http

    def create(self, payload: CreateRefundRequest, idempotency_key: str | None = None) -> Refund:
        """Create a refund for paid order line items."""
        return self.http.post_with_headers(
            "/refunds/create",
            payload,
            self._idempotency_headers(idempotency_key),
        )

    def cancel(self, refund_id: str, idempotency_key: str | None = None) -> Refund:
        """Cancel a pending refund."""
        return self.http.post_with_headers(
            "/refunds/cancel",
            {"refund_id": refund_id},
            self._idempotency_headers(idempotency_key),
        )

    def lookup(self, refund_id: str) -> Refund:
        """Look up a refund by ID."""
        return self.http.post("/refunds/lookup", {"refund_id": refund_id})

    def page(self, payload: PageRefundsRequest) -> RefundPage:
        """Page through refunds."""
        return self.http.post("/refunds/page", payload)

    def _idempotency_headers(self, idempotency_key: str | None) -> dict[str, str]:
        return {"Idempotency-Key": idempotency_key} if idempotency_key else {}
