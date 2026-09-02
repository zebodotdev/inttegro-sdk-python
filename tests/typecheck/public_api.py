from inttegro import CreateRefundRequest, InttegroClient, RefundResponse


def refund(client: InttegroClient) -> tuple[str, int]:
    request: CreateRefundRequest = {
        "order_id": "or_0123456789abcdefghijklmnopqrstuvwxyzABCD",
        "reason": "requested_by_customer",
        "line_items": [
            {
                "order_line_item_id": "oli_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN",
                "refund_amount": {"currency": "ghs", "value": 2500},
            }
        ],
    }
    response: RefundResponse = client.refunds.create(request)
    invalid_request: CreateRefundRequest = {  # type: ignore[typeddict-item]
        "order_id": "or_0123456789abcdefghijklmnopqrstuvwxyzABCD"
    }
    wrong_response: str = client.refunds.create(request)  # type: ignore[assignment]
    wrong_total: str = response.refund.total.value  # type: ignore[assignment]
    del invalid_request, wrong_response, wrong_total
    return response.refund.id, response.refund.total.value
