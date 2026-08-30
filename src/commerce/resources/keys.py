"""Secret key management resource."""

from __future__ import annotations

from ..http_client import HttpClient


class Keys:
    """Secret key generation, lookup, update, revocation, and usage operations."""

    def __init__(self, http: HttpClient):
        self.http = http

    def generate(self, payload: dict | None = None):
        """Generate a new active secret key. The token is returned only once."""
        return self.http.post("/keys/generate", payload or {})

    def page(self, payload: dict | None = None):
        """List safe secret key metadata."""
        return self.http.post("/keys/page", payload or {})

    def lookup(self, secret_key_id: str):
        """Retrieve safe metadata for a secret key by ID."""
        return self.lookup_with_params({"secret_key_id": secret_key_id})

    def lookup_with_params(self, payload: dict):
        """Retrieve safe metadata using any supported ID alias."""
        return self.http.post("/keys/lookup", payload)

    def update(self, payload: dict):
        """Update safe mutable metadata for a secret key."""
        return self.http.post("/keys/update", payload)

    def destroy(self, secret_key_id: str):
        """Revoke a secret key by ID."""
        return self.destroy_with_params({"secret_key_id": secret_key_id})

    def destroy_with_params(self, payload: dict):
        """Revoke a secret key using any supported ID alias."""
        return self.http.post("/keys/destroy", payload)

    def usage(self, payload: dict | str):
        """Retrieve successful session usage and attributable failed verification attempts."""
        if isinstance(payload, str):
            payload = {"secret_key_id": payload}
        return self.http.post("/keys/usage", payload)
