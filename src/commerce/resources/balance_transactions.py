"""Balance transactions resource for viewing account activity."""

from __future__ import annotations

from ..http_client import HttpClient


class BalanceTransactions:
    """
    Balance transactions resource for viewing detailed account activity.

    Balance transactions are merchant balance entries caused by payments or refunds.
    ``type`` is either ``payment`` or ``refund`` and identifies the semantic source,
    not accounting direction. The matching ``payment_id`` or ``refund_id`` is present.

    See https://studio.inttegro.com/api/balance-transactions for detailed documentation.
    """

    def __init__(self, http: HttpClient):
        """Initialize BalanceTransactions resource with HTTP client."""
        self.http = http

    def lookup(self, transaction_id: str):
        """
        Retrieve a balance transaction by ID.

        Args:
            transaction_id: Balance transaction identifier.

        Returns:
            ResponseObject whose ``transaction`` contains required ``id``, ``type``,
            ``order_id``, ``amount``, and ``created_at`` fields. Switch on ``type`` to
            read exactly one matching ``payment_id`` or ``refund_id``.
        """
        return self.http.post("/balance_transactions/lookup", {"transaction_id": transaction_id})

    def page(self, payload: dict | None = None):
        """
        List balance transactions with page-based pagination.

        Retrieves payment- and refund-sourced merchant balance entries, sorted by
        creation date (most recent first).

        Args:
            payload: Pagination parameters including:
                - page_number: Page index to fetch (1-10 inclusive, default: 1)
                - page_size: Number of transactions per page (1-256, default: 20)

        Returns:
            ResponseObject containing:
                - page: Object with:
                    - number: The page number returned
                    - size: Number of transactions in this page
                    - transactions: Array of objects with required ``id``, ``type``,
                      ``order_id``, ``amount``, and ``created_at``. A payment entry has
                      ``payment_id``; a refund entry has ``refund_id``.

        Example:
            ```python
            # Get first page
            result = client.balance_transactions.page({"page_number": 1, "page_size": 20})
            page = result.page

            for txn in page["transactions"]:
                source_id = txn["payment_id"] if txn["type"] == "payment" else txn["refund_id"]
                print(f"{txn['id']} ({txn['type']} {source_id}): {txn['amount']['value']}")

            # Get second page
            result = client.balance_transactions.page({"page_number": 2, "page_size": 20})
            ```

        See Also:
            - Orders.page(): List orders (source of payment transactions)
            - Payouts.page(): List payouts (source of payout transactions)
            - https://studio.inttegro.com/api/balance-transactions/page
        """
        return self.http.post("/balance_transactions/page", payload or {})
