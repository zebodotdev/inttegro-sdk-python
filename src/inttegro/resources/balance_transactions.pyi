"""Generated public typing surface. Do not edit by hand."""

from typing import Any

from ..http_client import HttpClient
from .._models import *
from ..request_types import *
from ..response_object import ResponseObject

class BalanceTransactions:
    def __init__(self, http: HttpClient) -> None: ...
    def lookup(self, transaction_id: str) -> BalanceTransactionResponse: ...
    def page(self, payload: PageBalanceTransactionsRequest | None = None) -> BalanceTransactionPageResponse: ...
