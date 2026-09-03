import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from inttegro import CatalogPrice, CatalogPriceParams, Currency, Price, PriceParams, chimes, payments
from inttegro.money import Amount, AmountParams


class DomainModuleTest(unittest.TestCase):
    def test_amount_and_price_types_preserve_request_and_response_shapes(self) -> None:
        price = PriceParams(currency=Currency.GHS, value=3005)
        catalog_params = CatalogPriceParams(amount=price, label="Retail")
        catalog_price = CatalogPrice.from_dict(
            {
                "id": "pr_123",
                "active": True,
                "nominal": {"currency": "ghs", "value": 3005},
                "created_at": "2026-09-02T12:00:00Z",
            }
        )
        inline_price = Price.from_dict({"currency": "eur", "value": 900})

        self.assertEqual({"currency": "ghs", "value": 3005}, price.to_dict())
        self.assertEqual(
            {"amount": {"currency": "ghs", "value": 3005}, "label": "Retail"},
            catalog_params.to_dict(),
        )
        self.assertIsInstance(catalog_price.nominal, Amount)
        self.assertEqual(Currency.GHS, catalog_price.nominal.currency)
        self.assertEqual(Currency.EUR, inline_price.currency)

    def test_payments_module_exposes_payment_lifecycle_types(self) -> None:
        payment = payments.Payment.from_dict(
            {"id": "py_1", "status": "initiated", "amount": {"currency": "ghs", "value": 5000}}
        )

        self.assertEqual("py_1", payment.id)
        self.assertEqual(5000, payment.amount.value)
        self.assertEqual("initiated", payments.PaymentStatus.INITIATED.value)

    def test_chimes_module_exposes_chimes_broadcasts_and_schedules(self) -> None:
        chime = chimes.Chime.from_dict({"id": "ch_1"})
        broadcast = chimes.Broadcast.from_dict(
            {
                "id": "br_1",
                "recipients": ["+233544998605"],
                "content": "Hello",
                "sender_id": "Inttegro",
                "send_after": "2026-09-03T12:00:00Z",
                "created_at": "2026-09-03T11:00:00Z",
            }
        )
        schedule = chimes.Schedule.from_dict(
            {
                "id": "sch_1",
                "recipients": ["+233544998605"],
                "content": "Hello later",
                "sender_id": "Inttegro",
                "send_after": "2026-09-04T12:00:00Z",
                "created_at": "2026-09-03T11:00:00Z",
            }
        )

        self.assertEqual("ch_1", chime.id)
        self.assertEqual("br_1", broadcast.id)
        self.assertEqual("sch_1", schedule.id)


if __name__ == "__main__":
    unittest.main()
