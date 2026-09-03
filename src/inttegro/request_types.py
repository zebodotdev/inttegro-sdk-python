"""Generated immutable request objects. Do not edit by hand."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal, TypeAlias

from ._request_base import ApiRequest, UNSET, UnsetType
from .money import AmountParams
from .price_types import PriceParams
from ._enums import (
    AppCredentialOwner,
    AppManagementRole,
    BankAccountType,
    ChimeRecipientType,
    ChimeTransport,
    FileDelivery,
    FileDisposition,
    FileLinkDeliveryMode,
    FileLinkStatus,
    FileStatus,
    FinancialAccountType,
    LineItemType,
    MessageTemplateChannel,
    MessageTemplateStatus,
    MessageTemplateVariableItemType,
    MessageTemplateVariableType,
    MobileMoneyNetwork,
    OTPAlphabetType,
    PaymentMethodType,
    ProductShipmentInputType,
    ProductType,
    RefundReason,
    UploadRequestStatus,
    UploadReviewDecision,
    WalletType,
)

@dataclass(frozen=True, slots=True, kw_only=True)
class InitiateOTPRequest(ApiRequest):
    async_delivery: bool | UnsetType = field(default=UNSET)
    message_template: str | UnsetType = field(default=UNSET)
    purpose: str | UnsetType = field(default=UNSET)
    sender: str | UnsetType = field(default=UNSET)
    token_alphabet: str | UnsetType = field(default=UNSET)
    token_alphabet_type: Literal['numeric', 'alpha', 'alphanumeric', OTPAlphabetType.NUMERIC, OTPAlphabetType.ALPHA, OTPAlphabetType.ALPHANUMERIC] | UnsetType = field(default=UNSET)
    validity_duration_in_minutes: int | UnsetType = field(default=UNSET)
    recipient: str
    service_name: str
    token_size: int

@dataclass(frozen=True, slots=True, kw_only=True)
class VerifyOTPRequest(ApiRequest):
    transaction_id: str
    recipient: str
    token: str

@dataclass(frozen=True, slots=True, kw_only=True)
class LookupOTPRequest(ApiRequest):
    transaction_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class SendChimeRequest(ApiRequest):
    full_message: str | UnsetType = field(default=UNSET)
    email: ChimeEmailMessageInput | UnsetType = field(default=UNSET)
    message_template: MessageTemplateReferenceInput | UnsetType = field(default=UNSET)
    sender_id: str | UnsetType = field(default=UNSET)
    purpose: str | UnsetType = field(default=UNSET)
    custom_data: dict[str, str] | UnsetType = field(default=UNSET)
    request_meta: SendChimeRequestRequestMeta | UnsetType = field(default=UNSET)
    recipient: ChimeRecipientInput

@dataclass(frozen=True, slots=True, kw_only=True)
class ChimeInlineRecipientInputVariant1(ApiRequest):
    name: str | UnsetType = field(default=UNSET)
    phone: ChimeInlineRecipientInputVariant1Phone
    type: Literal['phone', ChimeRecipientType.PHONE]

@dataclass(frozen=True, slots=True, kw_only=True)
class ChimeInlineRecipientInputVariant1Phone(ApiRequest):
    number: str

@dataclass(frozen=True, slots=True, kw_only=True)
class ChimeInlineRecipientInputVariant2(ApiRequest):
    name: str | UnsetType = field(default=UNSET)
    email: ChimeInlineRecipientInputVariant2Email
    type: Literal['email', ChimeRecipientType.EMAIL]

@dataclass(frozen=True, slots=True, kw_only=True)
class ChimeInlineRecipientInputVariant2Email(ApiRequest):
    address: str

@dataclass(frozen=True, slots=True, kw_only=True)
class ChimeSavedCustomerRecipientInput(ApiRequest):
    customer_id: str
    transport: Literal['sms', 'email', ChimeTransport.SMS, ChimeTransport.EMAIL]

@dataclass(frozen=True, slots=True, kw_only=True)
class ChimeEmailMessageInput(ApiRequest):
    html: str | UnsetType = field(default=UNSET)
    reply_to: str | UnsetType = field(default=UNSET)
    headers: dict[str, str] | UnsetType = field(default=UNSET)
    subject: str
    text: str
    from_: ChimeEmailMailboxInput = field(metadata={'wire_name': 'from'})

@dataclass(frozen=True, slots=True, kw_only=True)
class ChimeEmailMailboxInput(ApiRequest):
    name: str | UnsetType = field(default=UNSET)
    address: str | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class MessageTemplateReferenceInput(ApiRequest):
    variables: MessageTemplateVariablesInput | UnsetType = field(default=UNSET)
    template_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class SendChimeRequestRequestMeta(ApiRequest):
    idempotency_key: str | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class LookupChimeRequest(ApiRequest):
    chime_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class PageChimesRequest(ApiRequest):
    customer_id: str | UnsetType = field(default=UNSET)
    page_number: int | UnsetType = field(default=UNSET)
    page_size: int | UnsetType = field(default=UNSET)
    recipient: str | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class ScheduleChimeRequest(ApiRequest):
    request_meta: ScheduleChimeRequestRequestMeta | UnsetType = field(default=UNSET)
    full_message: str | UnsetType = field(default=UNSET)
    email: ChimeEmailMessageInput | UnsetType = field(default=UNSET)
    message_template: MessageTemplateReferenceInput | UnsetType = field(default=UNSET)
    sender_id: str | UnsetType = field(default=UNSET)
    purpose: str | UnsetType = field(default=UNSET)
    recipients: list[ChimeRecipientInput]
    send_after: str

@dataclass(frozen=True, slots=True, kw_only=True)
class ScheduleChimeRequestRequestMeta(ApiRequest):
    idempotency_key: str | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class BroadcastRequest(ApiRequest):
    request_meta: BroadcastRequestRequestMeta | UnsetType = field(default=UNSET)
    message_template: str | MessageTemplateReferenceInput | UnsetType = field(default=UNSET)
    email: ChimeEmailMessageInput | UnsetType = field(default=UNSET)
    purpose: str | UnsetType = field(default=UNSET)
    sender: str | UnsetType = field(default=UNSET)
    recipients: list[ChimeRecipientInput]

@dataclass(frozen=True, slots=True, kw_only=True)
class BroadcastRequestRequestMeta(ApiRequest):
    idempotency_key: str | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class LookupScheduleRequest(ApiRequest):
    schedule_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class CancelScheduleRequest(ApiRequest):
    schedule_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class LookupBroadcastRequest(ApiRequest):
    broadcast_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class CancelBroadcastRequest(ApiRequest):
    broadcast_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class CreateSMSMessageTemplateRequest(ApiRequest):
    about: str | UnsetType = field(default=UNSET)
    locale: str | UnsetType = field(default=UNSET)
    variables: list[MessageTemplateVariableInput] | UnsetType = field(default=UNSET)
    channel: Literal['sms', MessageTemplateChannel.SMS]
    name: str
    purpose: str
    sms: MessageTemplateSMSContentInput

@dataclass(frozen=True, slots=True, kw_only=True)
class MessageTemplateSMSContentInput(ApiRequest):
    message_template: str

@dataclass(frozen=True, slots=True, kw_only=True)
class MessageTemplateVariableInput(ApiRequest):
    required: bool | UnsetType = field(default=UNSET)
    default: Any | UnsetType = field(default=UNSET)
    about: str | UnsetType = field(default=UNSET)
    items: list[MessageTemplateVariableItemInput] | UnsetType = field(default=UNSET)
    name: str
    type: Literal['string', 'number', 'integer', 'boolean', 'url', 'email', 'phone', 'date', 'datetime', 'array', MessageTemplateVariableType.STRING, MessageTemplateVariableType.NUMBER, MessageTemplateVariableType.INTEGER, MessageTemplateVariableType.BOOLEAN, MessageTemplateVariableType.URL, MessageTemplateVariableType.EMAIL, MessageTemplateVariableType.PHONE, MessageTemplateVariableType.DATE, MessageTemplateVariableType.DATETIME, MessageTemplateVariableType.ARRAY]

@dataclass(frozen=True, slots=True, kw_only=True)
class MessageTemplateVariableItemInput(ApiRequest):
    about: str | UnsetType = field(default=UNSET)
    default: Any | UnsetType = field(default=UNSET)
    required: bool | UnsetType = field(default=UNSET)
    name: str
    type: Literal['string', 'number', 'integer', 'boolean', 'url', 'email', 'phone', 'date', 'datetime', MessageTemplateVariableItemType.STRING, MessageTemplateVariableItemType.NUMBER, MessageTemplateVariableItemType.INTEGER, MessageTemplateVariableItemType.BOOLEAN, MessageTemplateVariableItemType.URL, MessageTemplateVariableItemType.EMAIL, MessageTemplateVariableItemType.PHONE, MessageTemplateVariableItemType.DATE, MessageTemplateVariableItemType.DATETIME]

@dataclass(frozen=True, slots=True, kw_only=True)
class CreateEmailMessageTemplateRequest(ApiRequest):
    about: str | UnsetType = field(default=UNSET)
    attachments: MessageTemplateAttachmentIDsInput | UnsetType = field(default=UNSET)
    locale: str | UnsetType = field(default=UNSET)
    variables: list[MessageTemplateVariableInput] | UnsetType = field(default=UNSET)
    channel: Literal['email', MessageTemplateChannel.EMAIL]
    email: MessageTemplateEmailContentInput
    name: str
    purpose: str

@dataclass(frozen=True, slots=True, kw_only=True)
class MessageTemplateEmailContentInput(ApiRequest):
    from_: MessageTemplateMailboxInput | UnsetType = field(default=UNSET, metadata={'wire_name': 'from'})
    reply_to: MessageTemplateMailboxInput | UnsetType = field(default=UNSET)
    headers: dict[str, str] | UnsetType = field(default=UNSET)
    subject: str
    html: str

@dataclass(frozen=True, slots=True, kw_only=True)
class MessageTemplateMailboxInput(ApiRequest):
    name: str | UnsetType = field(default=UNSET)
    address: str

@dataclass(frozen=True, slots=True, kw_only=True)
class UpdateMessageTemplateRequest(ApiRequest):
    name: str | UnsetType = field(default=UNSET)
    about: str | UnsetType = field(default=UNSET)
    channel: Literal['sms', 'email', MessageTemplateChannel.SMS, MessageTemplateChannel.EMAIL] | UnsetType = field(default=UNSET)
    purpose: str | UnsetType = field(default=UNSET)
    locale: str | UnsetType = field(default=UNSET)
    variables: list[MessageTemplateVariableInput] | UnsetType = field(default=UNSET)
    sms: MessageTemplateSMSContentInput | UnsetType = field(default=UNSET)
    email: MessageTemplateEmailContentInput | UnsetType = field(default=UNSET)
    attachments: MessageTemplateAttachmentIDsInput | UnsetType = field(default=UNSET)
    id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class MessageTemplateIDRequest(ApiRequest):
    id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class PageMessageTemplatesRequest(ApiRequest):
    page: int | UnsetType = field(default=UNSET)
    size: int | UnsetType = field(default=UNSET)
    status: Literal['draft', 'published', 'archived', MessageTemplateStatus.DRAFT, MessageTemplateStatus.PUBLISHED, MessageTemplateStatus.ARCHIVED] | UnsetType = field(default=UNSET)
    channel: Literal['sms', 'email', MessageTemplateChannel.SMS, MessageTemplateChannel.EMAIL] | UnsetType = field(default=UNSET)
    purpose: str | UnsetType = field(default=UNSET)
    locale: str | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class RenderMessageTemplatePreviewRequest(ApiRequest):
    message_template: MessageTemplateReferenceInput

@dataclass(frozen=True, slots=True, kw_only=True)
class CreateCustomerRequest(ApiRequest):
    billing_address: CustomerAddressInput | UnsetType = field(default=UNSET)
    custom_data: dict[str, Any] | UnsetType = field(default=UNSET)
    email_address: str | UnsetType = field(default=UNSET)
    phone_number: str | UnsetType = field(default=UNSET)
    reference: str | UnsetType = field(default=UNSET)
    shipping_address: CustomerAddressInput | UnsetType = field(default=UNSET)
    title: str | UnsetType = field(default=UNSET)
    name: str

@dataclass(frozen=True, slots=True, kw_only=True)
class CustomerAddressInput(ApiRequest):
    city: str | UnsetType = field(default=UNSET)
    line1: str | UnsetType = field(default=UNSET)
    line2: str | UnsetType = field(default=UNSET)
    name: str | UnsetType = field(default=UNSET)
    phone_number: str | UnsetType = field(default=UNSET)
    post_code: str | UnsetType = field(default=UNSET)
    region: str | UnsetType = field(default=UNSET)
    country: str

@dataclass(frozen=True, slots=True, kw_only=True)
class LookupCustomerRequest(ApiRequest):
    customer_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class UpdateCustomerRequest(ApiRequest):
    billing_address: CustomerAddressInput | UnsetType = field(default=UNSET)
    custom_data: dict[str, Any] | UnsetType = field(default=UNSET)
    email_address: str | UnsetType = field(default=UNSET)
    name: str | UnsetType = field(default=UNSET)
    phone_number: str | UnsetType = field(default=UNSET)
    reference: str | UnsetType = field(default=UNSET)
    shipping_address: CustomerAddressInput | UnsetType = field(default=UNSET)
    suffix: str | UnsetType = field(default=UNSET)
    title: str | UnsetType = field(default=UNSET)
    customer_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class PageCustomersRequest(ApiRequest):
    page_size: int | UnsetType = field(default=UNSET)
    page_number: int

@dataclass(frozen=True, slots=True, kw_only=True)
class CreateOrderNewCustomerInput(ApiRequest):
    number: str | UnsetType = field(default=UNSET)
    receipt_number: str | UnsetType = field(default=UNSET)
    statement_descriptor: str | UnsetType = field(default=UNSET)
    statement_descriptor_prefix: str | UnsetType = field(default=UNSET)
    execute_payment: bool | UnsetType = field(default=UNSET)
    finalize: bool | UnsetType = field(default=UNSET)
    request_meta: CreateOrderNewCustomerInputRequestMeta | UnsetType = field(default=UNSET)
    checkout_settings: CreateOrderNewCustomerInputCheckoutSettings | UnsetType = field(default=UNSET)
    invoice_settings: InvoiceSettingsInput | UnsetType = field(default=UNSET)
    payout_settings: OrderPayoutSettingsRequest | UnsetType = field(default=UNSET)
    custom_data: dict[str, str] | UnsetType = field(default=UNSET)
    billing_details: BillingDetailsInput | UnsetType = field(default=UNSET)
    shipping: ShippingInput | UnsetType = field(default=UNSET)
    payment_method_data: PaymentMethodDataInput | UnsetType = field(default=UNSET)
    customer_data: CustomerDataInput
    line_items: list[LineItemInput]

@dataclass(frozen=True, slots=True, kw_only=True)
class CustomerDataInput(ApiRequest):
    reference: str | UnsetType = field(default=UNSET)
    custom_data: dict[str, Any] | UnsetType = field(default=UNSET)
    name: str
    email_address: str
    phone_number: str

@dataclass(frozen=True, slots=True, kw_only=True)
class CreateOrderNewCustomerInputRequestMeta(ApiRequest):
    idempotency_key: str | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class CreateOrderNewCustomerInputCheckoutSettings(ApiRequest):
    redirect_url: str | UnsetType = field(default=UNSET)
    cancel_url: str | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class InvoiceSettingsInput(ApiRequest):
    number: str | UnsetType = field(default=UNSET)
    memo: str | UnsetType = field(default=UNSET)
    footer: str | UnsetType = field(default=UNSET)
    custom_data: dict[str, str] | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class OrderPayoutSettingsRequest(ApiRequest):
    destination: OrderPayoutSettingsRequestDestination | UnsetType = field(default=UNSET)
    enable_fx: Literal[False] | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class OrderPayoutSettingsRequestDestination(ApiRequest):
    financial_account_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class ProductLineItemInput(ApiRequest):
    type: Literal['product', LineItemType.PRODUCT]
    product: ProductDetailsInput

@dataclass(frozen=True, slots=True, kw_only=True)
class InlineProductDetailsInput(ApiRequest):
    about: str | UnsetType = field(default=UNSET)
    custom_data: dict[str, Any] | UnsetType = field(default=UNSET)
    reference: str | UnsetType = field(default=UNSET)
    tax_code: str | UnsetType = field(default=UNSET)
    name: str
    price: PriceParams
    quantity: int
    type: Literal['physical', 'digital', 'service', 'voucher', 'custom', 'cause', ProductType.PHYSICAL, ProductType.DIGITAL, ProductType.SERVICE, ProductType.VOUCHER, ProductType.CUSTOM, ProductType.CAUSE]

@dataclass(frozen=True, slots=True, kw_only=True)
class CatalogProductWithPriceDataInput(ApiRequest):
    price: PriceParams
    product_id: str
    quantity: int

@dataclass(frozen=True, slots=True, kw_only=True)
class CatalogProductWithPriceReferenceInput(ApiRequest):
    price_id: str
    product_id: str
    quantity: int

@dataclass(frozen=True, slots=True, kw_only=True)
class FeeLineItemInput(ApiRequest):
    type: Literal['fee', LineItemType.FEE]
    fee: FeeDetailsInput

@dataclass(frozen=True, slots=True, kw_only=True)
class FeeDetailsInput(ApiRequest):
    id: str | UnsetType = field(default=UNSET)
    label: str | UnsetType = field(default=UNSET)
    tax_code: str | UnsetType = field(default=UNSET)
    description: str | UnsetType = field(default=UNSET)
    custom_data: dict[str, Any] | UnsetType = field(default=UNSET)
    amount: AmountParams

@dataclass(frozen=True, slots=True, kw_only=True)
class ShippingLineItemInput(ApiRequest):
    type: Literal['shipping', LineItemType.SHIPPING]
    shipping: ShippingDetailsInput

@dataclass(frozen=True, slots=True, kw_only=True)
class ShippingDetailsInput(ApiRequest):
    id: str | UnsetType = field(default=UNSET)
    tax_code: str | UnsetType = field(default=UNSET)
    custom_data: dict[str, Any] | UnsetType = field(default=UNSET)
    fee: AmountParams

@dataclass(frozen=True, slots=True, kw_only=True)
class BillingDetailsInput(ApiRequest):
    address: AddressInput | UnsetType = field(default=UNSET)
    name: str
    email_address: str
    phone_number: str

@dataclass(frozen=True, slots=True, kw_only=True)
class AddressInput(ApiRequest):
    line2: str | UnsetType = field(default=UNSET)
    region: str | UnsetType = field(default=UNSET)
    district: str | UnsetType = field(default=UNSET)
    post_code: str | UnsetType = field(default=UNSET)
    name: str
    phone_number: str
    line1: str
    town: str
    country: str

@dataclass(frozen=True, slots=True, kw_only=True)
class ShippingInput(ApiRequest):
    address: AddressInput

@dataclass(frozen=True, slots=True, kw_only=True)
class CreateOrderExistingCustomerInput(ApiRequest):
    payment_method_id: str | UnsetType = field(default=UNSET)
    payment_method_data: PaymentMethodDataInput | UnsetType = field(default=UNSET)
    receipt_number: str | UnsetType = field(default=UNSET)
    statement_descriptor: str | UnsetType = field(default=UNSET)
    statement_descriptor_prefix: str | UnsetType = field(default=UNSET)
    execute_payment: bool | UnsetType = field(default=UNSET)
    finalize: bool | UnsetType = field(default=UNSET)
    request_meta: CreateOrderExistingCustomerInputRequestMeta | UnsetType = field(default=UNSET)
    checkout_settings: CreateOrderExistingCustomerInputCheckoutSettings | UnsetType = field(default=UNSET)
    invoice_settings: InvoiceSettingsInput | UnsetType = field(default=UNSET)
    payout_settings: OrderPayoutSettingsRequest | UnsetType = field(default=UNSET)
    custom_data: dict[str, str] | UnsetType = field(default=UNSET)
    billing_details: BillingDetailsInput | UnsetType = field(default=UNSET)
    shipping: ShippingInput | UnsetType = field(default=UNSET)
    customer_id: str
    line_items: list[LineItemInput]

@dataclass(frozen=True, slots=True, kw_only=True)
class CreateOrderExistingCustomerInputRequestMeta(ApiRequest):
    idempotency_key: str | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class CreateOrderExistingCustomerInputCheckoutSettings(ApiRequest):
    redirect_url: str | UnsetType = field(default=UNSET)
    cancel_url: str | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class LookupOrderRequest(ApiRequest):
    order_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class UpdateOrderRequest(ApiRequest):
    clear_payment_method: bool | UnsetType = field(default=UNSET)
    custom_data: dict[str, str] | UnsetType = field(default=UNSET)
    invoice_settings: InvoiceSettingsInput | UnsetType = field(default=UNSET)
    finalize: bool | UnsetType = field(default=UNSET)
    line_items: list[LineItemInput] | UnsetType = field(default=UNSET)
    number: str | UnsetType = field(default=UNSET)
    receipt_number: str | UnsetType = field(default=UNSET)
    payment_method_data: UpdateOrderRequestPaymentMethodData | UnsetType = field(default=UNSET)
    payment_method_id: str | UnsetType = field(default=UNSET)
    statement_descriptor: str | UnsetType = field(default=UNSET)
    statement_descriptor_prefix: str | UnsetType = field(default=UNSET)
    order_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class UpdateOrderRequestPaymentMethodData(ApiRequest):
    mobile_money: UpdateOrderRequestPaymentMethodDataMobileMoney | UnsetType = field(default=UNSET)
    type: Literal['mobile_money', PaymentMethodType.MOBILE_MONEY]

@dataclass(frozen=True, slots=True, kw_only=True)
class UpdateOrderRequestPaymentMethodDataMobileMoney(ApiRequest):
    network: Literal['airtel', 'mtn', 'telecel', 'vodafone', MobileMoneyNetwork.AIRTEL, MobileMoneyNetwork.MTN, MobileMoneyNetwork.TELECEL, MobileMoneyNetwork.VODAFONE]
    account_number: str

@dataclass(frozen=True, slots=True, kw_only=True)
class PayOrderRequest(ApiRequest):
    payment_method_data: PaymentMethodDataInput | UnsetType = field(default=UNSET)
    payment_method_id: str | UnsetType = field(default=UNSET)
    paid_out_of_band: bool | UnsetType = field(default=UNSET)
    order_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class PaymentMethodDataInput(ApiRequest):
    mobile_money: PaymentMethodDataInputMobileMoney | UnsetType = field(default=UNSET)
    type: Literal['mobile_money', PaymentMethodType.MOBILE_MONEY]

@dataclass(frozen=True, slots=True, kw_only=True)
class PaymentMethodDataInputMobileMoney(ApiRequest):
    network: Literal['airtel', 'mtn', 'telecel', 'vodafone', MobileMoneyNetwork.AIRTEL, MobileMoneyNetwork.MTN, MobileMoneyNetwork.TELECEL, MobileMoneyNetwork.VODAFONE]
    account_number: str

@dataclass(frozen=True, slots=True, kw_only=True)
class ConfirmPaymentRequest(ApiRequest):
    order_id: str
    payment_id: str
    confirmation_id: str
    token: str

@dataclass(frozen=True, slots=True, kw_only=True)
class RequestConfirmationRequest(ApiRequest):
    order_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class CancelOrderRequest(ApiRequest):
    reason: str | UnsetType = field(default=UNSET)
    execute_refund: bool | UnsetType = field(default=UNSET)
    order_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class FinalizeOrderRequest(ApiRequest):
    order_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class CompleteOrderRequest(ApiRequest):
    paid_out_of_band: bool | UnsetType = field(default=UNSET)
    order_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class OrderDocumentDeliveryRequest(ApiRequest):
    order_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class PageOrdersRequest(ApiRequest):
    page_number: int | UnsetType = field(default=UNSET)
    customer_id: str | UnsetType = field(default=UNSET)
    page_size: int

@dataclass(frozen=True, slots=True, kw_only=True)
class CreateRefundRequest(ApiRequest):
    custom_data: dict[str, str] | UnsetType = field(default=UNSET)
    reason_details: str | UnsetType = field(default=UNSET)
    reference: str | UnsetType = field(default=UNSET)
    request_meta: RefundRequestMetaInput | UnsetType = field(default=UNSET)
    line_items: list[CreateRefundLineItemInput]
    order_id: str
    reason: RefundReasonInput

@dataclass(frozen=True, slots=True, kw_only=True)
class CreateRefundLineItemInput(ApiRequest):
    reason: RefundReasonInput | UnsetType = field(default=UNSET)
    reason_details: str | UnsetType = field(default=UNSET)
    order_line_item_id: str
    refund_amount: AmountParams

@dataclass(frozen=True, slots=True, kw_only=True)
class RefundRequestMetaInput(ApiRequest):
    idempotency_key: str | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class CancelRefundRequest(ApiRequest):
    request_meta: RefundRequestMetaInput | UnsetType = field(default=UNSET)
    refund_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class LookupRefundRequest(ApiRequest):
    refund_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class PageRefundsRequest(ApiRequest):
    page_size: int | UnsetType = field(default=UNSET)
    page_number: int

@dataclass(frozen=True, slots=True, kw_only=True)
class CreateApplicationRequest(ApiRequest):
    alias: str | UnsetType = field(default=UNSET)
    description: str | UnsetType = field(default=UNSET)
    legal_entity_type: str | UnsetType = field(default=UNSET)
    placement_parent_application_id: str | UnsetType = field(default=UNSET)
    relationship_policy: CreateApplicationRequestRelationshipPolicy | UnsetType = field(default=UNSET)
    name: str

@dataclass(frozen=True, slots=True, kw_only=True)
class CreateApplicationRequestRelationshipPolicy(ApiRequest):
    child_standing: str | UnsetType = field(default=UNSET)
    management: Literal['parent', 'child', AppManagementRole.PARENT, AppManagementRole.CHILD] | UnsetType = field(default=UNSET)
    credentials: Literal['child', 'parent', AppCredentialOwner.CHILD, AppCredentialOwner.PARENT] | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class UpdateApplicationRequest(ApiRequest):
    name: str | UnsetType = field(default=UNSET)
    alias: str | UnsetType = field(default=UNSET)
    description: str | UnsetType = field(default=UNSET)
    legal_entity_type: str | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class GenerateSecretKeyRequest(ApiRequest):
    label: str | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class PageSecretKeysRequest(ApiRequest):
    page: int | UnsetType = field(default=UNSET)
    number: int | UnsetType = field(default=UNSET)
    size: int | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class LookupSecretKeyRequest(ApiRequest):
    secret_key_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class UpdateSecretKeyRequest(ApiRequest):
    label: str
    secret_key_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class DestroySecretKeyRequest(ApiRequest):
    secret_key_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class SecretKeyUsageRequest(ApiRequest):
    number: int | UnsetType = field(default=UNSET)
    page: int | UnsetType = field(default=UNSET)
    size: int | UnsetType = field(default=UNSET)
    secret_key_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class FinancialAccountWalletRequest(ApiRequest):
    custom_data: dict[str, Any] | UnsetType = field(default=UNSET)
    description: str | UnsetType = field(default=UNSET)
    pull_configuration: FinancialAccountWalletRequestPullConfiguration | UnsetType = field(default=UNSET)
    push_configuration: FinancialAccountWalletRequestPushConfiguration | UnsetType = field(default=UNSET)
    currency: str
    label: str
    owner: FinancialAccountOwnerInput
    reference: str
    type: Literal['wallet', FinancialAccountType.WALLET]
    wallet: FinancialAccountWalletRequestWallet

@dataclass(frozen=True, slots=True, kw_only=True)
class FinancialAccountOwnerInput(ApiRequest):
    name: str
    address: FinancialAccountOwnerInputAddress

@dataclass(frozen=True, slots=True, kw_only=True)
class FinancialAccountOwnerInputAddress(ApiRequest):
    city: str | UnsetType = field(default=UNSET)
    line_1: str | UnsetType = field(default=UNSET)
    line_2: str | UnsetType = field(default=UNSET)
    name: str | UnsetType = field(default=UNSET)
    phone: str | UnsetType = field(default=UNSET)
    post_code: str | UnsetType = field(default=UNSET)
    region: str | UnsetType = field(default=UNSET)
    country: str

@dataclass(frozen=True, slots=True, kw_only=True)
class FinancialAccountWalletRequestPullConfiguration(ApiRequest):
    enabled: bool | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class FinancialAccountWalletRequestPushConfiguration(ApiRequest):
    enabled: bool | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class FinancialAccountWalletRequestWallet(ApiRequest):
    type: Literal['mobile_money', WalletType.MOBILE_MONEY]
    mobile_money: FinancialAccountWalletRequestWalletMobileMoney

@dataclass(frozen=True, slots=True, kw_only=True)
class FinancialAccountWalletRequestWalletMobileMoney(ApiRequest):
    account_number: str
    network: Literal['airtel', 'mtn', 'telecel', 'vodafone', MobileMoneyNetwork.AIRTEL, MobileMoneyNetwork.MTN, MobileMoneyNetwork.TELECEL, MobileMoneyNetwork.VODAFONE]

@dataclass(frozen=True, slots=True, kw_only=True)
class FinancialAccountBankRequest(ApiRequest):
    custom_data: dict[str, Any] | UnsetType = field(default=UNSET)
    description: str | UnsetType = field(default=UNSET)
    owner: FinancialAccountOwnerInput | UnsetType = field(default=UNSET)
    pull_configuration: FinancialAccountBankRequestPullConfiguration | UnsetType = field(default=UNSET)
    push_configuration: FinancialAccountBankRequestPushConfiguration | UnsetType = field(default=UNSET)
    currency: str
    label: str
    reference: str
    type: Literal['bank_account', FinancialAccountType.BANK_ACCOUNT]
    bank_account: FinancialAccountBankRequestBankAccount

@dataclass(frozen=True, slots=True, kw_only=True)
class FinancialAccountBankRequestPullConfiguration(ApiRequest):
    enabled: bool | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class FinancialAccountBankRequestPushConfiguration(ApiRequest):
    enabled: bool | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class FinancialAccountBankRequestBankAccountGhanaBankAccount(ApiRequest):
    bank_name: str | UnsetType = field(default=UNSET)
    branch: str | UnsetType = field(default=UNSET)
    sort_code: str | UnsetType = field(default=UNSET)
    swift_code: str | UnsetType = field(default=UNSET)
    holder: FinancialAccountOwnerInput | UnsetType = field(default=UNSET)
    number: str

@dataclass(frozen=True, slots=True, kw_only=True)
class FinancialAccountBankRequestBankAccount(ApiRequest):
    type: Literal['ghana_bank_account', BankAccountType.GHANA_BANK_ACCOUNT]
    ghana_bank_account: FinancialAccountBankRequestBankAccountGhanaBankAccount

@dataclass(frozen=True, slots=True, kw_only=True)
class FinancialAccountDoshRequest(ApiRequest):
    custom_data: dict[str, Any] | UnsetType = field(default=UNSET)
    description: str | UnsetType = field(default=UNSET)
    pull_configuration: FinancialAccountDoshRequestPullConfiguration | UnsetType = field(default=UNSET)
    push_configuration: FinancialAccountDoshRequestPushConfiguration | UnsetType = field(default=UNSET)
    currency: str
    label: str
    owner: FinancialAccountOwnerInput
    reference: str
    type: Literal['dosh_account', FinancialAccountType.DOSH_ACCOUNT]
    dosh_account: dict[str, Any]

@dataclass(frozen=True, slots=True, kw_only=True)
class FinancialAccountDoshRequestPullConfiguration(ApiRequest):
    enabled: bool | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class FinancialAccountDoshRequestPushConfiguration(ApiRequest):
    enabled: bool | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class FinancialAccountIDRequest(ApiRequest):
    account_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class FinancialAccountPageRequest(ApiRequest):
    page_size: int | UnsetType = field(default=UNSET)
    page_number: int

@dataclass(frozen=True, slots=True, kw_only=True)
class FinancialAccountUpdateRequest(ApiRequest):
    custom_data: dict[str, Any] | UnsetType = field(default=UNSET)
    description: str | UnsetType = field(default=UNSET)
    label: str | UnsetType = field(default=UNSET)
    owner: FinancialAccountOwnerUpdateInput | UnsetType = field(default=UNSET)
    reference: str | UnsetType = field(default=UNSET)
    account_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class FinancialAccountOwnerUpdateInput(ApiRequest):
    name: str | UnsetType = field(default=UNSET)
    address: FinancialAccountOwnerUpdateInputAddress | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class FinancialAccountOwnerUpdateInputAddress(ApiRequest):
    city: str | UnsetType = field(default=UNSET)
    country: str | UnsetType = field(default=UNSET)
    line_1: str | UnsetType = field(default=UNSET)
    line_2: str | UnsetType = field(default=UNSET)
    name: str | UnsetType = field(default=UNSET)
    phone: str | UnsetType = field(default=UNSET)
    post_code: str | UnsetType = field(default=UNSET)
    region: str | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class FinancialAccountDisableRequest(ApiRequest):
    unset_as_payout_destination: bool | UnsetType = field(default=UNSET)
    account_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class FinancialAccountEnablePullRequest(ApiRequest):
    ip_address: str | UnsetType = field(default=UNSET)
    user_agent: str | UnsetType = field(default=UNSET)
    account_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class LookupBalancesRequest(ApiRequest):
    pass

@dataclass(frozen=True, slots=True, kw_only=True)
class LookupBalanceTransactionRequest(ApiRequest):
    transaction_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class PageBalanceTransactionsRequest(ApiRequest):
    page_number: int
    page_size: int

@dataclass(frozen=True, slots=True, kw_only=True)
class SchedulePayoutRequest(ApiRequest):
    execute_after: str | UnsetType = field(default=UNSET)
    max_amount: int | UnsetType = field(default=UNSET)
    destination_id: str
    reference: str

@dataclass(frozen=True, slots=True, kw_only=True)
class LookupPayoutRequest(ApiRequest):
    payout_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class SetPayoutDestinationsRequest(ApiRequest):
    destinations: dict[str, str]

@dataclass(frozen=True, slots=True, kw_only=True)
class GetPayoutSettingsRequest(ApiRequest):
    pass

@dataclass(frozen=True, slots=True, kw_only=True)
class DisableAutomaticPayoutsRequest(ApiRequest):
    pass

@dataclass(frozen=True, slots=True, kw_only=True)
class EnableAutomaticPayoutsRequest(ApiRequest):
    pass

@dataclass(frozen=True, slots=True, kw_only=True)
class PagePayoutsRequest(ApiRequest):
    page_size: int | UnsetType = field(default=UNSET)
    page_number: int

@dataclass(frozen=True, slots=True, kw_only=True)
class CancelPayoutRequest(ApiRequest):
    payout_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class LookupFileRequest(ApiRequest):
    file_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class PageFilesRequest(ApiRequest):
    purpose: str | UnsetType = field(default=UNSET)
    status: Literal['uploading', 'processing', 'available', 'failed', 'deleted', FileStatus.UPLOADING, FileStatus.PROCESSING, FileStatus.AVAILABLE, FileStatus.FAILED, FileStatus.DELETED] | UnsetType = field(default=UNSET)
    page_number: int | UnsetType = field(default=UNSET)
    page_size: int | UnsetType = field(default=UNSET)
    created_after: str | UnsetType = field(default=UNSET)
    created_before: str | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class FileContentsRequest(ApiRequest):
    disposition: Literal['attachment', 'inline', FileDisposition.ATTACHMENT, FileDisposition.INLINE] | UnsetType = field(default=UNSET)
    delivery: Literal['stream', 'redirect', FileDelivery.STREAM, FileDelivery.REDIRECT] | UnsetType = field(default=UNSET)
    file_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class DeleteFileRequest(ApiRequest):
    file_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class CreateFileLinkRequest(ApiRequest):
    delivery: FileLinkDeliveryInput | UnsetType = field(default=UNSET)
    access: FileLinkAccessRequest | UnsetType = field(default=UNSET)
    created_by: FileActorInput | UnsetType = field(default=UNSET)
    custom_data: dict[str, str] | UnsetType = field(default=UNSET)
    expires_at: str | UnsetType = field(default=UNSET)
    file_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class FileLinkDeliveryInput(ApiRequest):
    mode: Literal['redirect', 'download', 'inline', FileLinkDeliveryMode.REDIRECT, FileLinkDeliveryMode.DOWNLOAD, FileLinkDeliveryMode.INLINE] | UnsetType = field(default=UNSET)
    filename: str | UnsetType = field(default=UNSET)
    content_type: str | UnsetType = field(default=UNSET)
    disposition: str | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class FileLinkAccessRequest(ApiRequest):
    max_accesses: int | UnsetType = field(default=UNSET)
    allow_download: bool | UnsetType = field(default=UNSET)
    allowed_origins: list[str] | UnsetType = field(default=UNSET)
    allowed_ip_ranges: list[str] | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class FileActorInput(ApiRequest):
    email: str | UnsetType = field(default=UNSET)
    id: str | UnsetType = field(default=UNSET)
    name: str | UnsetType = field(default=UNSET)
    type: str | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class LookupFileLinkRequest(ApiRequest):
    id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class PageFileLinksRequest(ApiRequest):
    file_id: str | UnsetType = field(default=UNSET)
    status: Literal['active', 'revoked', 'expired', 'disabled', FileLinkStatus.ACTIVE, FileLinkStatus.REVOKED, FileLinkStatus.EXPIRED, FileLinkStatus.DISABLED] | UnsetType = field(default=UNSET)
    page_number: int | UnsetType = field(default=UNSET)
    page_size: int | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class RevokeFileLinkRequest(ApiRequest):
    revoked_by: FileActorInput | UnsetType = field(default=UNSET)
    id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class CreateUploadRequestRequest(ApiRequest):
    constraints: UploadRequestConstraintsInput | UnsetType = field(default=UNSET)
    display: UploadRequestDisplayInput | UnsetType = field(default=UNSET)
    subject: FilePartyInput | UnsetType = field(default=UNSET)
    recipient: FilePartyInput | UnsetType = field(default=UNSET)
    resource: FileResourceInput | UnsetType = field(default=UNSET)
    requester: FileActorInput | UnsetType = field(default=UNSET)
    attempts: UploadRequestAttemptsRequest | UnsetType = field(default=UNSET)
    custom_data: dict[str, str] | UnsetType = field(default=UNSET)
    expires_at: str | UnsetType = field(default=UNSET)
    purpose: str

@dataclass(frozen=True, slots=True, kw_only=True)
class UploadRequestConstraintsInput(ApiRequest):
    min_size: int | UnsetType = field(default=UNSET)
    max_size: int | UnsetType = field(default=UNSET)
    exact_size: int | UnsetType = field(default=UNSET)
    content_types: list[str] | UnsetType = field(default=UNSET)
    extensions: list[str] | UnsetType = field(default=UNSET)
    filename: str | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class UploadRequestDisplayInput(ApiRequest):
    title: str | UnsetType = field(default=UNSET)
    description: str | UnsetType = field(default=UNSET)
    help_text: str | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class FilePartyInput(ApiRequest):
    type: str | UnsetType = field(default=UNSET)
    id: str | UnsetType = field(default=UNSET)
    name: str | UnsetType = field(default=UNSET)
    email: str | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class FileResourceInput(ApiRequest):
    type: str | UnsetType = field(default=UNSET)
    id: str | UnsetType = field(default=UNSET)
    name: str | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class UploadRequestAttemptsRequest(ApiRequest):
    max_attempts: int | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class LookupUploadRequestRequest(ApiRequest):
    id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class PageUploadRequestsRequest(ApiRequest):
    purpose: str | UnsetType = field(default=UNSET)
    status: Literal['pending', 'uploading', 'fulfilled', 'expired', 'canceled', 'failed', UploadRequestStatus.PENDING, UploadRequestStatus.UPLOADING, UploadRequestStatus.FULFILLED, UploadRequestStatus.EXPIRED, UploadRequestStatus.CANCELED, UploadRequestStatus.FAILED] | UnsetType = field(default=UNSET)
    resource: FileResourceInput | UnsetType = field(default=UNSET)
    page_number: int | UnsetType = field(default=UNSET)
    page_size: int | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class CancelUploadRequestRequest(ApiRequest):
    canceled_by: FileActorInput | UnsetType = field(default=UNSET)
    id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class ReviewUploadRequestAttemptByIDRequest(ApiRequest):
    public_message: str | UnsetType = field(default=UNSET)
    reasons: list[UploadRequestReviewReasonInput] | UnsetType = field(default=UNSET)
    attempt_id: str
    decision: Literal['approved', 'rejected', UploadReviewDecision.APPROVED, UploadReviewDecision.REJECTED]
    id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class UploadRequestReviewReasonInput(ApiRequest):
    param: str | UnsetType = field(default=UNSET)
    code: str
    message: str

@dataclass(frozen=True, slots=True, kw_only=True)
class ReviewUploadRequestAttemptByOrdinalRequest(ApiRequest):
    public_message: str | UnsetType = field(default=UNSET)
    reasons: list[UploadRequestReviewReasonInput] | UnsetType = field(default=UNSET)
    attempt_ordinal: int
    decision: Literal['approved', 'rejected', UploadReviewDecision.APPROVED, UploadReviewDecision.REJECTED]
    id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class FileReferenceReconcileRequest(ApiRequest):
    references: list[FileReferenceInput] | UnsetType = field(default=UNSET)
    resource_type: str
    resource_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class FileReferenceInput(ApiRequest):
    reference: str | UnsetType = field(default=UNSET)
    reference_kind: str | UnsetType = field(default=UNSET)
    purpose: str | UnsetType = field(default=UNSET)
    file_id: str
    field: str

@dataclass(frozen=True, slots=True, kw_only=True)
class TokenizeMobileMoneyPaymentMethodRequest(ApiRequest):
    custom_data: dict[str, str] | UnsetType = field(default=UNSET)
    customer_id: str
    type: Literal['mobile_money', PaymentMethodType.MOBILE_MONEY]
    mobile_money: TokenizeMobileMoneyPaymentMethodRequestMobileMoney
    owner: PaymentMethodOwnerInput

@dataclass(frozen=True, slots=True, kw_only=True)
class TokenizeMobileMoneyPaymentMethodRequestMobileMoney(ApiRequest):
    account_number: str
    network: Literal['airtel', 'mtn', 'telecel', 'vodafone', MobileMoneyNetwork.AIRTEL, MobileMoneyNetwork.MTN, MobileMoneyNetwork.TELECEL, MobileMoneyNetwork.VODAFONE]

@dataclass(frozen=True, slots=True, kw_only=True)
class PaymentMethodOwnerInput(ApiRequest):
    address: PaymentMethodOwnerInputAddress
    name: str

@dataclass(frozen=True, slots=True, kw_only=True)
class PaymentMethodOwnerInputAddress(ApiRequest):
    city: str | UnsetType = field(default=UNSET)
    line1: str | UnsetType = field(default=UNSET)
    line2: str | UnsetType = field(default=UNSET)
    name: str | UnsetType = field(default=UNSET)
    phone_number: str | UnsetType = field(default=UNSET)
    post_code: str | UnsetType = field(default=UNSET)
    region: str | UnsetType = field(default=UNSET)
    country: str

@dataclass(frozen=True, slots=True, kw_only=True)
class LookupPaymentMethodRequest(ApiRequest):
    payment_method_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class PaymentMethodPageRequest(ApiRequest):
    customer_id: str | UnsetType = field(default=UNSET)
    page_number: int | UnsetType = field(default=UNSET)
    page_size: int | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class UpdatePaymentMethodRequest(ApiRequest):
    custom_data: dict[str, str | None] | UnsetType = field(default=UNSET)
    active: bool | UnsetType = field(default=UNSET)
    archived: bool | UnsetType = field(default=UNSET)
    owner: UpdatePaymentMethodRequestOwner | UnsetType = field(default=UNSET)
    payment_method_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class UpdatePaymentMethodRequestOwner(ApiRequest):
    name: str | UnsetType = field(default=UNSET)
    address: UpdatePaymentMethodRequestOwnerAddress | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class UpdatePaymentMethodRequestOwnerAddress(ApiRequest):
    city: str | UnsetType = field(default=UNSET)
    country: str | UnsetType = field(default=UNSET)
    line1: str | UnsetType = field(default=UNSET)
    line2: str | UnsetType = field(default=UNSET)
    name: str | UnsetType = field(default=UNSET)
    phone_number: str | UnsetType = field(default=UNSET)
    post_code: str | UnsetType = field(default=UNSET)
    region: str | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class ActivatePaymentMethodRequest(ApiRequest):
    payment_method_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class DisactivatePaymentMethodRequest(ApiRequest):
    payment_method_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class ArchivePaymentMethodRequest(ApiRequest):
    payment_method_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class UnarchivePaymentMethodRequest(ApiRequest):
    payment_method_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class GetPaymentMethodSettingsRequest(ApiRequest):
    pass

@dataclass(frozen=True, slots=True, kw_only=True)
class CreateProductRequest(ApiRequest):
    reference: str | UnsetType = field(default=UNSET)
    description: str | UnsetType = field(default=UNSET)
    about: str | UnsetType = field(default=UNSET)
    tax_code: str | UnsetType = field(default=UNSET)
    category: str | UnsetType = field(default=UNSET)
    shipment: ProductShipmentInput | UnsetType = field(default=UNSET)
    dimensions: ProductDimensionsInput | UnsetType = field(default=UNSET)
    unit_dimension: str | UnsetType = field(default=UNSET)
    media: ProductMediaInput | UnsetType = field(default=UNSET)
    attributes: list[ProductAttributeInput] | UnsetType = field(default=UNSET)
    publish: bool | UnsetType = field(default=UNSET)
    custom_data: dict[str, str] | UnsetType = field(default=UNSET)
    type: Literal['physical', 'digital', 'service', 'voucher', 'custom', 'cause', ProductType.PHYSICAL, ProductType.DIGITAL, ProductType.SERVICE, ProductType.VOUCHER, ProductType.CUSTOM, ProductType.CAUSE]
    name: str

@dataclass(frozen=True, slots=True, kw_only=True)
class ProductShipmentInput(ApiRequest):
    type: Literal['delivery', 'download', 'render', 'stream', ProductShipmentInputType.DELIVERY, ProductShipmentInputType.DOWNLOAD, ProductShipmentInputType.RENDER, ProductShipmentInputType.STREAM]

@dataclass(frozen=True, slots=True, kw_only=True)
class ProductDimensionsInput(ApiRequest):
    physical: ProductDimensionsInputPhysical | UnsetType = field(default=UNSET)
    digital: ProductDimensionsInputDigital | UnsetType = field(default=UNSET)
    custom: ProductDimensionsInputCustom | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class ProductDimensionsInputPhysical(ApiRequest):
    weight_unit: str | UnsetType = field(default=UNSET)
    weight: float | UnsetType = field(default=UNSET)
    size: float | UnsetType = field(default=UNSET)
    volume_unit: str | UnsetType = field(default=UNSET)
    volume: float | UnsetType = field(default=UNSET)
    length: float | UnsetType = field(default=UNSET)
    height: float | UnsetType = field(default=UNSET)
    width: float | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class ProductDimensionsInputDigital(ApiRequest):
    bytes: float | UnsetType = field(default=UNSET)
    size_unit: str | UnsetType = field(default=UNSET)
    size: float | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class ProductDimensionsInputCustom(ApiRequest):
    size_unit: str | UnsetType = field(default=UNSET)
    size: float | UnsetType = field(default=UNSET)
    details: dict[str, str] | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class ProductMediaInput(ApiRequest):
    hero_image: str | UnsetType = field(default=UNSET)
    thumbnail: str | UnsetType = field(default=UNSET)
    web_page_url: str | UnsetType = field(default=UNSET)
    brand_logo: str | UnsetType = field(default=UNSET)
    infographic: str | UnsetType = field(default=UNSET)
    promo_video: str | UnsetType = field(default=UNSET)
    demo_video: str | UnsetType = field(default=UNSET)
    gallery: list[str] | UnsetType = field(default=UNSET)
    downloads: list[str] | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class ProductAttributeInput(ApiRequest):
    name: str
    value: str

@dataclass(frozen=True, slots=True, kw_only=True)
class AddProductPriceRequest(ApiRequest):
    label: str | UnsetType = field(default=UNSET)
    about: str | UnsetType = field(default=UNSET)
    product_id: str
    amount: AmountParams

@dataclass(frozen=True, slots=True, kw_only=True)
class LookupProductRequest(ApiRequest):
    product_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class UpdateProductRequest(ApiRequest):
    type: Literal['physical', 'digital', 'service', 'voucher', 'custom', 'cause', ProductType.PHYSICAL, ProductType.DIGITAL, ProductType.SERVICE, ProductType.VOUCHER, ProductType.CUSTOM, ProductType.CAUSE] | UnsetType = field(default=UNSET)
    name: str | UnsetType = field(default=UNSET)
    description: str | UnsetType = field(default=UNSET)
    about: str | UnsetType = field(default=UNSET)
    tax_code: str | UnsetType = field(default=UNSET)
    category: str | UnsetType = field(default=UNSET)
    shipment: ProductShipmentInput | UnsetType = field(default=UNSET)
    dimensions: ProductDimensionsInput | UnsetType = field(default=UNSET)
    unit_dimension: str | UnsetType = field(default=UNSET)
    media: ProductMediaInput | UnsetType = field(default=UNSET)
    images: list[str] | UnsetType = field(default=UNSET)
    attributes: list[ProductAttributeInput] | UnsetType = field(default=UNSET)
    custom_data: dict[str, str] | UnsetType = field(default=UNSET)
    product_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class ProductActionRequest(ApiRequest):
    product_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class PageProductsRequest(ApiRequest):
    page_size: int | UnsetType = field(default=UNSET)
    page_number: int

@dataclass(frozen=True, slots=True, kw_only=True)
class CreatePurchaseIntentRequest(ApiRequest):
    product: CreatePurchaseIntentRequestProduct | UnsetType = field(default=UNSET)
    product_id: str | UnsetType = field(default=UNSET)
    price: CreatePurchaseIntentRequestPrice | UnsetType = field(default=UNSET)
    price_id: str | UnsetType = field(default=UNSET)
    usage: CreatePurchaseIntentRequestUsage | UnsetType = field(default=UNSET)
    expires_at: str | UnsetType = field(default=UNSET)
    quantity: CreatePurchaseIntentRequestQuantity

@dataclass(frozen=True, slots=True, kw_only=True)
class CreatePurchaseIntentRequestProduct(ApiRequest):
    variant_set_id: str | UnsetType = field(default=UNSET)
    id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class CreatePurchaseIntentRequestPrice(ApiRequest):
    id: str | UnsetType = field(default=UNSET)
    nominal: PriceParams | UnsetType = field(default=UNSET)
    original: CreatePurchaseIntentRequestPriceOriginal | UnsetType = field(default=UNSET)
    original_id: str | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class CreatePurchaseIntentRequestPriceOriginal(ApiRequest):
    id: str | UnsetType = field(default=UNSET)
    nominal: PriceParams | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class CreatePurchaseIntentRequestQuantity(ApiRequest):
    max: int | UnsetType = field(default=UNSET)
    min: int

@dataclass(frozen=True, slots=True, kw_only=True)
class CreatePurchaseIntentRequestUsage(ApiRequest):
    single_use: bool | UnsetType = field(default=UNSET)
    multi_use: bool | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class UpdatePurchaseIntentRequest(ApiRequest):
    expires_at: str | None | UnsetType = field(default=UNSET)
    id: str | UnsetType = field(default=UNSET)
    quantity: UpdatePurchaseIntentRequestQuantity | UnsetType = field(default=UNSET)
    purchase_intent_id: str | UnsetType = field(default=UNSET)
    reactivate: bool | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class UpdatePurchaseIntentRequestQuantity(ApiRequest):
    max: int | UnsetType = field(default=UNSET)
    min: int

@dataclass(frozen=True, slots=True, kw_only=True)
class CancelPurchaseIntentRequest(ApiRequest):
    id: str | UnsetType = field(default=UNSET)
    purchase_intent_id: str | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class LookupPurchaseIntentRequest(ApiRequest):
    id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class PagePurchaseIntentsRequest(ApiRequest):
    page_number: int
    page_size: int

@dataclass(frozen=True, slots=True, kw_only=True)
class CatalogPriceParams(ApiRequest):
    product_id: str | UnsetType = field(default=UNSET)
    label: str | UnsetType = field(default=UNSET)
    about: str | UnsetType = field(default=UNSET)
    amount: AmountParams

@dataclass(frozen=True, slots=True, kw_only=True)
class LookupPriceRequest(ApiRequest):
    price_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class PricePageRequest(ApiRequest):
    page_number: int | UnsetType = field(default=UNSET)
    page_size: int | UnsetType = field(default=UNSET)
    product_id: str | UnsetType = field(default=UNSET)

@dataclass(frozen=True, slots=True, kw_only=True)
class UpdatePriceRequest(ApiRequest):
    label: str | UnsetType = field(default=UNSET)
    about: str | UnsetType = field(default=UNSET)
    price_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class PriceActionRequest(ApiRequest):
    price_id: str

@dataclass(frozen=True, slots=True, kw_only=True)
class ListCountrySpecsRequest(ApiRequest):
    pass

ChimeInlineRecipientInput: TypeAlias = ChimeInlineRecipientInputVariant1 | ChimeInlineRecipientInputVariant2
ChimeRecipientInput: TypeAlias = ChimeInlineRecipientInput | ChimeSavedCustomerRecipientInput
MessageTemplateVariablesInput: TypeAlias = dict[str, Any]
MessageTemplateAttachmentIDsInput: TypeAlias = list[str]
CreateMessageTemplateRequest: TypeAlias = CreateSMSMessageTemplateRequest | CreateEmailMessageTemplateRequest
ProductDetailsInput: TypeAlias = InlineProductDetailsInput | CatalogProductWithPriceDataInput | CatalogProductWithPriceReferenceInput
LineItemInput: TypeAlias = ProductLineItemInput | FeeLineItemInput | ShippingLineItemInput
CreateOrderRequest: TypeAlias = CreateOrderNewCustomerInput | CreateOrderExistingCustomerInput
RefundReasonInput: TypeAlias = Literal[
    'requested_by_customer',
    'duplicate',
    'fraudulent',
    'order_canceled',
    'item_returned',
    'item_damaged',
    'item_not_received',
    'item_not_as_described',
    'custom',
    RefundReason.REQUESTED_BY_CUSTOMER,
    RefundReason.DUPLICATE,
    RefundReason.FRAUDULENT,
    RefundReason.ORDER_CANCELED,
    RefundReason.ITEM_RETURNED,
    RefundReason.ITEM_DAMAGED,
    RefundReason.ITEM_NOT_RECEIVED,
    RefundReason.ITEM_NOT_AS_DESCRIBED,
    RefundReason.CUSTOM,
]
FinancialAccountCreateRequest: TypeAlias = FinancialAccountWalletRequest | FinancialAccountBankRequest | FinancialAccountDoshRequest
ReviewUploadRequestAttemptRequest: TypeAlias = ReviewUploadRequestAttemptByIDRequest | ReviewUploadRequestAttemptByOrdinalRequest

__all__ = [
    'ActivatePaymentMethodRequest',
    'AddProductPriceRequest',
    'AddressInput',
    'ArchivePaymentMethodRequest',
    'BillingDetailsInput',
    'BroadcastRequest',
    'BroadcastRequestRequestMeta',
    'CancelBroadcastRequest',
    'CancelOrderRequest',
    'CancelPayoutRequest',
    'CancelPurchaseIntentRequest',
    'CancelRefundRequest',
    'CancelScheduleRequest',
    'CancelUploadRequestRequest',
    'CatalogProductWithPriceDataInput',
    'CatalogProductWithPriceReferenceInput',
    'ChimeEmailMailboxInput',
    'ChimeEmailMessageInput',
    'ChimeInlineRecipientInput',
    'ChimeInlineRecipientInputVariant1',
    'ChimeInlineRecipientInputVariant1Phone',
    'ChimeInlineRecipientInputVariant2',
    'ChimeInlineRecipientInputVariant2Email',
    'ChimeRecipientInput',
    'ChimeSavedCustomerRecipientInput',
    'CompleteOrderRequest',
    'ConfirmPaymentRequest',
    'CreateApplicationRequest',
    'CreateApplicationRequestRelationshipPolicy',
    'CreateCustomerRequest',
    'CreateEmailMessageTemplateRequest',
    'CreateFileLinkRequest',
    'CreateMessageTemplateRequest',
    'CreateOrderExistingCustomerInput',
    'CreateOrderExistingCustomerInputCheckoutSettings',
    'CreateOrderExistingCustomerInputRequestMeta',
    'CreateOrderNewCustomerInput',
    'CreateOrderNewCustomerInputCheckoutSettings',
    'CreateOrderNewCustomerInputRequestMeta',
    'CreateOrderRequest',
    'CatalogPriceParams',
    'CreateProductRequest',
    'CreatePurchaseIntentRequest',
    'CreatePurchaseIntentRequestPrice',
    'CreatePurchaseIntentRequestPriceOriginal',
    'CreatePurchaseIntentRequestProduct',
    'CreatePurchaseIntentRequestQuantity',
    'CreatePurchaseIntentRequestUsage',
    'CreateRefundLineItemInput',
    'CreateRefundRequest',
    'CreateSMSMessageTemplateRequest',
    'CreateUploadRequestRequest',
    'CustomerAddressInput',
    'CustomerDataInput',
    'DeleteFileRequest',
    'DestroySecretKeyRequest',
    'DisableAutomaticPayoutsRequest',
    'DisactivatePaymentMethodRequest',
    'EnableAutomaticPayoutsRequest',
    'FeeDetailsInput',
    'FeeLineItemInput',
    'FileActorInput',
    'FileContentsRequest',
    'FileLinkAccessRequest',
    'FileLinkDeliveryInput',
    'FilePartyInput',
    'FileReferenceInput',
    'FileReferenceReconcileRequest',
    'FileResourceInput',
    'FinalizeOrderRequest',
    'FinancialAccountBankRequest',
    'FinancialAccountBankRequestBankAccount',
    'FinancialAccountBankRequestPullConfiguration',
    'FinancialAccountBankRequestPushConfiguration',
    'FinancialAccountCreateRequest',
    'FinancialAccountDisableRequest',
    'FinancialAccountDoshRequest',
    'FinancialAccountDoshRequestPullConfiguration',
    'FinancialAccountDoshRequestPushConfiguration',
    'FinancialAccountEnablePullRequest',
    'FinancialAccountIDRequest',
    'FinancialAccountOwnerInput',
    'FinancialAccountOwnerInputAddress',
    'FinancialAccountOwnerUpdateInput',
    'FinancialAccountOwnerUpdateInputAddress',
    'FinancialAccountPageRequest',
    'FinancialAccountUpdateRequest',
    'FinancialAccountWalletRequest',
    'FinancialAccountWalletRequestPullConfiguration',
    'FinancialAccountWalletRequestPushConfiguration',
    'FinancialAccountWalletRequestWallet',
    'FinancialAccountWalletRequestWalletMobileMoney',
    'GenerateSecretKeyRequest',
    'GetPaymentMethodSettingsRequest',
    'GetPayoutSettingsRequest',
    'InitiateOTPRequest',
    'InlineProductDetailsInput',
    'InvoiceSettingsInput',
    'LineItemInput',
    'ListCountrySpecsRequest',
    'LookupBalanceTransactionRequest',
    'LookupBalancesRequest',
    'LookupBroadcastRequest',
    'LookupChimeRequest',
    'LookupCustomerRequest',
    'LookupFileLinkRequest',
    'LookupFileRequest',
    'LookupOTPRequest',
    'LookupOrderRequest',
    'LookupPaymentMethodRequest',
    'LookupPayoutRequest',
    'LookupPriceRequest',
    'LookupProductRequest',
    'LookupPurchaseIntentRequest',
    'LookupRefundRequest',
    'LookupScheduleRequest',
    'LookupSecretKeyRequest',
    'LookupUploadRequestRequest',
    'MessageTemplateAttachmentIDsInput',
    'MessageTemplateEmailContentInput',
    'MessageTemplateIDRequest',
    'MessageTemplateMailboxInput',
    'MessageTemplateReferenceInput',
    'MessageTemplateSMSContentInput',
    'MessageTemplateVariableInput',
    'MessageTemplateVariableItemInput',
    'MessageTemplateVariablesInput',
    'OrderDocumentDeliveryRequest',
    'OrderPayoutSettingsRequest',
    'OrderPayoutSettingsRequestDestination',
    'PageBalanceTransactionsRequest',
    'PageChimesRequest',
    'PageCustomersRequest',
    'PageFileLinksRequest',
    'PageFilesRequest',
    'PageMessageTemplatesRequest',
    'PageOrdersRequest',
    'PagePayoutsRequest',
    'PageProductsRequest',
    'PagePurchaseIntentsRequest',
    'PageRefundsRequest',
    'PageSecretKeysRequest',
    'PageUploadRequestsRequest',
    'PayOrderRequest',
    'PaymentMethodDataInput',
    'PaymentMethodDataInputMobileMoney',
    'PaymentMethodOwnerInput',
    'PaymentMethodOwnerInputAddress',
    'PaymentMethodPageRequest',
    'PriceActionRequest',
    'PricePageRequest',
    'ProductActionRequest',
    'ProductAttributeInput',
    'ProductDetailsInput',
    'ProductDimensionsInput',
    'ProductDimensionsInputCustom',
    'ProductDimensionsInputDigital',
    'ProductDimensionsInputPhysical',
    'ProductLineItemInput',
    'ProductMediaInput',
    'ProductShipmentInput',
    'RefundReasonInput',
    'RefundRequestMetaInput',
    'RenderMessageTemplatePreviewRequest',
    'RequestConfirmationRequest',
    'ReviewUploadRequestAttemptByIDRequest',
    'ReviewUploadRequestAttemptByOrdinalRequest',
    'ReviewUploadRequestAttemptRequest',
    'RevokeFileLinkRequest',
    'ScheduleChimeRequest',
    'ScheduleChimeRequestRequestMeta',
    'SchedulePayoutRequest',
    'SecretKeyUsageRequest',
    'SendChimeRequest',
    'SendChimeRequestRequestMeta',
    'SetPayoutDestinationsRequest',
    'ShippingDetailsInput',
    'ShippingInput',
    'ShippingLineItemInput',
    'TokenizeMobileMoneyPaymentMethodRequest',
    'TokenizeMobileMoneyPaymentMethodRequestMobileMoney',
    'UnarchivePaymentMethodRequest',
    'UpdateApplicationRequest',
    'UpdateCustomerRequest',
    'UpdateMessageTemplateRequest',
    'UpdateOrderRequest',
    'UpdateOrderRequestPaymentMethodData',
    'UpdateOrderRequestPaymentMethodDataMobileMoney',
    'UpdatePaymentMethodRequest',
    'UpdatePaymentMethodRequestOwner',
    'UpdatePaymentMethodRequestOwnerAddress',
    'UpdatePriceRequest',
    'UpdateProductRequest',
    'UpdatePurchaseIntentRequest',
    'UpdatePurchaseIntentRequestQuantity',
    'UpdateSecretKeyRequest',
    'UploadRequestAttemptsRequest',
    'UploadRequestConstraintsInput',
    'UploadRequestDisplayInput',
    'UploadRequestReviewReasonInput',
    'VerifyOTPRequest',
]
