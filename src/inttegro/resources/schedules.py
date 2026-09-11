"""Schedules resource for looking up and canceling scheduled chimes."""

from __future__ import annotations

from ..http_client import HttpClient


class Schedules:
    """Schedules resource for managing scheduled chimes.

    Access this service as ``InttegroClient.schedules``. Methods use the client's shared transport and return the typed resource shapes documented below.
    """

    def __init__(self, http: HttpClient):
        self.http = http

    def lookup(self, schedule_id: str):
        """Lookup a scheduled chime by schedule ID.

        API endpoint: ``/schedules/lookup``.

        Args:
            schedule_id (str): Unique identifier of the schedule.

        Returns:
            ``Schedule`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/schedules/lookup", {"schedule_id": schedule_id})

    def cancel(self, schedule_id: str):
        """Cancel a scheduled chime by schedule ID.

        API endpoint: ``/schedules/cancel``.

        Args:
            schedule_id (str): Unique identifier of the schedule.

        Returns:
            ``CancelDetail`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/schedules/cancel", {"schedule_id": schedule_id})
