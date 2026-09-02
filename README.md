# Inttegro Python SDK

[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/zebodotdev/inttegro-sdk-python/badge)](https://scorecard.dev/viewer/?uri=github.com/zebodotdev/inttegro-sdk-python)

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

import inttegro
from inttegro import APIError, LineItemType, ProductType

client = inttegro.InttegroClient(api_key=os.environ["INTTEGRO_API_KEY"])

try:
    request = inttegro.orders.CreateRequest(
        request_meta=inttegro.orders.RequestMeta(
            idempotency_key="checkout-cart-123",
        ),
        customer_data=inttegro.orders.Customer(
            name="Akua Mensah",
            email_address="akua@example.com",
            phone_number="+233544998605",
        ),
        finalize=True,
        checkout_settings=inttegro.orders.CheckoutSettings(
            redirect_url="https://example.com/orders/complete",
            cancel_url="https://example.com/cart",
        ),
        line_items=[
            inttegro.orders.ProductLineItem(
                type=LineItemType.PRODUCT,
                product=inttegro.orders.Product(
                    type=ProductType.DIGITAL,
                    name="Monthly subscription",
                    quantity=1,
                    price=inttegro.orders.Money(currency="ghs", value=5000),
                ),
            ),
        ],
    )
    order = client.orders.create(request)

    checkout_url = order.invoice.format.web.url
    print(order.id, checkout_url)
except APIError as error:
    print(error.code, error.detail or str(error))
    raise
```

Amounts use integer minor units: `5000` GHS is GHS 50.00. Reuse the same idempotency key when retrying the same logical write. If you omit one, the SDK generates a UUIDv7 key for mutating calls.

## Work with the API

The SDK covers orders and checkout, customers, products and prices, purchase intents, payment methods, balances, payouts and refunds, notifications, files, application settings, keys, and country specifications. Resources use snake-case attributes such as `purchase_intents` and `payment_methods`.

Python-specific features:

- Standard-library-only runtime with no third-party dependencies.
- OpenAPI-generated, immutable request and response dataclasses with fully typed nested fields.
- Resource namespaces such as `inttegro.orders.CreateRequest` keep related request objects together.
- Backwards-compatible mapping access and `to_dict()` conversion on every response model.
- Backwards-compatible dictionary request payloads for integrations migrating to typed objects.
- JSON-compatible string enums for public API values.
- Configurable timeout, base URL, and injectable transport for tests or custom networking.
- Structured authentication, rate-limit, network, timeout, and API exceptions.

Request and response fields are available to editors, Pyright, and mypy without plugins:

```python
import os

import inttegro

client = inttegro.InttegroClient(api_key=os.environ["INTTEGRO_API_KEY"])

request = inttegro.refunds.CreateRequest(
    order_id="or_0123456789abcdefghijklmnopqrstuvwxyzABCD",
    reason=inttegro.RefundReason.REQUESTED_BY_CUSTOMER,
    line_items=[
        inttegro.refunds.LineItem(
            order_line_item_id="oli_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN",
            refund_amount=inttegro.refunds.Money(currency="ghs", value=2500),
        ),
    ],
)

response: inttegro.RefundResponse = client.refunds.create(request)
print(response.refund.id, response.refund.total.value)
```

See the [API reference](https://studio.inttegro.com/api-reference) for request fields and lifecycle rules, [errors](https://studio.inttegro.com/errors) for recovery guidance, and [idempotency](https://studio.inttegro.com/idempotency) for safe retries.

## Verify a release

The GitHub release for each version is the canonical record. It contains the exact wheel and source distribution uploaded to PyPI, SHA-256 checksums, and a Sigstore attestation tied to the source commit and release workflow.

```bash
sha256sum --check SHA256SUMS
gh attestation verify inttegro-2.1.0-py3-none-any.whl \
  --repo zebodotdev/inttegro-sdk-python
```

## Develop

```bash
poetry install
poetry run python -m unittest discover -s tests -p "test_*.py"
```
