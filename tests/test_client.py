import json
import os
import re
import sys
import tempfile
import unittest
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from inttegro import AuthenticationError
from inttegro.client import InttegroClient


UUID_V7_RE = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-7[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$", re.I)


class TransportRecorder:
    def __init__(self):
        self.requests = []

    def __call__(self, req, timeout):
        self.requests.append(req)
        body = {}
        if req.data:
            try:
                body = json.loads(req.data.decode("utf-8"))
            except Exception:
                body = {}
        return 200, {"content-type": "application/json"}, json.dumps(body or {"ok": True})


class ErrorTransport:
    def __call__(self, req, timeout):
        return (
            401,
            {"content-type": "application/json"},
            json.dumps(
                {
                    "type": "authentication_error",
                    "code": "invalid_api_key",
                    "url": "https://studio.inttegro.com/e/invalid_api_key",
                    "message": "invalid key",
                    "detail": "API key is missing or invalid.",
                    "fix_code": "check_api_key",
                    "cause": "authentication_failure",
                }
            ),
        )


class BalanceTransactionTransport:
    def __call__(self, req, timeout):
        del timeout
        if urllib.parse.urlparse(req.full_url).path.endswith("/lookup"):
            body = {
                "transaction": {
                    "id": "bt_payment",
                    "type": "payment",
                    "payment_id": "py_123",
                    "order_id": "or_123",
                    "amount": {"currency": "GHS", "value": 2500},
                    "created_at": "2026-08-31T12:00:00Z",
                }
            }
        else:
            body = {
                "page": {
                    "number": 1,
                    "size": 1,
                    "transactions": [
                        {
                            "id": "bt_refund",
                            "type": "refund",
                            "refund_id": "rf_123",
                            "order_id": "or_123",
                            "amount": {"currency": "GHS", "value": 500},
                            "created_at": "2026-08-31T12:01:00Z",
                        }
                    ],
                }
            }
        return 200, {"content-type": "application/json"}, json.dumps(body)


OPENAPI_CAPABILITY_URL_PATHS = {
    "/file_links/open",
    "/upload_requests/upload",
}


def openapi_spec_path() -> Path:
    return Path(os.environ.get("INTTEGRO_OPENAPI_SPEC", "../../openapi/commerce.yml"))


def read_openapi_paths(path: Path) -> list[str]:
    paths = []
    in_paths = False
    with path.open("r", encoding="utf-8") as handle:
        for raw_line in handle:
            line = raw_line.rstrip("\n")
            stripped = line.strip()
            if not stripped or stripped == "---":
                continue
            if not in_paths:
                if stripped == "paths:":
                    in_paths = True
                continue
            if not line.startswith((" ", "\t")):
                break
            if line.startswith("    /"):
                path_key, separator, _ = stripped.partition(":")
                if not separator:
                    raise AssertionError(f"malformed OpenAPI path line: {line!r}")
                paths.append(path_key)
    if not in_paths:
        raise AssertionError(f"OpenAPI paths block not found in {path}")
    if not paths:
        raise AssertionError(f"OpenAPI paths block in {path} was empty")
    return paths


class InttegroClientTest(unittest.TestCase):
    def test_balance_transactions_expose_matching_semantic_sources(self):
        client = InttegroClient(
            api_key="test",
            base_url="https://api.inttegro.com",
            transport=BalanceTransactionTransport(),
        )

        payment = client.balance_transactions.lookup("bt_payment").transaction
        self.assertEqual("payment", payment.type)
        self.assertEqual("py_123", payment.payment_id)
        self.assertFalse(hasattr(payment, "refund_id"))
        self.assertEqual(2500, payment.amount.value)

        refund = client.balance_transactions.page({"page_number": 1}).page.transactions[0]
        self.assertEqual("refund", refund.type)
        self.assertEqual("rf_123", refund.refund_id)
        self.assertFalse(hasattr(refund, "payment_id"))

    def test_paths_cover_spec(self):
        recorder = TransportRecorder()
        client = InttegroClient(api_key="test", base_url="https://api.inttegro.com", transport=recorder)

        client.orders.create({"number": "1"})
        client.orders.new({"number": "2"})
        client.orders.lookup("or_1")
        client.orders.update({"order_id": "or_1", "number": "ORDER-1A"})
        client.orders.pay({"order_id": "or_1"})
        client.orders.confirm_payment({"order_id": "or_1", "token": "123456"})
        client.orders.request_confirmation("or_1")
        client.orders.cancel("or_1")
        client.orders.finalize("or_1")
        client.orders.complete({"order_id": "or_1"})
        client.orders.send_invoice({"order_id": "or_1"})
        client.orders.send_receipt({"order_id": "or_1"})
        client.orders.refund("or_1")
        client.orders.page({})

        client.payment_methods.tokenize({"type": "mobile_money"})
        client.payment_methods.verify("pm_1")
        client.payment_methods.confirm_verification({"payment_method_id": "pm_1", "token": "123456"})
        client.payment_methods.lookup("pm_1")
        client.payment_methods.page({})
        client.payment_methods.update({"payment_method_id": "pm_1", "active": True})
        client.payment_methods.activate("pm_1")
        client.payment_methods.disactivate("pm_1")
        client.payment_methods.archive("pm_1")
        client.payment_methods.unarchive("pm_1")
        client.payment_methods.delete("pm_1")
        client.payment_methods.settings()

        client.payouts.schedule({"destination_id": "fa_1", "max_amount": 100, "reference": "PAYOUT-1"})
        client.payouts.lookup("po_1")
        client.payouts.set_destinations({"ghs": "dest"})
        client.payouts.settings()
        client.payouts.disable_automatic()
        client.payouts.enable_automatic()
        client.payouts.enable_fx()
        client.payouts.disable_fx()
        client.payouts.page({})
        client.payouts.cancel("po_1")

        client.balance_transactions.lookup("bt_1")
        client.balance_transactions.page({})

        client.financial_accounts.create({"name": "Account"})
        client.financial_accounts.lookup("fa_1")
        client.financial_accounts.archive({"account_id": "fa_1"})
        client.financial_accounts.page({})
        client.financial_accounts.verify({"account_id": "fa_1"})
        client.financial_accounts.connect({"name": "Account"})
        client.financial_accounts.update({"account_id": "fa_1", "label": "Updated"})
        client.financial_accounts.enable_push("fa_1")
        client.financial_accounts.disable_push("fa_1", unset_as_payout_destination=True)
        client.financial_accounts.disconnect("fa_1", unset_as_payout_destination=True)
        client.financial_accounts.reconnect("fa_1")
        client.financial_accounts.enable_pull("fa_1")
        client.financial_accounts.disable_pull("fa_1")

        client.customers.create({"name": "Jane Doe"})
        client.customers.lookup("cu_1")
        client.customers.update({"customer_id": "cu_1", "name": "Jane Smith"})
        client.customers.page({"page_number": 1})

        client.products.create({"type": "physical", "name": "Product"})
        client.products.add_price({
            "product_id": "prod_1",
            "amount": {"currency": "ghs", "value": 5000},
            "set_as_default": True,
        })
        client.products.set_default_unit_price({"product_id": "prod_1", "price_id": "pr_1"})
        client.products.lookup("prod_1")
        client.products.update({"product_id": "prod_1", "name": "Updated"})
        client.products.publish("prod_1")
        client.products.unpublish("prod_1")
        client.products.archive("prod_1")
        client.products.page({"page_number": 1})

        client.chimes.send({"message": "hi"})
        client.chimes.lookup("ch_1")
        client.chimes.page({})
        client.chimes.schedule({
            "recipients": ["+233544998605"],
            "full_message": "later",
            "send_after": "2026-01-18T10:00:00Z",
        })
        client.chimes.broadcast({
            "recipients": ["+233544998605"],
            "message_template": "hello",
            "service_name": "marketing",
        })

        client.schedules.lookup("sch_1")
        client.schedules.cancel("sch_1")
        client.broadcasts.lookup("brc_1")
        client.broadcasts.cancel("brc_1")

        client.message_templates.create({
            "name": "welcome_sms",
            "channel": "sms",
            "purpose": "marketing",
            "sms": {"message_template": "Welcome {{name}}"},
        })
        client.message_templates.update({"id": "mtpl_1", "name": "welcome_sms"})
        client.message_templates.publish("mtpl_1")
        client.message_templates.archive("mtpl_1")
        client.message_templates.lookup("mtpl_1")
        client.message_templates.page({})
        client.message_templates.render_preview({"message_template": {"template_id": "mtpl_1"}})

        client.otp.initiate({
            "recipient": "+233",
            "sender": "Acme",
            "service_name": "Acme Bank",
            "idempotency_key": "otp_login_1700000000",
        })
        client.otp.verify({"transaction_id": "txn_1", "recipient": "+233", "token": "123456"})
        client.otp.lookup({"transaction_id": "txn_1"})
        client.otp.cancel({"transaction_id": "txn_1", "reason": "test"})

        client.apps.create({"name": "My App"})
        client.apps.lookup()
        client.apps.update({"alias": "my-app"})

        client.keys.generate({"label": "Integration"})
        client.keys.page({})
        client.keys.lookup("sk_1")
        client.keys.update({"secret_key_id": "sk_1", "label": "Renamed"})
        client.keys.destroy("sk_1")
        client.keys.usage({"secret_key_id": "sk_1"})

        with tempfile.NamedTemporaryFile() as upload:
            upload.write(b"hello")
            upload.flush()
            client.files.create(file=upload.name, purpose="identity")
        client.files.lookup("file_1")
        client.files.page({})
        client.files.contents(file_id="file_1")
        client.files.delete("file_1")
        client.file_links.create({"file_id": "file_1"})
        client.file_links.lookup("fl_1")
        client.file_links.page({})
        client.file_links.revoke({"id": "fl_1"})
        client.upload_requests.create({"purpose": "identity"})
        client.upload_requests.lookup("ur_1")
        client.upload_requests.page({})
        client.upload_requests.cancel({"id": "ur_1"})
        client.upload_requests.review({"id": "ur_1", "attempt_id": "uat_1", "decision": "approved"})
        client.file_references.reconcile({"resource_type": "product", "resource_id": "prod_1"})

        client.purchase_intents.create({
            "product_id": "prod_1",
            "price_id": "pr_1",
            "quantity": {"min": 1, "max": 5},
        })
        client.purchase_intents.update({"id": "sale_1", "quantity": {"min": 1}})
        client.purchase_intents.cancel("sale_1")
        client.purchase_intents.lookup("sale_1")
        client.purchase_intents.page({"page_number": 1, "page_size": 20})

        client.prices.create({"currency": "ghs", "amount": 100})
        client.prices.lookup("pr_1")
        client.prices.page({})
        client.prices.update({"price_id": "pr_1", "label": "Updated"})
        client.prices.activate("pr_1")
        client.prices.deactivate("pr_1")
        client.prices.archive("pr_1")

        client.refunds.create({
            "order_id": "or_1",
            "reason": "requested_by_customer",
            "line_items": [{
                "order_line_item_id": "oli_1",
                "refund_amount": {"currency": "ghs", "value": 100},
            }],
        })
        client.refunds.cancel("rf_1")
        client.refunds.lookup("rf_1")
        client.refunds.page({"page_number": 1})

        client.spec.countries()
        client.balances.get()

        covered_paths = {urllib.parse.urlparse(req.full_url).path for req in recorder.requests}
        spec_path = openapi_spec_path()
        missing_paths = [
            path
            for path in read_openapi_paths(spec_path)
            if path not in covered_paths and path not in OPENAPI_CAPABILITY_URL_PATHS
        ]
        self.assertEqual([], missing_paths, f"Python SDK missing OpenAPI paths from {spec_path}")

        spec_paths = set(read_openapi_paths(spec_path))
        stale_exceptions = sorted(path for path in OPENAPI_CAPABILITY_URL_PATHS if path not in spec_paths)
        self.assertEqual([], stale_exceptions, "Python SDK OpenAPI coverage exceptions no longer exist in spec")

        # Response object wrapping
        resp = client.orders.create({"order": {"id": "or_123"}})
        self.assertEqual("or_123", resp.order["id"])

    def test_authentication_error_is_raised(self):
        client = InttegroClient(api_key="bad", base_url="https://api.inttegro.com", transport=ErrorTransport())

        with self.assertRaises(AuthenticationError):
            client.orders.lookup("or_1")

    def test_mutating_posts_generate_request_meta_idempotency_key(self):
        recorder = TransportRecorder()
        client = InttegroClient(api_key="test", base_url="https://api.inttegro.com", transport=recorder)

        client.orders.create({"number": "ORDER-1", "idempotency_key": "legacy"})

        body = json.loads(recorder.requests[0].data.decode("utf-8"))
        self.assertNotIn("idempotency_key", body)
        self.assertRegex(body["request_meta"]["idempotency_key"], UUID_V7_RE)

    def test_read_style_posts_do_not_generate_idempotency_metadata(self):
        recorder = TransportRecorder()
        client = InttegroClient(api_key="test", base_url="https://api.inttegro.com", transport=recorder)

        client.orders.lookup("or_1")

        body = json.loads(recorder.requests[0].data.decode("utf-8"))
        self.assertNotIn("request_meta", body)
        self.assertNotIn("idempotency_key", body)

    def test_message_templates_create_uses_request_meta_idempotency_by_default(self):
        recorder = TransportRecorder()
        client = InttegroClient(api_key="test", base_url="https://api.inttegro.com", transport=recorder)

        client.message_templates.create({
            "name": "welcome_sms",
            "channel": "sms",
            "purpose": "marketing",
            "sms": {"message_template": "Welcome {{name}}"},
        })

        request = recorder.requests[0]
        headers = {key.lower(): value for key, value in request.header_items()}
        body = json.loads(request.data.decode("utf-8"))
        self.assertNotIn("idempotency-key", headers)
        self.assertRegex(body["request_meta"]["idempotency_key"], UUID_V7_RE)


if __name__ == "__main__":
    unittest.main()
