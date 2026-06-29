"""Orders resource for creating and managing orders and payments."""

from __future__ import annotations

from ..http_client import HttpClient


def _stable_order_request_meta(action: str, order_id: str) -> dict:
    return {"idempotency_key": f"orders_{action}_{order_id}"}


class Orders:
    """
    Orders resource for creating orders, processing payments, and managing order lifecycle.

    Orders are the central transaction object in Commerce. They represent a purchase with
    line items, customer information, and payment details. Use this resource to create
    orders, charge customers, handle confirmations, and process refunds.

    The typical order flow is:
    1. Create order with line items and customer details
    2. Pay order with a payment method (may require OTP confirmation)
    3. Finalize order to make it available in reporting
    4. Complete order when fulfillment is done (optional)

    All methods return a ResponseObject containing the API response data.

    See https://commerce.zebo.dev/orders for detailed guides.
    """

    def __init__(self, http: HttpClient):
        """Initialize Orders resource with HTTP client."""
        self.http = http

    def create(self, payload: dict):
        """
        Create a new order with line items, customer, and payment details.

        Creates an order representing a purchase. You can create an order for a new or
        existing customer, include multiple line items, and optionally execute payment
        immediately. Orders must have at least one line item and billing details.

        Args:
            payload: Order creation parameters including:
                - customer_data or customer_id: Customer information (required)
                - line_items: List of products/services being purchased (required)
                - billing_details: Billing contact information (required)
                - payment_method_id or payment_method_data: Payment method (optional)
                - execute_payment: Whether to immediately charge (default: False)
                - request_meta: Request controls such as idempotency_key (optional)
                - statement_descriptor_prefix: Static prefix, 2-10 characters, used to build prefix*order_id (optional)
                - success_url: Redirect URL after successful payment
                - cancel_url: Redirect URL if customer cancels
                - payout_settings: Order-specific payout destination configuration (optional)
                - custom_data: Key-value custom data (max 25KB)

        Returns:
            ResponseObject containing the created order with:
                - order: The order object with id, status, customer, line_items, etc.
                - invoice: Associated invoice details if payment was executed
                - redirect_url: URL to redirect customer for payment (if applicable)

        Raises:
            ApiError: If request fails (invalid parameters, authentication error, etc.)

        Example:
            ```python
            # Create order with new customer
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
                "request_meta": {
                    "idempotency_key": "order_2025_001"
                },
                "execute_payment": True
            })

            order = result.data["order"]
            print(f"Created order: {order['id']}")
            ```

            ```python
            # Create order with saved customer and payment method
            result = client.orders.create({
                "customer_id": "cu_abc123",
                "payment_method_id": "pm_xyz789",
                "line_items": [{
                    "type": "product",
                    "product": {
                        "type": "physical",
                        "name": "T-Shirt",
                        "quantity": 2,
                        "price": {"currency": "ghs", "value": 8000}
                    }
                }],
                "billing_details": {
                    "name": "Kwame Mensah",
                    "phone_number": "+233241234567",
                    "address": {
                        "line1": "123 Independence Ave",
                        "town": "Accra",
                        "region": "Greater Accra",
                        "country": "GH"
                    }
                },
                "execute_payment": True
            })
            ```

        See Also:
            - pay(): Charge an order with a payment method
            - https://commerce.zebo.dev/create-your-first-order
        """
        return self.http.post("/orders/new", payload)

    def new(self, payload: dict):
        """
        Alias for create(). Creates a new order.

        This is a convenience method that calls create() internally. Use whichever
        method name feels more natural in your code.

        Args:
            payload: Same parameters as create()

        Returns:
            ResponseObject with created order details

        Example:
            ```python
            # These are equivalent
            order1 = client.orders.create({...})
            order2 = client.orders.new({...})
            ```
        """
        return self.create(payload)

    def lookup(self, order_id: str, **options):
        """
        Retrieve an existing order by ID.

        Fetches full details of an order including its current status, payment information,
        line items, and customer data. Use this to check order status, retrieve payment
        details, or display order history to customers.

        Args:
            order_id: The order ID (e.g., "or_abc123")
            **options: Additional options:
                - expand: List of fields to expand (e.g., ["customer", "payment"])

        Returns:
            ResponseObject containing:
                - order: Full order object with all details

        Raises:
            ApiError: If order not found or request fails

        Example:
            ```python
            # Basic lookup
            result = client.orders.lookup("or_abc123")
            order = result.data["order"]
            print(f"Order status: {order['status']}")

            # Lookup with expanded fields
            result = client.orders.lookup(
                "or_abc123",
                expand=["customer", "payment", "line_items"]
            )
            ```

        See Also:
            - page(): List multiple orders with pagination
            - https://commerce.zebo.dev/api/orders/lookup
        """
        body = {"order_id": order_id, **options}
        return self.http.post("/orders/lookup", body)

    def pay(self, payload: dict):
        """
        Charge a payment method for an existing order.

        Processes payment for an order using a payment method (saved or new). For mobile
        money payments, the customer typically receives an OTP prompt on their phone.
        If the payment method requires confirmation (confirms_use=True), you'll need to
        call confirm_payment() with the OTP.

        Args:
            payload: Payment parameters including:
                - order_id: The order to charge (required)
                - payment_method_id or payment_method_data: Payment method (required)
                - request_meta.idempotency_key: Unique key to prevent duplicate charges (optional)

        Returns:
            ResponseObject containing:
                - order: Updated order with payment status
                - payment: Payment object with status and details
                - next_action: Required action if payment needs confirmation
                  (type: "confirm_payment" means OTP is needed)

        Raises:
            ApiError: If payment fails or parameters are invalid

        Example:
            ```python
            # Pay with saved payment method
            result = client.orders.pay({
                "order_id": "or_abc123",
                "payment_method_id": "pm_xyz789"
            })

            # Check if confirmation is needed
            if result.data.get("next_action", {}).get("type") == "confirm_payment":
                print("OTP sent to customer's phone")
                # Prompt customer for OTP and call confirm_payment()

            # Pay with new mobile money number
            result = client.orders.pay({
                "order_id": "or_abc123",
                "payment_method_data": {
                    "type": "mobile_money",
                    "mobile_money": {
                        "network": "mtn",
                        "account_number": "0241234567"
                    }
                }
            })

            # Idempotent payment (safe to retry)
            result = client.orders.pay({
                "order_id": "or_abc123",
                "payment_method_id": "pm_xyz789",
                "request_meta": {
                    "idempotency_key": "order_abc123_initial_charge"
                }
            })
            ```

        See Also:
            - confirm_payment(): Submit OTP for payments requiring confirmation
            - create(): Create and pay order in one step with execute_payment=True
            - https://commerce.zebo.dev/charge-repeat-customers
        """
        return self.http.post("/orders/pay", payload)

    def confirm_payment(self, payload: dict):
        """
        Submit OTP confirmation token to complete a payment.

        After calling pay() on a payment method that requires confirmation (confirms_use=True),
        the customer receives an OTP on their mobile device. Collect this OTP from the customer
        and submit it via this method to complete the payment.

        Args:
            payload: Confirmation parameters including:
                - order_id: The order being paid (required)
                - token: The OTP code from customer (required, 6 digits)

        Returns:
            ResponseObject containing:
                - order: Updated order with final payment status
                - payment: Payment object showing success or failure

        Raises:
            ApiError: If OTP is invalid, expired, or payment fails

        Example:
            ```python
            # Step 1: Initiate payment
            result = client.orders.pay({
                "order_id": "or_abc123",
                "payment_method_id": "pm_xyz789"
            })

            # Step 2: Check if confirmation needed
            if result.data.get("next_action", {}).get("type") == "confirm_payment":
                # Display OTP input form to customer
                otp = input("Enter the OTP sent to your phone: ")

                # Step 3: Submit OTP
                result = client.orders.confirm_payment({
                    "order_id": "or_abc123",
                    "token": otp
                })

                if result.data["payment"]["status"] == "paid":
                    print("Payment successful!")
            ```

        See Also:
            - pay(): Initiate payment that may require confirmation
            - request_confirmation(): Resend OTP if customer didn't receive it
            - https://commerce.zebo.dev/charge-repeat-customers
        """
        return self.http.post("/orders/confirm_payment", payload)

    def request_confirmation(self, order_id: str, request_meta: dict | None = None):
        """
        Resend OTP confirmation code to customer.

        If a customer didn't receive the initial OTP or it expired, use this method to
        trigger a new OTP to be sent to their mobile device. The payment must be in a
        state awaiting confirmation.

        Args:
            order_id: The order ID with pending payment confirmation
            request_meta: Request controls such as idempotency_key

        Returns:
            ResponseObject confirming OTP was resent

        Raises:
            ApiError: If order has no pending confirmation or request fails

        Example:
            ```python
            # Customer didn't receive OTP
            result = client.orders.request_confirmation("or_abc123")
            print("New OTP sent to customer's phone")

            # Now prompt customer for the new OTP
            otp = input("Enter the OTP: ")
            client.orders.confirm_payment({
                "order_id": "or_abc123",
                "token": otp
            })
            ```

        See Also:
            - confirm_payment(): Submit the OTP code
            - pay(): Initial payment that triggers OTP
        """
        return self.http.post(
            "/orders/request_confirmation",
            {
                "order_id": order_id,
                "request_meta": request_meta or _stable_order_request_meta(
                    "request_confirmation", order_id
                ),
            },
        )

    def finalize(self, order_id: str, request_meta: dict | None = None):
        """
        Finalize an order to make it available in reports and analytics.

        Finalizing an order locks its line items and amounts, making it appear in financial
        reports, dashboards, and analytics. Only paid orders can be finalized. This is
        typically done automatically but can be called manually if needed.

        Most applications don't need to call this explicitly as orders finalize automatically
        after successful payment.

        Args:
            order_id: The order ID to finalize
            request_meta: Request controls such as idempotency_key

        Returns:
            ResponseObject containing the finalized order

        Raises:
            ApiError: If order is not paid or cannot be finalized

        Example:
            ```python
            # Finalize order manually
            result = client.orders.finalize("or_abc123")
            order = result.data["order"]
            print(f"Order finalized at: {order['finalized_at']}")
            ```

        See Also:
            - complete(): Mark order as fulfilled (separate from finalization)
            - https://commerce.zebo.dev/api/orders/finalize
        """
        return self.http.post(
            "/orders/finalize",
            {
                "order_id": order_id,
                "request_meta": request_meta or _stable_order_request_meta("finalize", order_id),
            },
        )

    def send_invoice(self, payload: dict):
        """
        Send the hosted invoice link for an existing order.

        Args:
            payload: Send invoice parameters including:
                - order_id: The order whose invoice should be sent (required)

        Returns:
            ResponseObject containing the order and delivery details
        """
        return self.http.post("/orders/send_invoice", payload)

    def send_receipt(self, payload: dict):
        """
        Send the hosted receipt link for a paid order.

        Args:
            payload: Send receipt parameters including:
                - order_id: The paid order whose receipt should be sent (required)

        Returns:
            ResponseObject containing the order and delivery details
        """
        return self.http.post("/orders/send_receipt", payload)

    def complete(self, payload: dict):
        """
        Mark an order as complete after fulfillment.

        Call this method after you've fulfilled the order (shipped goods, delivered service,
        etc.). Completing an order is separate from payment—it indicates that your
        obligations to the customer are fulfilled. This affects refund eligibility and
        dispute windows.

        Args:
            payload: Completion parameters including:
                - order_id: The order to mark as complete (required)
                - proof: Optional fulfillment proof (tracking number, photo URL, etc.)

        Returns:
            ResponseObject containing the completed order

        Raises:
            ApiError: If order cannot be completed (not paid, already completed, etc.)

        Example:
            ```python
            # Complete physical goods order
            result = client.orders.complete({
                "order_id": "or_abc123",
                "proof": "TRACKING123456"
            })

            # Complete digital order
            result = client.orders.complete({
                "order_id": "or_abc123"
            })

            order = result.data["order"]
            print(f"Order completed at: {order['completed_at']}")
            ```

        See Also:
            - finalize(): Financial finalization (different from completion)
            - refund(): Issue refund (easier before completion)
            - https://commerce.zebo.dev/api/orders/complete
        """
        return self.http.post("/orders/complete", payload)

    def cancel(self, order_id: str, request_meta: dict | None = None):
        """
        Cancel an unpaid order.

        Cancels an order that hasn't been paid yet. Once cancelled, the order cannot be
        paid or modified. This is useful for abandonment flows, expired carts, or when
        customers explicitly cancel before payment.

        You cannot cancel orders that have been paid. Use refund() instead for paid orders.

        Args:
            order_id: The order ID to cancel
            request_meta: Request controls such as idempotency_key

        Returns:
            ResponseObject containing the cancelled order

        Raises:
            ApiError: If order is already paid or cannot be cancelled

        Example:
            ```python
            # Cancel abandoned order
            result = client.orders.cancel("or_abc123")
            order = result.data["order"]
            print(f"Order status: {order['status']}")  # "cancelled"

            # Cancellation flow with expiration
            import time

            # Create order
            order_result = client.orders.create({...})
            order_id = order_result.data["order"]["id"]

            # Wait for payment (with timeout)
            time.sleep(300)  # 5 minutes

            # Check if still unpaid
            lookup_result = client.orders.lookup(order_id)
            if lookup_result.data["order"]["status"] == "pending":
                # Cancel expired order
                client.orders.cancel(order_id)
            ```

        See Also:
            - refund(): Return money for paid orders
            - https://commerce.zebo.dev/api/orders/cancel
        """
        return self.http.post(
            "/orders/cancel",
            {
                "order_id": order_id,
                "request_meta": request_meta or _stable_order_request_meta("cancel", order_id),
            },
        )

    def refund(self, order_id: str):
        """
        Issue a full refund for a paid order.

        Refunds return money to the customer and reverse the original payment. The refund
        process depends on the payment method—mobile money refunds are instant, while
        card refunds may take 5-10 business days to appear on the customer's statement.

        Only paid orders can be refunded. The order status will change to "refunded" and
        the amount will be returned to the customer's payment method.

        Args:
            order_id: The order ID to refund

        Returns:
            ResponseObject containing:
                - order: Updated order with refund status
                - refund: Refund object with id, amount, and status

        Raises:
            ApiError: If order is not paid, already refunded, or refund fails

        Example:
            ```python
            # Issue refund
            result = client.orders.refund("or_abc123")
            refund = result.data["refund"]
            print(f"Refund status: {refund['status']}")
            print(f"Refund amount: {refund['amount']['value']} {refund['amount']['currency']}")

            # Check refund in order details
            order = result.data["order"]
            print(f"Order status: {order['status']}")  # "refunded"
            ```

        Note:
            - Mobile money refunds: Instant to customer's account
            - Card refunds: 5-10 business days to appear on statement
            - Only full refunds supported currently (no partial refunds)

        See Also:
            - cancel(): Cancel unpaid orders
            - https://commerce.zebo.dev/api/orders/refund
        """
        return self.http.post("/orders/refund", {"order_id": order_id})

    def page(self, payload: dict | None = None):
        """
        List orders with page-based pagination.

        Retrieves a paginated list of orders for your application. Use this to build
        order history views, display transaction data, or export reports. Results are
        sorted by creation date (most recent first).

        Args:
            payload: Pagination parameters including:
                - page_number: Page index to fetch (1-10 inclusive, default: 1)
                - page_size: Number of orders per page (1-256, default: 20)

        Returns:
            ResponseObject containing:
                - page: Object with:
                    - number: The page number returned
                    - size: Number of orders in this page
                    - orders: Array of order objects

        Example:
            ```python
            # Get first page of orders
            result = client.orders.page({"page_number": 1, "page_size": 20})
            page = result.data["page"]
            
            for order in page["orders"]:
                print(f"{order['id']}: {order['status']}")
            
            # Get second page
            next_page = client.orders.page({
                "page_number": 2,
                "page_size": 20
            })
            
            # Retrieve more orders per page
            large_page = client.orders.page({
                "page_number": 1,
                "page_size": 100
            })
            
            # Iterate through all pages
            for page_num in range(1, 11):  # Max 10 pages
                result = client.orders.page({
                    "page_number": page_num,
                    "page_size": 50
                })
                
                page = result.data["page"]
                if page["size"] == 0:
                    break
                
                for order in page["orders"]:
                    print(f"Order: {order['id']}")
            ```

        See Also:
            - lookup(): Get a single order by ID
            - https://commerce.zebo.dev/api/orders/page
        """
        return self.http.post("/orders/page", payload or {})
