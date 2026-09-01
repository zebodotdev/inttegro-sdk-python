"""Broadcasts resource for looking up and canceling broadcasts."""

from __future__ import annotations

from ..http_client import HttpClient


class Broadcasts:
    """Broadcasts resource for managing broadcast chimes."""

    def __init__(self, http: HttpClient):
        self.http = http

    def lookup(self, broadcast_id: str):
        """Lookup a broadcast by broadcast ID."""
        return self.http.post("/broadcasts/lookup", {"broadcast_id": broadcast_id})

    def cancel(self, broadcast_id: str):
        """Cancel a broadcast by broadcast ID."""
        return self.http.post("/broadcasts/cancel", {"broadcast_id": broadcast_id})
