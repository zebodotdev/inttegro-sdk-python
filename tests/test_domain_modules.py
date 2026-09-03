import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from inttegro import (
    CatalogPrice,
    CatalogPriceParams,
    Currency,
    Price,
    PriceParams,
    bank_accounts,
    chimes,
    orders,
    payment_methods,
    payments,
    products,
    purchase_intents,
    wallets,
)
from inttegro.money import Amount


class DomainModuleTest(unittest.TestCase):
    def test_amount_and_price_types_preserve_request_and_response_shapes(self) -> None:
        price = PriceParams(currency=Currency.GHS, value=3005)
        catalog_params = CatalogPriceParams(amount=price, label="Retail")
        catalog_price = CatalogPrice.from_dict(
            {
                "id": "pr_123",
                "active": True,
                "nominal": {"currency": "ghs", "value": 3005},
                "product_id": "prod_123",
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
        self.assertEqual("prod_123", catalog_price.product_id)
        self.assertEqual(Currency.EUR, inline_price.currency)
        self.assertEqual(Currency.GHS, Currency("GHS"))
        self.assertIs(PriceParams, purchase_intents.NominalPrice)

    def test_payments_module_exposes_payment_lifecycle_types(self) -> None:
        payment = payments.Payment.from_dict(
            {"id": "py_1", "status": "initiated", "amount": {"currency": "ghs", "value": 5000}}
        )

        self.assertEqual("py_1", payment.id)
        self.assertEqual(5000, payment.amount.value)
        self.assertEqual("initiated", payments.PaymentStatus.INITIATED.value)
        self.assertEqual("mobile_money", payment_methods.PaymentMethodType.MOBILE_MONEY.value)
        self.assertEqual("product", orders.LineItemType.PRODUCT.value)
        self.assertEqual("digital", products.ProductType.DIGITAL.value)

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
        self.assertEqual("sms", chimes.ChimeTransport.SMS.value)

    def test_financial_account_variants_have_focused_modules(self) -> None:
        wallet = wallets.Wallet.from_dict(
            {
                "id": "wallet_1",
                "type": "mobile_money",
                "mobile_money": {"account_number": "233200000000", "network": "mtn"},
            }
        )
        bank_account = bank_accounts.BankAccount.from_dict(
            {
                "type": "ghana_bank_account",
                "ghana_bank_account": {
                    "number": "0123456789",
                    "holder": {
                        "name": "Yaw Boakye",
                        "address": {
                            "country": "GH",
                            "city": "Accra",
                            "line_1": "1 Independence Avenue",
                            "region": "Greater Accra",
                        },
                    },
                },
            }
        )

        self.assertEqual("mtn", wallet.mobile_money.network)
        self.assertEqual("0123456789", bank_account.ghana_bank_account.number)

        bank_params = bank_accounts.Params(
            type=bank_accounts.BankAccountType.GHANA_BANK_ACCOUNT,
            ghana_bank_account=bank_accounts.GhanaBankAccountParams(
                number="0123456789",
                sort_code="010100",
                holder=bank_accounts.OwnerParams(
                    name="Yaw Boakye",
                    address=bank_accounts.OwnerAddressParams(country="GH"),
                ),
            ),
        )
        self.assertEqual(
            "0123456789",
            bank_params.to_dict()["ghana_bank_account"]["number"],
        )


if __name__ == "__main__":
    unittest.main()
