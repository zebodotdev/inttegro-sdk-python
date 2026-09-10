import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from inttegro import Order, Payment, PaymentMethod, Product, PurchaseIntent


class ResourceSemanticsTest(unittest.TestCase):
    def test_payment_and_order_semantics(self) -> None:
        payment = Payment.from_dict(
            {
                "amount": {"currency": "ghs", "value": 1000},
                "id": "py_123",
                "initiated_at": "2026-09-09T12:00:00Z",
                "next_action": {"type": "redirect"},
                "statement_descriptor": "INTTEGRO",
                "status": "requires_action",
            }
        )
        order = Order.from_dict(
            {
                "customer": {"guest": False, "id": "cu_123", "name": "Ama"},
                "id": "or_123",
                "initiated_at": "2026-09-09T12:00:00Z",
                "payment": payment.to_dict(),
                "status": "requires_payment",
            }
        )

        self.assertTrue(payment.requires_action())
        self.assertFalse(payment.is_terminal())
        self.assertIsNotNone(payment.required_action())
        self.assertTrue(order.requires_payment())
        self.assertIsNotNone(order.required_payment_action())

    def test_catalog_and_payment_method_semantics(self) -> None:
        intent = PurchaseIntent.from_dict(
            {
                "allow_variants": False,
                "created_at": "2026-09-09T12:00:00Z",
                "id": "sale_123",
                "quantity": {"min": 1},
                "status": "used",
                "usage": {
                    "order": {
                        "created_at": "2026-09-09T12:01:00Z",
                        "id": "or_123",
                    },
                    "single_use": True,
                },
            }
        )
        product = Product.from_dict(
            {
                "active": True,
                "created_at": "2026-09-09T12:00:00Z",
                "id": "prod_123",
                "name": "Tea guide",
                "published_at": "2026-09-09T12:00:00Z",
                "type": "digital",
            }
        )
        method = PaymentMethod.from_dict(
            {
                "active": True,
                "created_at": "2026-09-09T12:00:00Z",
                "customer_id": "cu_123",
                "id": "pm_123",
                "type": "mobile_money",
                "verified_at": "2026-09-09T12:00:00Z",
            }
        )

        self.assertTrue(intent.is_single_use())
        self.assertEqual(intent.used_order_id(), "or_123")
        self.assertTrue(product.is_published())
        self.assertTrue(product.was_ever_published())
        self.assertTrue(method.is_verified())
        self.assertTrue(method.is_reusable())


if __name__ == "__main__":
    unittest.main()
