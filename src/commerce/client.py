from __future__ import annotations

from .http_client import HttpClient
from .resources.balance_transactions import BalanceTransactions
from .resources.chimes import Chimes
from .resources.customers import Customers
from .resources.schedules import Schedules
from .resources.broadcasts import Broadcasts
from .resources.message_templates import MessageTemplates
from .resources.financial_accounts import FinancialAccounts
from .resources.files import Files
from .resources.file_links import FileLinks
from .resources.otp import Otp
from .resources.orders import Orders
from .resources.payment_methods import PaymentMethods
from .resources.platform import Platform
from .resources.payouts import Payouts
from .resources.products import Products
from .resources.prices import Prices
from .resources.spec import Spec
from .resources.balances import Balances
from .resources.upload_requests import UploadRequests


class CommerceClient:
    """
    Main Commerce SDK client for the Zebo Commerce API.

    The Commerce client provides access to all API resources including orders,
    payment methods, payouts, financial accounts, and more. Initialize with
    your API key from the Commerce dashboard.

    Attributes:
        orders: Orders resource for creating and managing orders, processing payments
        payment_methods: Payment methods resource for tokenizing and managing payment instruments
        payouts: Payouts resource for scheduling and managing fund transfers
        balance_transactions: Balance transactions resource for viewing account activity
        financial_accounts: Financial accounts resource for connecting bank and mobile money accounts
        customers: Customers resource for creating and managing customers
        products: Products resource for managing catalog products
        prices: Prices resource for managing catalog prices
        chimes: Chimes resource for sending transactional notifications
        schedules: Schedules resource for looking up and canceling scheduled chimes
        broadcasts: Broadcasts resource for looking up and canceling broadcasts
        otp: OTP resource for one-time password verification
        platform: Platform resource for application and API key management
        spec: Spec resource for retrieving supported countries and currencies

    Example:
        ```python
        import os
        from commerce import CommerceClient

        # Initialize client with API key
        client = CommerceClient(api_key=os.environ["COMMERCE_API_KEY"])

        # Create and process an order
        result = client.orders.create({
            "customer_data": {
                "name": "Akua Asantewaa",
                "phone_number": "+233541234567",
                "email_address": "akua@example.com"
            },
            "line_items": [{
                "type": "product",
                "product": {
                    "type": "digital",
                    "name": "Premium Subscription",
                    "quantity": 1,
                    "price": {"currency": "ghs", "value": 5000}
                }
            }],
            "billing_details": {
                "name": "Akua Asantewaa",
                "phone_number": "+233541234567"
            },
            "execute_payment": True
        })
        ```

    Thread Safety:
        The client is thread-safe after initialization and can be safely shared
        across multiple threads.
    """

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.zebo.dev",
        timeout: float = 30.0,
        transport=None,
    ):
        """
        Initialize a new Commerce client.

        Args:
            api_key: Your Commerce API key (required). Get this from your dashboard
                at https://commerce.zebo.dev/settings/keys. Use test keys (sk_test_...)
                for development and live keys (sk_live_...) for production.
            base_url: API base URL. Defaults to production (https://api.zebo.dev).
                Override for testing or staging environments.
            timeout: Request timeout in seconds. Defaults to 30.0. Increase for
                long-running operations or slow networks.
            transport: Custom HTTP transport adapter. Pass a requests.Session or
                custom transport for connection pooling, retries, or proxies.

        Raises:
            ValueError: If api_key is empty or invalid

        Example:
            ```python
            # Production usage
            client = CommerceClient(api_key="sk_live_...")

            # Development with custom timeout
            client = CommerceClient(
                api_key="sk_test_...",
                timeout=60.0
            )

            # Testing with mock server
            client = CommerceClient(
                api_key="sk_test_...",
                base_url="http://localhost:8080"
            )
            ```
        """
        self.http = HttpClient(api_key=api_key, base_url=base_url, timeout=timeout, transport=transport)

        self.orders = Orders(self.http)
        self.payment_methods = PaymentMethods(self.http)
        self.payouts = Payouts(self.http)
        self.balance_transactions = BalanceTransactions(self.http)
        self.financial_accounts = FinancialAccounts(self.http)
        self.files = Files(self.http)
        self.file_links = FileLinks(self.http)
        self.customers = Customers(self.http)
        self.products = Products(self.http)
        self.prices = Prices(self.http)
        self.chimes = Chimes(self.http)
        self.schedules = Schedules(self.http)
        self.broadcasts = Broadcasts(self.http)
        self.message_templates = MessageTemplates(self.http)
        self.otp = Otp(self.http)
        self.platform = Platform(self.http)
        self.spec = Spec(self.http)
        self.balances = Balances(self.http)
        self.upload_requests = UploadRequests(self.http)
