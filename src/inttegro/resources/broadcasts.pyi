"""Generated public typing surface. Do not edit by hand."""

from typing import Any

from ..http_client import HttpClient
from .._models import *
from ..request_types import *
from ..response_object import ResponseObject

class Broadcasts:
    def __init__(self, http: HttpClient) -> None: ...
    def lookup(self, broadcast_id: str) -> LookupBroadcastResponse: ...
    def cancel(self, broadcast_id: str) -> BroadcastCancelResponse: ...
