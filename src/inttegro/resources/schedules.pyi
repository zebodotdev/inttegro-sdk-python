"""Generated public typing surface. Do not edit by hand."""

from typing import Any

from ..http_client import HttpClient
from .._models import ScheduleCancelDetail, ScheduleDetail
from ..request_types import *

class Schedules:
    def __init__(self, http: HttpClient) -> None: ...
    def lookup(self, schedule_id: str) -> ScheduleDetail: ...
    def cancel(self, schedule_id: str) -> ScheduleCancelDetail: ...
