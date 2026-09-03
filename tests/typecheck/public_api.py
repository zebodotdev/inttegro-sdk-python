import inttegro
from inttegro import InttegroClient, Refund


def refund(client: InttegroClient) -> tuple[str, int]:
    request = inttegro.refunds.CreateRequest(
        order_id="or_0123456789abcdefghijklmnopqrstuvwxyzABCD",
        reason=inttegro.RefundReason.REQUESTED_BY_CUSTOMER,
        line_items=[
            inttegro.refunds.LineItem(
                order_line_item_id="oli_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN",
                refund_amount=inttegro.refunds.Money(currency="ghs", value=2500),
            )
        ],
    )
    response: Refund = client.refunds.create(request)
    invalid_request = inttegro.refunds.CreateRequest(  # type: ignore[call-arg]
        order_id="or_0123456789abcdefghijklmnopqrstuvwxyzABCD",
    )
    wrong_response: str = client.refunds.create(request)  # type: ignore[assignment]
    wrong_total: str = response.total.value  # type: ignore[assignment]
    del invalid_request, wrong_response, wrong_total
    return response.id, response.total.value


def create_order(client: InttegroClient) -> str:
    request = inttegro.orders.CreateRequest(
        customer_data=inttegro.orders.Customer(
            name="Akua Mensah",
            email_address="akua@example.com",
            phone_number="+233544998605",
        ),
        payment_method_data=inttegro.orders.PaymentMethod(
            type=inttegro.PaymentMethodType.MOBILE_MONEY,
            mobile_money=inttegro.orders.MobileMoney(
                network=inttegro.MobileMoneyNetwork.MTN,
                account_number="0544998605",
            ),
        ),
        line_items=[
            inttegro.orders.ProductLineItem(
                type=inttegro.LineItemType.PRODUCT,
                product=inttegro.orders.Product(
                    name="Monthly subscription",
                    price=inttegro.orders.Money(currency="ghs", value=5000),
                    quantity=1,
                    type=inttegro.ProductType.DIGITAL,
                ),
            )
        ],
    )
    return client.orders.create(request).id
