"""Generated public typing surface. Do not edit by hand."""

from typing import Any

from ..http_client import HttpClient
from .._models import FileReferenceReconciliation
from ..request_types import *

class FileReferences:
    def __init__(self, http: HttpClient) -> None: ...
    def reconcile(self, payload: FileReferenceReconcileRequest) -> FileReferenceReconciliation: ...
