"""Generated public typing surface. Do not edit by hand."""

from typing import Any

from ..http_client import HttpClient
from inttegro.file_reference.reconciliation import Reconciliation
from inttegro.file_reference.reconcile_request import ReconcileRequest

class FileReferences:
    def __init__(self, http: HttpClient) -> None: ...
    def reconcile(self, payload: ReconcileRequest) -> Reconciliation: ...
