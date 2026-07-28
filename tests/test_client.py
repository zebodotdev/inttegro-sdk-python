import json
import re
import sys
import unittest
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from commerce import AuthenticationError
from commerce.client import CommerceClient


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
                    "url": "https://commerce.zebo.dev/e/invalid_api_key",
                    "message": "invalid key",
                    "detail": "API key is missing or invalid.",
                    "fix_code": "check_api_key",
                    "cause": "authentication_failure",
                }
            ),
        )


class CommerceClientTest(unittest.TestCase):
    def test_paths_cover_spec(self):
        recorder = TransportRecorder()
        client = CommerceClient(api_key="test", base_url="https://api.zebo.dev", transport=recorder)

        client.orders.create({"number": "1"})
        client.orders.new({"number": "2"})
        client.orders.lookup("or_1")
        client.orders.pay({"order_id": "or_1"})
        client.orders.confirm_payment({"order_id": "or_1", "token": "123456"})
        client.orders.request_confirmation("or_1")
        client.orders.finalize("or_1")
        client.orders.send_invoice({"order_id": "or_1"})
        client.orders.send_receipt({"order_id": "or_1"})
        client.orders.complete({"order_id": "or_1"})
        client.orders.cancel("or_1")
        client.orders.refund("or_1")
        client.orders.page({})

        client.payment_methods.tokenize({"type": "mobile_money"})
        client.payment_methods.verify("pm_1")
        client.payment_methods.confirm_verification({"payment_method_id": "pm_1", "token": "123456"})
        client.payment_methods.lookup("pm_1")
        client.payment_methods.delete("pm_1")
        client.payment_methods.settings()

        client.payouts.set_destinations({"ghs": "dest"})
        client.payouts.settings()
        client.payouts.disable_automatic()
        client.payouts.enable_fx()
        client.payouts.disable_fx()
        client.payouts.page({})
        client.payouts.cancel("po_1")

        client.balance_transactions.page({})

        client.financial_accounts.create({"name": "Account"})
        client.financial_accounts.lookup("fa_1")
        client.financial_accounts.connect({"name": "Account"})
        client.financial_accounts.archive({"account_id": "fa_1"})
        client.financial_accounts.page({})
        client.financial_accounts.verify({"account_id": "fa_1"})
        client.financial_accounts.enable_push("fa_1")
        client.financial_accounts.disable_push("fa_1", unset_as_payout_destination=True)
        client.financial_accounts.enable_pull("fa_1")
        client.financial_accounts.disable_pull("fa_1")
        client.financial_accounts.disconnect("fa_1", unset_as_payout_destination=True)

        client.customers.create({"name": "Jane Doe"})
        client.customers.lookup("cu_1")
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

        client.spec.countries()
        client.balances.get()

        paths = [req.full_url for req in recorder.requests]
        expected_paths = [
            "/orders/new",
            "/orders/new",
            "/orders/lookup",
            "/orders/pay",
            "/orders/confirm_payment",
            "/orders/request_confirmation",
            "/orders/finalize",
            "/orders/send_invoice",
            "/orders/send_receipt",
            "/orders/complete",
            "/orders/cancel",
            "/orders/refund",
            "/orders/page",
            "/payment_methods/tokenize",
            "/payment_methods/verify",
            "/payment_methods/confirm_verification",
            "/payment_methods/lookup",
            "/payment_methods/delete",
            "/payment_methods/settings",
            "/payouts/set_destinations",
            "/payouts/settings",
            "/payouts/disable",
            "/payouts/enable_fx",
            "/payouts/disable_fx",
            "/payouts/page",
            "/payouts/cancel",
            "/balance_transactions/page",
            "/financial_accounts/create",
            "/financial_accounts/lookup",
            "/financial_accounts/connect",
            "/financial_accounts/archive",
            "/financial_accounts/page",
            "/financial_accounts/verify",
            "/financial_accounts/enable_push",
            "/financial_accounts/disable_push",
            "/financial_accounts/enable_pull",
            "/financial_accounts/disable_pull",
            "/financial_accounts/disconnect",
            "/customers/create",
            "/customers/lookup",
            "/customers/page",
            "/products/create",
            "/products/add_price",
            "/products/set_default_unit_price",
            "/products/lookup",
            "/products/update",
            "/products/publish",
            "/products/unpublish",
            "/products/archive",
            "/products/page",
            "/chimes/send",
            "/chimes/lookup",
            "/chimes/schedule",
            "/chimes/broadcast",
            "/schedules/lookup",
            "/schedules/cancel",
            "/broadcasts/lookup",
            "/broadcasts/cancel",
            "/otp/initiate",
            "/otp/verify",
            "/otp/lookup",
            "/otp/cancel",
            "/apps/create",
            "/apps/lookup",
            "/apps/update",
            "/spec/countries",
            "/balances",
        ]
        self.assertEqual(expected_paths, [urllib.parse.urlparse(p).path for p in paths])

        # Response object wrapping
        resp = client.orders.create({"order": {"id": "or_123"}})
        self.assertEqual("or_123", resp.order["id"])

    def test_authentication_error_is_raised(self):
        client = CommerceClient(api_key="bad", base_url="https://api.zebo.dev", transport=ErrorTransport())

        with self.assertRaises(AuthenticationError):
            client.orders.lookup("or_1")

    def test_mutating_posts_generate_request_meta_idempotency_key(self):
        recorder = TransportRecorder()
        client = CommerceClient(api_key="test", base_url="https://api.zebo.dev", transport=recorder)

        client.orders.create({"number": "ORDER-1", "idempotency_key": "legacy"})

        body = json.loads(recorder.requests[0].data.decode("utf-8"))
        self.assertNotIn("idempotency_key", body)
        self.assertRegex(body["request_meta"]["idempotency_key"], UUID_V7_RE)

    def test_read_style_posts_do_not_generate_idempotency_metadata(self):
        recorder = TransportRecorder()
        client = CommerceClient(api_key="test", base_url="https://api.zebo.dev", transport=recorder)

        client.orders.lookup("or_1")

        body = json.loads(recorder.requests[0].data.decode("utf-8"))
        self.assertNotIn("request_meta", body)
        self.assertNotIn("idempotency_key", body)

    def test_message_templates_create_uses_request_meta_idempotency_by_default(self):
        recorder = TransportRecorder()
        client = CommerceClient(api_key="test", base_url="https://api.zebo.dev", transport=recorder)

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
