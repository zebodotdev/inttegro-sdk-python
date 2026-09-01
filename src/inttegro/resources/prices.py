"""Prices resource for managing catalog prices."""

from __future__ import annotations

from ..http_client import HttpClient


class Prices:
    """Prices resource for creating, updating, and managing prices."""

    def __init__(self, http: HttpClient):
        self.http = http

    def create(self, payload: dict):
        """Create a price."""
        return self.http.post("/prices/create", payload)

    def lookup(self, price_id: str):
        """Lookup a price by ID."""
        return self.http.post("/prices/lookup", {"price_id": price_id})

    def page(self, payload: dict | None = None):
        """Page through prices."""
        return self.http.post("/prices/page", payload or {})

    def update(self, payload: dict):
        """Update a price."""
        return self.http.post("/prices/update", payload)

    def activate(self, price_id: str):
        """Activate an inactive price."""
        return self.http.post("/prices/activate", {"price_id": price_id})

    def deactivate(self, price_id: str):
        """Deactivate a price."""
        return self.http.post("/prices/deactivate", {"price_id": price_id})

    def archive(self, price_id: str, idempotency_key: str | None = None):
        """Archive a price and mark it inactive."""
        headers = {"Idempotency-Key": idempotency_key} if idempotency_key else {}
        return self.http.post_with_headers("/prices/archive", {"price_id": price_id}, headers)
