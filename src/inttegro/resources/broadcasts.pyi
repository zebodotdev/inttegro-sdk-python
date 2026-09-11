"""Generated public typing surface. Do not edit by hand."""

from typing import Any

from ..http_client import HttpClient
from inttegro.broadcast.cancel_detail import CancelDetail
from inttegro.broadcast.broadcast import Broadcast

class Broadcasts:
    def __init__(self, http: HttpClient) -> None: ...
    def lookup(self, broadcast_id: str) -> Broadcast: ...
    def cancel(self, broadcast_id: str) -> CancelDetail: ...
