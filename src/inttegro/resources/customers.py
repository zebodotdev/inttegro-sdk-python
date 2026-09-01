"""Customers resource for creating and managing customer records."""

from __future__ import annotations

from ..http_client import HttpClient


class Customers:
    """Customers resource for creating, updating, looking up, and paging customers."""

    def __init__(self, http: HttpClient):
        self.http = http

    def create(self, payload: dict):
        """Create a customer record."""
        return self.http.post("/customers/create", payload)

    def lookup(self, customer_id: str):
        """Lookup a customer by ID."""
        return self.http.post("/customers/lookup", {"customer_id": customer_id})

    def update(self, payload: dict, idempotency_key: str | None = None):
        """Update supplied fields on a customer record."""
        headers = {"Idempotency-Key": idempotency_key} if idempotency_key else {}
        return self.http.post_with_headers("/customers/update", payload, headers)

    def page(self, payload: dict | None = None):
        """Page through customers."""
        return self.http.post("/customers/page", payload or {})
