"""Prices resource for managing catalog prices."""

from __future__ import annotations

from ..http_client import HttpClient


class Prices:
    """Prices resource for creating, updating, and managing prices.

    Access this service as ``InttegroClient.prices``. Methods use the client's shared transport and return the typed resource shapes documented below.
    """

    def __init__(self, http: HttpClient):
        self.http = http

    def create(self, payload: dict):
        """Create a price.

        API endpoint: ``/prices/create``.

        Args:
            payload (dict): Typed request object or equivalent request mapping for this operation.

        Returns:
            ``Price`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/prices/create", payload)

    def lookup(self, price_id: str):
        """Lookup a price by ID.

        API endpoint: ``/prices/lookup``.

        Args:
            price_id (str): Unique identifier of the price.

        Returns:
            ``Price`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/prices/lookup", {"price_id": price_id})

    def page(self, payload: dict | None = None):
        """Page through prices.

        API endpoint: ``/prices/page``.

        Args:
            payload (dict | None): Typed request object or equivalent request mapping for this operation.

        Returns:
            ``Page`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/prices/page", payload or {})

    def update(self, payload: dict):
        """Update a price.

        API endpoint: ``/prices/update``.

        Args:
            payload (dict): Typed request object or equivalent request mapping for this operation.

        Returns:
            ``Price`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/prices/update", payload)

    def activate(self, price_id: str):
        """Activate an inactive price.

        API endpoint: ``/prices/activate``.

        Args:
            price_id (str): Unique identifier of the price.

        Returns:
            ``Price`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/prices/activate", {"price_id": price_id})

    def deactivate(self, price_id: str):
        """Deactivate a price.

        API endpoint: ``/prices/deactivate``.

        Args:
            price_id (str): Unique identifier of the price.

        Returns:
            ``Price`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/prices/deactivate", {"price_id": price_id})

    def archive(self, price_id: str, idempotency_key: str | None = None):
        """Archive a price and mark it inactive.

        API endpoint: ``/prices/archive``.

        Args:
            price_id (str): Unique identifier of the price.
            idempotency_key (str | None): Optional stable key to reuse when retrying the same logical write.

        Returns:
            ``Price`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        headers = {"Idempotency-Key": idempotency_key} if idempotency_key else {}
        return self.http.post_with_headers("/prices/archive", {"price_id": price_id}, headers)
