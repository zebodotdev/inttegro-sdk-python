"""Generated public typing surface. Do not edit by hand."""

from typing import Any

from ..http_client import HttpClient
from .._models import BalanceTransaction, BalanceTransactionPage
from ..request_types import *

class BalanceTransactions:
    def __init__(self, http: HttpClient) -> None: ...
    def lookup(self, transaction_id: str) -> BalanceTransaction: ...
    def page(self, payload: PageBalanceTransactionsRequest | None = None) -> BalanceTransactionPage: ...
