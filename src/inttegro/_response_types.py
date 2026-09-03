"""Endpoint-to-domain-model registry used to hide HTTP response envelopes."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from . import _models as m


@dataclass(frozen=True, slots=True)
class ResponseShape:
    model: Any
    field: str | None = None


def _resource(model: Any, field: str) -> ResponseShape:
    return ResponseShape(model=model, field=field)


RESPONSE_TYPES_BY_PATH: dict[str, ResponseShape] = {
    '/apps/create': _resource(m.Application, 'app'), '/apps/lookup': _resource(m.Application, 'app'), '/apps/update': _resource(m.Application, 'app'),
    '/balance_transactions/lookup': _resource(m.BalanceTransaction, 'transaction'), '/balance_transactions/page': _resource(m.BalanceTransactionPage, 'page'), '/balances': _resource(dict[str, m.CurrencyBalanceSnapshot], 'balances'),
    '/broadcasts/cancel': _resource(m.BroadcastDetail, 'broadcast'), '/broadcasts/lookup': _resource(m.BroadcastDetail, 'broadcast'),
    '/chimes/broadcast': _resource(m.BroadcastCreationDetail, 'broadcast'), '/chimes/lookup': _resource(m.Chime, 'chime'), '/chimes/page': _resource(m.ChimePage, 'page'), '/chimes/schedule': _resource(m.ScheduleCreationDetail, 'scheduled_chime'), '/chimes/send': _resource(m.Chime, 'chime'),
    '/customers/create': _resource(m.Customer, 'customer'), '/customers/lookup': _resource(m.Customer, 'customer'), '/customers/page': _resource(m.CustomerPage, 'page'), '/customers/update': _resource(m.Customer, 'customer'),
    '/file_links/create': ResponseShape(m.FileLinkCreation), '/file_links/lookup': _resource(m.FileLink, 'file_link'), '/file_links/page': _resource(m.FileLinkPage, 'page'), '/file_links/revoke': _resource(m.FileLink, 'file_link'),
    '/file_references/reconcile': ResponseShape(m.FileReferenceReconciliation), '/files/create': _resource(m.File, 'file'), '/files/delete': _resource(m.File, 'file'), '/files/lookup': _resource(m.File, 'file'), '/files/page': _resource(m.FilePage, 'page'),
    '/financial_accounts/archive': _resource(m.FinancialAccount, 'account'), '/financial_accounts/connect': _resource(m.FinancialAccount, 'account'), '/financial_accounts/create': _resource(m.FinancialAccount, 'account'),
    '/financial_accounts/disable_pull': _resource(m.FinancialAccount, 'account'), '/financial_accounts/disable_push': _resource(m.FinancialAccount, 'account'), '/financial_accounts/disconnect': _resource(m.FinancialAccount, 'account'),
    '/financial_accounts/enable_pull': _resource(m.FinancialAccount, 'account'), '/financial_accounts/enable_push': _resource(m.FinancialAccount, 'account'), '/financial_accounts/lookup': _resource(m.FinancialAccount, 'account'),
    '/financial_accounts/page': _resource(m.FinancialAccountPage, 'page'), '/financial_accounts/reconnect': _resource(m.FinancialAccount, 'account'), '/financial_accounts/update': _resource(m.FinancialAccount, 'account'), '/financial_accounts/verify': _resource(m.FinancialAccount, 'account'),
    '/keys/destroy': _resource(m.SecretKey, 'key'), '/keys/generate': _resource(m.GeneratedSecretKey, 'key'), '/keys/lookup': _resource(m.SecretKey, 'key'), '/keys/page': _resource(m.SecretKeyPage, 'page'), '/keys/update': _resource(m.SecretKey, 'key'), '/keys/usage': ResponseShape(m.SecretKeyUsage),
    '/message_templates/archive': _resource(m.MessageTemplate, 'message_template'), '/message_templates/create': _resource(m.MessageTemplate, 'message_template'), '/message_templates/lookup': _resource(m.MessageTemplate, 'message_template'),
    '/message_templates/page': _resource(m.MessageTemplatesPage, 'page'), '/message_templates/publish': _resource(m.MessageTemplate, 'message_template'), '/message_templates/render_preview': ResponseShape(m.MessageTemplatePreview), '/message_templates/update': _resource(m.MessageTemplate, 'message_template'),
    '/orders/cancel': _resource(m.Order, 'order'), '/orders/complete': _resource(m.Order, 'order'), '/orders/confirm_payment': _resource(m.Order, 'order'), '/orders/create': _resource(m.Order, 'order'), '/orders/finalize': _resource(m.Order, 'order'),
    '/orders/lookup': _resource(m.Order, 'order'), '/orders/new': _resource(m.Order, 'order'), '/orders/page': _resource(m.OrderPage, 'page'), '/orders/pay': _resource(m.Order, 'order'), '/orders/refund': _resource(m.Refund, 'refund'),
    '/orders/request_confirmation': _resource(m.Order, 'order'), '/orders/send_invoice': ResponseShape(m.OrderDocumentDeliveryResult), '/orders/send_receipt': ResponseShape(m.OrderDocumentDeliveryResult), '/orders/update': _resource(m.Order, 'order'),
    '/otp/cancel': _resource(m.OTPTransaction, 'transaction'), '/otp/initiate': _resource(m.OTPTransaction, 'transaction'), '/otp/lookup': _resource(m.OTPTransaction, 'transaction'), '/otp/verify': ResponseShape(m.OTPVerification),
    '/payment_methods/activate': _resource(m.PaymentMethod, 'payment_method'), '/payment_methods/archive': _resource(m.PaymentMethod, 'payment_method'), '/payment_methods/confirm_verification': _resource(m.PaymentMethod, 'payment_method'),
    '/payment_methods/delete': ResponseShape(m.PaymentMethodDeletion), '/payment_methods/disactivate': _resource(m.PaymentMethod, 'payment_method'), '/payment_methods/lookup': _resource(m.PaymentMethod, 'payment_method'),
    '/payment_methods/page': _resource(m.PaymentMethodPage, 'page'), '/payment_methods/settings': _resource(m.PaymentMethodSettings, 'settings'), '/payment_methods/tokenize': _resource(m.PaymentMethod, 'payment_method'),
    '/payment_methods/unarchive': _resource(m.PaymentMethod, 'payment_method'), '/payment_methods/update': _resource(m.PaymentMethod, 'payment_method'), '/payment_methods/verify': _resource(m.PaymentMethodVerificationSession, 'verification'),
    '/payouts/cancel': _resource(m.Payout, 'payout'), '/payouts/disable': _resource(m.PayoutSettingsMutation, 'settings'), '/payouts/disable_fx': _resource(m.PayoutSettingsLookup, 'settings'),
    '/payouts/enable': _resource(m.PayoutSettingsMutation, 'settings'), '/payouts/enable_fx': _resource(m.PayoutSettingsLookup, 'settings'), '/payouts/lookup': _resource(m.Payout, 'payout'), '/payouts/page': _resource(m.PayoutPage, 'page'),
    '/payouts/schedule': _resource(m.Payout, 'payout'), '/payouts/set_destinations': _resource(m.PayoutSettingsMutation, 'settings'), '/payouts/settings': _resource(m.PayoutSettingsLookup, 'settings'),
    '/prices/activate': _resource(m.Price, 'price'), '/prices/archive': _resource(m.Price, 'price'), '/prices/create': _resource(m.Price, 'price'), '/prices/deactivate': _resource(m.Price, 'price'), '/prices/lookup': _resource(m.Price, 'price'), '/prices/page': _resource(m.PricePage, 'page'), '/prices/update': _resource(m.Price, 'price'),
    '/products/add_price': _resource(m.ProductPriceNominal, 'price'), '/products/archive': _resource(m.Product, 'product'), '/products/create': _resource(m.Product, 'product'), '/products/lookup': _resource(m.Product, 'product'),
    '/products/page': _resource(m.ProductPage, 'page'), '/products/publish': _resource(m.Product, 'product'), '/products/set_default_unit_price': _resource(m.Product, 'product'), '/products/unpublish': _resource(m.Product, 'product'), '/products/update': _resource(m.Product, 'product'),
    '/purchase_intents/cancel': _resource(m.PurchaseIntent, 'purchase_intent'), '/purchase_intents/create': _resource(m.PurchaseIntent, 'purchase_intent'), '/purchase_intents/lookup': _resource(m.PurchaseIntent, 'purchase_intent'), '/purchase_intents/page': _resource(m.PurchaseIntentPage, 'page'), '/purchase_intents/update': _resource(m.PurchaseIntent, 'purchase_intent'),
    '/refunds/cancel': _resource(m.Refund, 'refund'), '/refunds/create': _resource(m.Refund, 'refund'), '/refunds/lookup': _resource(m.Refund, 'refund'), '/refunds/page': _resource(m.RefundPage, 'page'),
    '/schedules/cancel': _resource(m.ScheduleCancelDetail, 'scheduled_chime'), '/schedules/lookup': _resource(m.ScheduleDetail, 'scheduled_chime'), '/spec/countries': _resource(dict[str, m.CountrySpecification], 'countries'),
    '/upload_requests/cancel': _resource(m.UploadRequest, 'upload_request'), '/upload_requests/create': _resource(m.UploadRequest, 'upload_request'), '/upload_requests/lookup': _resource(m.UploadRequest, 'upload_request'),
    '/upload_requests/page': _resource(m.UploadRequestPage, 'page'), '/upload_requests/review': _resource(m.UploadRequest, 'upload_request'), '/upload_requests/upload': ResponseShape(m.UploadFulfillment),
}


def response_type_for_path(path: str) -> ResponseShape | None:
    return RESPONSE_TYPES_BY_PATH.get(path)
