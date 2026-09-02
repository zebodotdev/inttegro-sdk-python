"""Generated public typing surface. Do not edit by hand."""

from typing import Any

from ..http_client import HttpClient
from .._models import *
from ..request_types import *
from ..response_object import ResponseObject

class Apps:
    def __init__(self, http: HttpClient) -> None: ...
    def create(self, payload: CreateApplicationRequest) -> CreateApplicationResponse: ...
    def lookup(self) -> LookupApplicationResponse: ...
    def update(self, payload: UpdateApplicationRequest) -> UpdateApplicationResponse: ...
