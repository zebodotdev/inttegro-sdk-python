"""Purchase intent resource for Pages Buy links."""

from __future__ import annotations

from ..http_client import HttpClient


class PurchaseIntents:
    """Create, update, cancel, look up, and page Buy link purchase intents."""

    def __init__(self, http: HttpClient):
        self.http = http

    def create(self, payload: dict):
        """Create a Buy link purchase intent."""
        return self.http.post("/purchase_intents/create", payload)

    def update(self, payload: dict):
        """Update mutable Buy link purchase intent fields."""
        return self.http.post("/purchase_intents/update", payload)

    def cancel(self, id: str):
        """Cancel a Buy link purchase intent."""
        return self.http.post("/purchase_intents/cancel", {"id": id})

    def lookup(self, id: str):
        """Retrieve a Buy link purchase intent by ID."""
        return self.http.post("/purchase_intents/lookup", {"id": id})

    def page(self, payload: dict):
        """List Buy link purchase intents."""
        return self.http.post("/purchase_intents/page", payload)
