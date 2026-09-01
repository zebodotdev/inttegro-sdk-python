"""Schedules resource for looking up and canceling scheduled chimes."""

from __future__ import annotations

from ..http_client import HttpClient


class Schedules:
    """Schedules resource for managing scheduled chimes."""

    def __init__(self, http: HttpClient):
        self.http = http

    def lookup(self, schedule_id: str):
        """Lookup a scheduled chime by schedule ID."""
        return self.http.post("/schedules/lookup", {"schedule_id": schedule_id})

    def cancel(self, schedule_id: str):
        """Cancel a scheduled chime by schedule ID."""
        return self.http.post("/schedules/cancel", {"schedule_id": schedule_id})
