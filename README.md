# Inttegro Python SDK

The official Python client for building server-side Inttegro integrations.

> **Fastest, most modern path:** connect an agent to [Inttegro MCP](https://studio.inttegro.com/inttegro-mcp) at `https://mcp.inttegro.com`, then ask it to run `design_integration`. It will produce an implementation and test plan for your application. Use this SDK when you are ready to connect that plan to your Python service.

All official Inttegro SDKs expose the same API capabilities. This package adds Python-specific data access, transports, and test seams.

## Install

Requires Python 3.10 or newer.

```bash
pip install inttegro
```

Store your secret key in the server environment:

```bash
export INTTEGRO_API_KEY="your_secret_key"
```

Never put the key in browser code, a mobile app, or source control. The client uses `https://api.inttegro.com` by default.

## Create a hosted checkout

Create and finalize an order, then send the customer to its hosted invoice URL:

```python
import os

from inttegro import APIError, InttegroClient, ProductType

inttegro = InttegroClient(api_key=os.environ["INTTEGRO_API_KEY"])

try:
    result = inttegro.orders.create({
        "request_meta": {"idempotency_key": "checkout-cart-123"},
        "customer_data": {
            "name": "Akua Mensah",
            "email_address": "akua@example.com",
            "phone_number": "+233544998605",
        },
        "finalize": True,
        "checkout_settings": {
            "redirect_url": "https://example.com/orders/complete",
            "cancel_url": "https://example.com/cart",
        },
        "line_items": [{
            "type": "product",
            "product": {
                "type": ProductType.DIGITAL,
                "name": "Monthly subscription",
                "quantity": 1,
                "price": {"currency": "ghs", "value": 5000},
            },
        }],
    })

    checkout_url = result.order.invoice.format.web.url
    print(result.order.id, checkout_url)
except APIError as error:
    print(error.code, error.detail or str(error))
    raise
```

Amounts use integer minor units: `5000` GHS is GHS 50.00. Reuse the same idempotency key when retrying the same logical write. If you omit one, the SDK generates a UUIDv7 key for mutating calls.

## Work with the API

The SDK covers orders and checkout, customers, products and prices, purchase intents, payment methods, balances, payouts and refunds, notifications, files, application settings, keys, and country specifications. Resources use snake-case attributes such as `purchase_intents` and `payment_methods`.

Python-specific features:

- Standard-library-only runtime with no third-party dependencies.
- Native dictionary requests and responses that support both attribute and mapping access.
- JSON-compatible string enums for public API values.
- Configurable timeout, base URL, and injectable transport for tests or custom networking.
- Structured authentication, rate-limit, network, timeout, and API exceptions.

See the [API reference](https://studio.inttegro.com/api-reference) for request fields and lifecycle rules, [errors](https://studio.inttegro.com/errors) for recovery guidance, and [idempotency](https://studio.inttegro.com/idempotency) for safe retries.

## Verify a release

The GitHub release for each version is the canonical record. It contains the exact wheel and source distribution uploaded to PyPI, SHA-256 checksums, and a Sigstore attestation tied to the source commit and release workflow.

```bash
sha256sum --check SHA256SUMS
gh attestation verify inttegro-1.0.0-py3-none-any.whl \
  --repo zebodotdev/inttegro-sdk-python
```

## Develop

```bash
poetry install
poetry run python -m unittest discover -s tests -p "test_*.py"
```
