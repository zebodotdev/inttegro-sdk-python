import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import inttegro


class PackageLayoutTest(unittest.TestCase):
    def test_main_resources_live_in_singular_namespaces(self) -> None:
        resources = {
            "app": "App",
            "balance": "Balance",
            "balance_transaction": "BalanceTransaction",
            "bank_account": "BankAccount",
            "broadcast": "Broadcast",
            "chime": "Chime",
            "customer": "Customer",
            "file": "File",
            "file_link": "FileLink",
            "financial_account": "FinancialAccount",
            "message_template": "MessageTemplate",
            "order": "Order",
            "payment": "Payment",
            "payment_method": "PaymentMethod",
            "payout": "Payout",
            "price": "Price",
            "product": "Product",
            "purchase_intent": "PurchaseIntent",
            "refund": "Refund",
            "schedule": "Schedule",
            "secret_key": "SecretKey",
            "upload_request": "UploadRequest",
            "wallet": "Wallet",
        }

        for package_name, class_name in resources.items():
            package = getattr(inttegro, package_name)
            resource = getattr(package, class_name)
            self.assertEqual(
                f"inttegro.{package_name}.{package_name}",
                resource.__module__,
            )

    def test_flat_resource_types_and_plural_facades_are_absent(self) -> None:
        for name in ("Payment", "Product", "ProductType", "RefundStatus", "CatalogPrice"):
            self.assertFalse(hasattr(inttegro, name), name)

        package_root = ROOT / "src" / "inttegro"
        for filename in ("payments.py", "products.py", "refunds.py", "wallets.py"):
            self.assertFalse((package_root / filename).exists(), filename)

    def test_monolithic_definition_modules_are_gone(self) -> None:
        package_root = ROOT / "src" / "inttegro"
        for filename in ("_models.py", "_enums.py", "request_types.py"):
            self.assertFalse((package_root / filename).exists(), filename)


if __name__ == "__main__":
    unittest.main()
