"""Secret key management resource."""

from __future__ import annotations

from ..http_client import HttpClient


class Keys:
    """Secret key generation, lookup, update, revocation, and usage operations.

    Access this service as ``InttegroClient.keys``. Methods use the client's shared transport and return the typed resource shapes documented below.
    """

    def __init__(self, http: HttpClient):
        self.http = http

    def generate(self, payload: dict | None = None):
        """Generate a new active secret key. The token is returned only once.

        API endpoint: ``/keys/generate``.

        Args:
            payload (dict | None): Typed request object or equivalent request mapping for this operation.

        Returns:
            ``Generated`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/keys/generate", payload or {})

    def page(self, payload: dict | None = None):
        """List safe secret key metadata.

        API endpoint: ``/keys/page``.

        Args:
            payload (dict | None): Typed request object or equivalent request mapping for this operation.

        Returns:
            ``Page`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/keys/page", payload or {})

    def lookup(self, secret_key_id: str):
        """Retrieve safe metadata for a secret key by ID.

        Args:
            secret_key_id (str): Unique identifier of the secret key.

        Returns:
            ``SecretKey`` decoded from the documented response shape.
        """
        return self.lookup_with_params({"secret_key_id": secret_key_id})

    def lookup_with_params(self, payload: dict):
        """Retrieve safe metadata using any supported ID alias.

        API endpoint: ``/keys/lookup``.

        Args:
            payload (dict): Typed request object or equivalent request mapping for this operation.

        Returns:
            ``SecretKey`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/keys/lookup", payload)

    def update(self, payload: dict):
        """Update safe mutable metadata for a secret key.

        API endpoint: ``/keys/update``.

        Args:
            payload (dict): Typed request object or equivalent request mapping for this operation.

        Returns:
            ``SecretKey`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/keys/update", payload)

    def destroy(self, secret_key_id: str):
        """Revoke a secret key by ID.

        Args:
            secret_key_id (str): Unique identifier of the secret key.

        Returns:
            ``SecretKey`` decoded from the documented response shape.
        """
        return self.destroy_with_params({"secret_key_id": secret_key_id})

    def destroy_with_params(self, payload: dict):
        """Revoke a secret key using any supported ID alias.

        API endpoint: ``/keys/destroy``.

        Args:
            payload (dict): Typed request object or equivalent request mapping for this operation.

        Returns:
            ``SecretKey`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/keys/destroy", payload)

    def usage(self, payload: dict | str):
        """Retrieve successful session usage and attributable failed verification attempts.

        API endpoint: ``/keys/usage``.

        Args:
            payload (dict | str): Typed request object or equivalent request mapping for this operation.

        Returns:
            ``Usage`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        if isinstance(payload, str):
            payload = {"secret_key_id": payload}
        return self.http.post("/keys/usage", payload)
