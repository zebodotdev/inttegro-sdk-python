"""File reference reconciliation resource."""

from __future__ import annotations

from ..http_client import HttpClient


class FileReferences:
    """Reconcile Commerce resource file references."""

    def __init__(self, http: HttpClient):
        self.http = http

    def reconcile(self, payload: dict):
        """Replace the live file references for a Commerce resource."""
        return self.http.post("/file_references/reconcile", payload)
