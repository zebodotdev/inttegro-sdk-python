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

    def update(self, payload: dict):
        """Update a price."""
        return self.http.post("/prices/update", payload)
