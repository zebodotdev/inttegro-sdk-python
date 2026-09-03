"""Generated public typing surface. Do not edit by hand."""

from typing import Any

from ..http_client import HttpClient
from .._models import BroadcastCancelDetail, BroadcastDetail
from ..request_types import *

class Broadcasts:
    def __init__(self, http: HttpClient) -> None: ...
    def lookup(self, broadcast_id: str) -> BroadcastDetail: ...
    def cancel(self, broadcast_id: str) -> BroadcastCancelDetail: ...
