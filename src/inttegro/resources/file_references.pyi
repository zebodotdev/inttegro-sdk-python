"""Generated public typing surface. Do not edit by hand."""

from typing import Any

from ..http_client import HttpClient
from .._models import *
from ..request_types import *
from ..response_object import ResponseObject

class FileReferences:
    def __init__(self, http: HttpClient) -> None: ...
    def reconcile(self, payload: FileReferenceReconcileRequest) -> FileReferenceReconcileResponse: ...
