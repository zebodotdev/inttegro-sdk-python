# Zebo Commerce Python SDK

Lightweight Python client for the Zebo Commerce API. It mirrors the Studio samples: orders, payment methods, payouts, OTP, chimes, financial accounts, apps, balance transactions, and specs.

## Installation

This SDK uses Poetry for packaging and targets Python 3.10+.

```bash
cd sdks/python
poetry install
```

Add to your project (once published):

```bash
poetry add zebo-commerce
```

## Quick start

```python
from commerce import CommerceClient

client = CommerceClient(api_key="sk_test_your_key")

order = client.orders.create({
    "customer_data": {"name": "Akua Mensah", "phone_number": "+233544998605"},
    "payout_settings": {
        "destination": {"financial_account_id": "fa_1234567890abcdef"},
        "enable_fx": False,
    },
    "payment_method_data": {
        "type": "mobile_money",
        "mobile_money": {"issuer": "mtn", "number": "0544998605"},
    },
    "line_items": [
        {
            "type": "product",
            "product": {
                "name": "Monthly Subscription",
                "price": {"currency": "ghs", "value": 5000},
                "quantity": 1,
            },
        }
    ],
})

print(order["order"]["id"])
```

Responses are wrapped so you can access keys via attributes or dict style (`order.order.id` or `order["order"]["id"]`).

## Examples

### Hosted checkout (orders.new)

```python
result = client.orders.new({
    "finalize": True,
    "customer_data": {"name": "Jane Doe"},
    "payout_settings": {
        "destination": {"financial_account_id": "fa_1234567890abcdef"},
        "enable_fx": False,
    },
    "line_items": [
        {
            "type": "product",
            "product": {
                "name": "Subscription",
                "quantity": 1,
                "price": {"currency": "ghs", "value": 5000},
            },
        }
    ],
})

checkout_url = result.order.invoice.format.web.url
```

### Handle errors

```python
from commerce import AuthenticationError, RateLimitError, APIError

try:
    client.orders.lookup("or_missing")
except AuthenticationError as e:
    print("Check API key", e)
except RateLimitError as e:
    print("Retry after", e.retry_after)
except APIError as e:
    print("API error", e.status, e)
```

### Tokenize and charge saved payment method

```python
pm = client.payment_methods.tokenize({
    "type": "mobile_money",
    "mobile_money": {"issuer": "mtn", "number": "0544998605"},
})

client.payment_methods.verify(pm.payment_method.id)

payment = client.orders.pay({"order_id": "or_123", "payment_method_id": pm.payment_method.id})

if getattr(payment, "requires_confirmation", False):
    client.orders.confirm_payment({"order_id": payment.order_id, "token": "123456"})
```

### OTP flows (with lookup/cancel from Studio samples)

```python
txn = client.otp.initiate({
    "recipient": "+233241234567",
    "idempotency_key": f"otp_login_{int(__import__('time').time())}",
    "sender": "Acme",
    "service_name": "Acme Bank",
    "purpose": "login",
})

result = client.otp.verify({
    "transaction_id": txn.transaction_id,
    "recipient": "+233241234567",
    "token": "123456",
})
client.otp.lookup({"transaction_id": txn.transaction_id})
client.otp.cancel({"transaction_id": txn.transaction_id, "reason": "user_requested_new_code"})
```

### Payout settings

```python
settings = client.payouts.set_destinations({"ghs": "momo:0544998605"})
```

### Financial accounts

```python
account = client.financial_accounts.connect({
    "label": "Primary GHS Bank Account",
    "type": "bank_account",
    "reference": "BANK-GHS-001",
    "currency": "ghs",
    "owner": {
        "name": "Jane Smith",
        "address": {
            "name": "Business Address",
            "line_1": "456 Business Road",
            "city": "Accra",
            "region": "Greater Accra",
            "country": "Ghana",
        },
    },
    "custom_data": {"merchant_id": "merch_123"},
    "pull_configuration": {"enabled": True, "mandate": {}},
    "bank_account": {
        "type": "ghana_bank_account",
        "ghana_bank_account": {
            "number": "1234567890",
            "sort_code": "040127",
            "holder": {
                "name": "Jane Smith",
                "address": {
                    "name": "Business Address",
                    "line_1": "456 Business Road",
                    "city": "Accra",
                    "region": "Greater Accra",
                    "country": "Ghana",
                },
            },
        },
    },
})

client.financial_accounts.disable_push(
    "fa_1234567890abcdef",
    unset_as_payout_destination=True,
)

client.financial_accounts.disconnect(
    "fa_1234567890abcdef",
    unset_as_payout_destination=True,
)

client.financial_accounts.page({"page_number": 1, "page_size": 50})
```

### Customers

```python
customer = client.customers.create({
    "name": "Jane Doe",
    "email_address": "jane@example.com",
    "phone_number": "+233501234567",
})

existing = client.customers.lookup("cu_1234567890abcdef")
page = client.customers.page({"page_number": 1, "page_size": 50})
```

### Products

```python
product = client.products.create({
    "type": "physical",
    "name": "Premium Cotton T-Shirt",
})

client.products.add_price({
    "product_id": product["product"]["id"],
    "amount": {"currency": "ghs", "value": 5000},
    "set_as_default": True,
})

products_page = client.products.page({"page_number": 1, "page_size": 50})

client.products.publish(product["product"]["id"])
```

### Prices

```python
price = client.prices.create({
    "currency": "USD",
    "amount": 1999,
    "label": "Standard pricing",
})

client.prices.update({
    "price_id": price["price"]["id"],
    "label": "Premium pricing",
})
```

### Apps

```python
app = client.apps.create({"name": "My App"})
current_app = client.apps.lookup()
updated_app = client.apps.update({"alias": "my-app"})
```

## Available resources

- `client.orders.create|new|lookup|pay|confirm_payment|request_confirmation|finalize|complete|cancel|refund|page`
- `client.payment_methods.tokenize|verify|confirm_verification|lookup|delete|settings`
- `client.payouts.set_destinations|settings|disable_automatic|enable_fx|disable_fx|page|cancel`
- `client.balance_transactions.page`
- `client.financial_accounts.create|lookup|connect|archive|page|verify|update|enable_push|disable_push|enable_pull|disable_pull|disconnect`
- `client.customers.create|lookup|page`
- `client.prices.create|lookup|update`
- `client.products.create|add_price|set_default_unit_price|lookup|update|publish|unpublish|archive|page`
- `client.chimes.send|lookup|schedule|broadcast`
- `client.schedules.lookup|cancel`
- `client.broadcasts.lookup|cancel`
- `client.otp.initiate|verify|lookup|cancel`
- `client.balances.get`
- `client.apps.create|lookup|update`
- `client.spec.countries`

## Development

From `sdks/python`:

```bash
poetry install
poetry run python -m unittest discover -s tests -p "test_*.py"
```

CI and release workflows live in `sdks/python/.github`.

## API enum values

String enums are exported from `commerce` and encode directly in JSON:

```python
from commerce import ProductType, RefundReason

payload = {
    "type": ProductType.DIGITAL,
    "reason": RefundReason.REQUESTED_BY_CUSTOMER,
}
```
