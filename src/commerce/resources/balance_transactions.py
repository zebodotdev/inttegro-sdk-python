"""Balance transactions resource for viewing account activity."""

from __future__ import annotations

from ..http_client import HttpClient


class BalanceTransactions:
    """
    Balance transactions resource for viewing detailed account activity.

    Balance transactions represent individual changes to your Commerce balance. Each
    transaction records a payment, payout, refund, fee, or other balance event with
    full details about amount, currency, source, and timing.

    See https://studio.zebo.dev/api/balance-transactions for detailed documentation.
    """

    def __init__(self, http: HttpClient):
        """Initialize BalanceTransactions resource with HTTP client."""
        self.http = http

    def page(self, payload: dict | None = None):
        """
        List balance transactions with page-based pagination.

        Retrieves a paginated history of all balance activity including payments received,
        payouts sent, refunds issued, and fees charged. Results are sorted by creation
        date (most recent first).

        Args:
            payload: Pagination parameters including:
                - page_number: Page index to fetch (1-10 inclusive, default: 1)
                - page_size: Number of transactions per page (1-256, default: 20)

        Returns:
            ResponseObject containing:
                - page: Object with:
                    - number: The page number returned
                    - size: Number of transactions in this page
                    - transactions: Array of balance transaction objects

        Example:
            ```python
            # Get first page
            result = client.balance_transactions.page({"page_number": 1, "page_size": 20})
            page = result.data["page"]
            
            for txn in page["transactions"]:
                print(f"{txn['id']}: {txn['amount_expected']['value']}")
            
            # Get second page
            result = client.balance_transactions.page({"page_number": 2, "page_size": 20})
            ```

        See Also:
            - Orders.page(): List orders (source of payment transactions)
            - Payouts.page(): List payouts (source of payout transactions)
            - https://studio.zebo.dev/api/balance-transactions/page
        """
        return self.http.post("/balance_transactions/page", payload or {})
