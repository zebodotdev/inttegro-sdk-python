"""Generated public typing surface. Do not edit by hand."""

from typing import Any

from ..http_client import HttpClient
from .._models import CurrencyBalanceSnapshot
from ..request_types import *

class Balances:
    def __init__(self, http: HttpClient) -> None: ...
    def get(self) -> dict[str, CurrencyBalanceSnapshot]: ...
