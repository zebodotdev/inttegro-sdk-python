"""Typed string constants for enums published by the Inttegro API."""

from enum import Enum


class WireEnum(str, Enum):
    """A JSON-compatible string enum used on the Inttegro API wire."""

    def __str__(self) -> str:
        return str(self.value)


class AppManagementRole(WireEnum):
    PARENT = "parent"
    CHILD = "child"


class AppCredentialOwner(WireEnum):
    CHILD = "child"
    PARENT = "parent"


class AppRelationshipKind(WireEnum):
    PLACEMENT = "placement"


class AppRelationshipStatus(WireEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"
    REVOKED = "revoked"


class SecretKeyTokenType(WireEnum):
    BEARER = "bearer"


class SecretKeyStatus(WireEnum):
    ACTIVE = "active"
    REVOKED = "revoked"
    EXPIRED = "expired"


class SecretKeyAuthResult(WireEnum):
    SUCCEEDED = "succeeded"
    FAILED = "failed"


class FileStatus(WireEnum):
    UPLOADING = "uploading"
    PROCESSING = "processing"
    AVAILABLE = "available"
    FAILED = "failed"
    DELETED = "deleted"


class FileDisposition(WireEnum):
    ATTACHMENT = "attachment"
    INLINE = "inline"


class FileDelivery(WireEnum):
    STREAM = "stream"
    REDIRECT = "redirect"


class FileScanStatus(WireEnum):
    PENDING = "pending"
    PASSED = "passed"
    FAILED = "failed"
    SKIPPED = "skipped"


class FileSourceType(WireEnum):
    DIRECT = "direct"
    UPLOAD_REQUEST = "upload_request"
    SERVICE = "service"


class FileStorageEncoding(WireEnum):
    IDENTITY = "identity"
    BROTLI = "br"


class FileLinkStatus(WireEnum):
    ACTIVE = "active"
    REVOKED = "revoked"
    EXPIRED = "expired"
    DISABLED = "disabled"


class FileLinkKind(WireEnum):
    PUBLIC = "public"


class FileLinkDeliveryMode(WireEnum):
    REDIRECT = "redirect"
    DOWNLOAD = "download"
    INLINE = "inline"


class UploadRequestStatus(WireEnum):
    PENDING = "pending"
    UPLOADING = "uploading"
    FULFILLED = "fulfilled"
    EXPIRED = "expired"
    CANCELED = "canceled"
    FAILED = "failed"


class UploadReviewDecision(WireEnum):
    APPROVED = "approved"
    REJECTED = "rejected"


class UploadReviewType(WireEnum):
    AUTOMATIC = "automatic"
    MANUAL = "manual"


class PaymentNextActionType(WireEnum):
    CONFIRM_PAYMENT = "confirm_payment"
    EXECUTE = "execute"
    REDIRECT = "redirect"
    AUTHORIZE = "authorize"
    NONE = "none"


class PaymentConfirmationChannel(WireEnum):
    SMS = "sms"
    EMAIL = "email"
    PUSH = "push"


class PaymentMethodType(WireEnum):
    MOBILE_MONEY = "mobile_money"
    BANK_ACCOUNT = "bank_account"
    CARD = "card"
    MOTITO = "motito"


class MobileMoneyNetwork(WireEnum):
    AIRTEL = "airtel"
    MTN = "mtn"
    TELECEL = "telecel"
    VODAFONE = "vodafone"


class ProductType(WireEnum):
    PHYSICAL = "physical"
    DIGITAL = "digital"
    SERVICE = "service"
    VOUCHER = "voucher"
    CUSTOM = "custom"
    CAUSE = "cause"


class ProductShipmentType(WireEnum):
    DELIVERY = "delivery"
    DOWNLOAD = "download"
    RENDER = "render"
    SERVICE = "service"
    STREAM = "stream"


class ProductShipmentInputType(WireEnum):
    DELIVERY = "delivery"
    DOWNLOAD = "download"
    RENDER = "render"
    STREAM = "stream"


class LineItemType(WireEnum):
    PRODUCT = "product"
    FEE = "fee"
    SHIPPING = "shipping"


class PurchaseIntentStatus(WireEnum):
    ACTIVE = "active"
    EXPIRED = "expired"
    INACTIVE = "inactive"
    USED = "used"


class PurchaseIntentActivityType(WireEnum):
    EXPIRED_VIEWED = "expired_viewed"
    ORDER_CREATED = "order_created"
    PAYMENT_FAILED = "payment_failed"
    PAYMENT_STARTED = "payment_started"
    VIEWED = "viewed"


class FinancialAccountType(WireEnum):
    WALLET = "wallet"
    BANK_ACCOUNT = "bank_account"
    DOSH_ACCOUNT = "dosh_account"


class WalletType(WireEnum):
    MOBILE_MONEY = "mobile_money"


class BankAccountType(WireEnum):
    GHANA_BANK_ACCOUNT = "ghana_bank_account"


class MessageTemplateChannel(WireEnum):
    SMS = "sms"
    EMAIL = "email"


class MessageTemplateStatus(WireEnum):
    DRAFT = "draft"
    PUBLISHED = "published"
    ARCHIVED = "archived"


class MessageTemplateVariableType(WireEnum):
    STRING = "string"
    NUMBER = "number"
    INTEGER = "integer"
    BOOLEAN = "boolean"
    URL = "url"
    EMAIL = "email"
    PHONE = "phone"
    DATE = "date"
    DATETIME = "datetime"
    ARRAY = "array"


class MessageTemplateVariableItemType(WireEnum):
    STRING = "string"
    NUMBER = "number"
    INTEGER = "integer"
    BOOLEAN = "boolean"
    URL = "url"
    EMAIL = "email"
    PHONE = "phone"
    DATE = "date"
    DATETIME = "datetime"


class ContentSafetyStatus(WireEnum):
    ALLOWED = "allowed"
    REJECTED = "rejected"
    QUARANTINED = "quarantined"


class OrderDocumentKind(WireEnum):
    INVOICE = "invoice"
    RECEIPT = "receipt"


class DeliveryChannel(WireEnum):
    EMAIL = "email"
    SMS = "sms"


class CheckoutOrderStatus(WireEnum):
    PREPARING = "preparing"
    REQUIRES_PAYMENT = "requires_payment"
    COMPLETED = "completed"
    CANCELED = "canceled"
    EXPIRED = "expired"


class OrderStatus(WireEnum):
    PREPARING = "preparing"
    REQUIRES_PAYMENT = "requires_payment"
    PAID = "paid"
    COMPLETED = "completed"
    CANCELED = "canceled"
    EXPIRED = "expired"
    UNKNOWN = "unknown"


class OrderPaymentStatus(WireEnum):
    INITIATED = "initiated"
    REQUIRES_ACTION = "requires_action"
    OVERDUE = "overdue"
    EXECUTED = "executed"
    PAID = "paid"
    CANCELED = "canceled"
    EXPIRED = "expired"
    FAILED = "failed"
    UNKNOWN = "unknown"


class PaymentAttemptStatus(WireEnum):
    INITIATED = "initiated"
    EXECUTED = "executed"
    SUCCEEDED = "succeeded"
    CANCELED = "canceled"
    EXPIRED = "expired"
    FAILED = "failed"
    UNKNOWN = "unknown"


class CheckoutPaymentStatus(WireEnum):
    REQUIRES_ACTION = "requires_action"
    PROCESSING = "processing"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELLED = "cancelled"


class PaymentResultStatus(WireEnum):
    PENDING = "pending"
    REQUIRES_CONFIRMATION = "requires_confirmation"
    PROCESSING = "processing"
    SUCCEEDED = "succeeded"
    FAILED = "failed"


class OrderCreatedFromResourceType(WireEnum):
    PURCHASE_INTENT = "purchase_intent"


class RefundReason(WireEnum):
    REQUESTED_BY_CUSTOMER = "requested_by_customer"
    DUPLICATE = "duplicate"
    FRAUDULENT = "fraudulent"
    ORDER_CANCELED = "order_canceled"
    ITEM_RETURNED = "item_returned"
    ITEM_DAMAGED = "item_damaged"
    ITEM_NOT_RECEIVED = "item_not_received"
    ITEM_NOT_AS_DESCRIBED = "item_not_as_described"
    CUSTOM = "custom"


class RefundStatus(WireEnum):
    CANCELED = "canceled"
    FAILED = "failed"
    PENDING = "pending"
    PROCESSING = "processing"
    SUCCEEDED = "succeeded"


class BalanceTransactionType(WireEnum):
    PAYMENT = "payment"
    REFUND = "refund"


class PayoutStatus(WireEnum):
    INITIALIZED = "initialized"
    SCHEDULED = "scheduled"
    PROCESSING = "processing"
    EXECUTING = "executing"
    SUCCEEDED = "succeeded"
    INVALID = "invalid"
    CANCELED = "canceled"


class ChimeRecipientType(WireEnum):
    PHONE = "phone"
    EMAIL = "email"


class ChimeTransport(WireEnum):
    SMS = "sms"
    EMAIL = "email"


class ChimeEmailSchemaKind(WireEnum):
    GMAIL_VIEW_ACTION = "gmail_view_action"
    SCHEMA_ORG_ORDER = "schema_org_order"
    SCHEMA_ORG_INVOICE = "schema_org_invoice"


class OTPAlphabetType(WireEnum):
    NUMERIC = "numeric"
    ALPHA = "alpha"
    ALPHANUMERIC = "alphanumeric"


class OTPStatus(WireEnum):
    CANCELED = "canceled"
    EXPIRED = "expired"
    PENDING = "pending"
    PENDING_DELIVERY = "pending_delivery"
    PENDING_VERIFICATION = "pending_verification"
    VERIFIED = "verified"


class OTPTransmissionStatus(WireEnum):
    DELIVERED = "delivered"
    FAILED = "failed"
    SUBMITTED = "submitted"


class OTPVerificationVerdict(WireEnum):
    FAIL = "fail"
    PASS = "pass"


__all__ = [
    name
    for name, value in globals().items()
    if isinstance(value, type) and issubclass(value, WireEnum)
]
