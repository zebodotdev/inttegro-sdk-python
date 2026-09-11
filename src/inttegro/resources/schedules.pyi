"""Generated public typing surface. Do not edit by hand."""

from typing import Any

from ..http_client import HttpClient
from inttegro.schedule.cancel_detail import CancelDetail
from inttegro.schedule.schedule import Schedule

class Schedules:
    def __init__(self, http: HttpClient) -> None: ...
    def lookup(self, schedule_id: str) -> Schedule: ...
    def cancel(self, schedule_id: str) -> CancelDetail: ...
