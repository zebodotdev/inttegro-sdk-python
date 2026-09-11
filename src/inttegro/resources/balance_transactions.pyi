"""Generated public typing surface. Do not edit by hand."""

from typing import Any

from ..http_client import HttpClient
from inttegro.balance_transaction.balance_transaction import BalanceTransaction
from inttegro.balance_transaction.page import Page
from inttegro.balance_transaction.page_request import PageRequest

class BalanceTransactions:
    def __init__(self, http: HttpClient) -> None: ...
    def lookup(self, transaction_id: str) -> BalanceTransaction: ...
    def page(self, payload: PageRequest | None = None) -> Page: ...
