import json
import sys
import unittest
from dataclasses import FrozenInstanceError, is_dataclass
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from inttegro import BalanceTransactionResponse, InttegroClient, RefundResponse


class StaticTransport:
    def __init__(self, body):
        self.body = body

    def __call__(self, request, timeout):
        del request, timeout
        return 200, {"content-type": "application/json"}, json.dumps(self.body)


class TypedModelTest(unittest.TestCase):
    def test_endpoint_returns_nested_dataclass_models(self):
        client = InttegroClient(
            api_key="test",
            transport=StaticTransport(
                {
                    "refund": {
                        "id": "rf_1",
                        "order_id": "or_1",
                        "reason": "requested_by_customer",
                        "status": "pending",
                        "total": {"currency": "ghs", "value": 2500},
                        "line_items": [],
                        "created_at": "2026-09-02T12:00:00Z",
                    }
                }
            ),
        )

        response = client.refunds.lookup("rf_1")

        self.assertIsInstance(response, RefundResponse)
        self.assertTrue(is_dataclass(response))
        self.assertEqual("rf_1", response.refund.id)
        self.assertEqual(2500, response.refund.total.value)
        self.assertEqual("rf_1", response["refund"]["id"])
        with self.assertRaises(FrozenInstanceError):
            response.refund.id = "rf_2"

    def test_models_preserve_unknown_fields_and_round_trip(self):
        response = RefundResponse.from_dict(
            {
                "refund": {
                    "id": "rf_1",
                    "order_id": "or_1",
                    "reason": "custom",
                    "status": "pending",
                    "total": {"currency": "ghs", "value": 100},
                    "line_items": [],
                    "created_at": "2026-09-02T12:00:00Z",
                    "future_field": {"enabled": True},
                },
                "request_id": "req_1",
            }
        )

        self.assertEqual({"enabled": True}, response.refund["future_field"])
        self.assertEqual("req_1", response["request_id"])
        self.assertEqual("req_1", response.to_dict()["request_id"])

    def test_absent_optional_fields_retain_presence_semantics(self):
        response = BalanceTransactionResponse.from_dict(
            {
                "transaction": {
                    "id": "bt_1",
                    "type": "payment",
                    "amount": {"currency": "ghs", "value": 100},
                    "created_at": "2026-09-02T12:00:00Z",
                }
            }
        )

        self.assertFalse(hasattr(response.transaction, "refund_id"))
        self.assertNotIn("refund_id", response.transaction)
