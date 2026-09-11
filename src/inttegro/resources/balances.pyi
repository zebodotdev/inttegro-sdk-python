"""Generated public typing surface. Do not edit by hand."""

from typing import Any

from ..http_client import HttpClient
from inttegro.balance.balance import Balance

class Balances:
    def __init__(self, http: HttpClient) -> None: ...
    def get(self) -> Balance: ...
