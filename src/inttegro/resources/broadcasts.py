"""Broadcasts resource for looking up and canceling broadcasts."""

from __future__ import annotations

from ..http_client import HttpClient


class Broadcasts:
    """Broadcasts resource for managing broadcast chimes.

    Access this service as ``InttegroClient.broadcasts``. Methods use the client's shared transport and return the typed resource shapes documented below.
    """

    def __init__(self, http: HttpClient):
        self.http = http

    def lookup(self, broadcast_id: str):
        """Lookup a broadcast by broadcast ID.

        API endpoint: ``/broadcasts/lookup``.

        Args:
            broadcast_id (str): Unique identifier of the broadcast.

        Returns:
            ``Broadcast`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/broadcasts/lookup", {"broadcast_id": broadcast_id})

    def cancel(self, broadcast_id: str):
        """Cancel a broadcast by broadcast ID.

        API endpoint: ``/broadcasts/cancel``.

        Args:
            broadcast_id (str): Unique identifier of the broadcast.

        Returns:
            ``CancelDetail`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/broadcasts/cancel", {"broadcast_id": broadcast_id})
