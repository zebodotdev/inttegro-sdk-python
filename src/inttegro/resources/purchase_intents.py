"""Purchase intent resource for Pages Buy links."""

from __future__ import annotations

from ..http_client import HttpClient


class PurchaseIntents:
    """Create, update, cancel, look up, and page Buy link purchase intents.

    Access this service as ``InttegroClient.purchase_intents``. Methods use the client's shared transport and return the typed resource shapes documented below.
    """

    def __init__(self, http: HttpClient):
        self.http = http

    def create(self, payload: dict):
        """Create a Buy link purchase intent.

        API endpoint: ``/purchase_intents/create``.

        Args:
            payload (dict): Typed request object or equivalent request mapping for this operation.

        Returns:
            ``PurchaseIntent`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/purchase_intents/create", payload)

    def update(self, payload: dict):
        """Update mutable Buy link purchase intent fields.

        API endpoint: ``/purchase_intents/update``.

        Args:
            payload (dict): Typed request object or equivalent request mapping for this operation.

        Returns:
            ``PurchaseIntent`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/purchase_intents/update", payload)

    def cancel(self, id: str):
        """Cancel a Buy link purchase intent.

        API endpoint: ``/purchase_intents/cancel``.

        Args:
            id (str): Unique identifier of the id.

        Returns:
            ``PurchaseIntent`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/purchase_intents/cancel", {"id": id})

    def lookup(self, id: str):
        """Retrieve a Buy link purchase intent by ID.

        API endpoint: ``/purchase_intents/lookup``.

        Args:
            id (str): Unique identifier of the id.

        Returns:
            ``PurchaseIntent`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/purchase_intents/lookup", {"id": id})

    def page(self, payload: dict):
        """List Buy link purchase intents.

        API endpoint: ``/purchase_intents/page``.

        Args:
            payload (dict): Typed request object or equivalent request mapping for this operation.

        Returns:
            ``Page`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/purchase_intents/page", payload)
