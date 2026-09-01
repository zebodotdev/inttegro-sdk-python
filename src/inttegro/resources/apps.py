"""Apps resource for managing the authenticated Inttegro application."""

from __future__ import annotations

from ..http_client import HttpClient


class Apps:
    """Application creation, lookup, and update operations."""

    def __init__(self, http: HttpClient):
        self.http = http

    def create(self, payload: dict):
        """Create a Inttegro application."""
        return self.http.post("/apps/create", payload)

    def lookup(self):
        """Retrieve the application associated with the configured API key."""
        return self.http.post("/apps/lookup", {})

    def update(self, payload: dict):
        """Update one or more attributes of the configured API key's application."""
        return self.http.post("/apps/update", payload)
