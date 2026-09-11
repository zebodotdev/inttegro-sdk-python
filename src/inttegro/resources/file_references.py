"""File reference reconciliation resource."""

from __future__ import annotations

from ..http_client import HttpClient


class FileReferences:
    """Reconcile Inttegro resource file references.

    Access this service as ``InttegroClient.file_references``. Methods use the client's shared transport and return the typed resource shapes documented below.
    """

    def __init__(self, http: HttpClient):
        self.http = http

    def reconcile(self, payload: dict):
        """Replace the live file references for a Inttegro resource.

        API endpoint: ``/file_references/reconcile``.

        Args:
            payload (dict): Typed request object or equivalent request mapping for this operation.

        Returns:
            ``Reconciliation`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/file_references/reconcile", payload)
