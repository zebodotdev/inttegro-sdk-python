"""Generated typed request dictionaries. Do not edit by hand."""

from __future__ import annotations

from typing import Any, Literal, TypeAlias, TypedDict

class _InitiateOTPRequestOptional(TypedDict, total=False):
    async_delivery: bool
    message_template: str
    purpose: str
    sender: str
    token_alphabet: str
    token_alphabet_type: Literal['numeric', 'alpha', 'alphanumeric']
    validity_duration_in_minutes: int

class InitiateOTPRequest(_InitiateOTPRequestOptional):
    recipient: str
    service_name: str
    token_size: int

class VerifyOTPRequest(TypedDict):
    transaction_id: str
    recipient: str
    token: str

class LookupOTPRequest(TypedDict):
    transaction_id: str

class _SendChimeRequestOptional(TypedDict, total=False):
    full_message: str
    email: ChimeEmailMessageInput
    message_template: MessageTemplateReferenceInput
    sender_id: str
    purpose: str
    custom_data: dict[str, str]
    request_meta: SendChimeRequestRequestMeta

class SendChimeRequest(_SendChimeRequestOptional):
    recipient: ChimeRecipientInput

class _ChimeInlineRecipientInputVariant1Optional(TypedDict, total=False):
    name: str

class ChimeInlineRecipientInputVariant1(_ChimeInlineRecipientInputVariant1Optional):
    phone: ChimeInlineRecipientInputVariant1Phone
    type: Literal['phone']

class ChimeInlineRecipientInputVariant1Phone(TypedDict):
    number: str

class _ChimeInlineRecipientInputVariant2Optional(TypedDict, total=False):
    name: str

class ChimeInlineRecipientInputVariant2(_ChimeInlineRecipientInputVariant2Optional):
    email: ChimeInlineRecipientInputVariant2Email
    type: Literal['email']

class ChimeInlineRecipientInputVariant2Email(TypedDict):
    address: str

class ChimeSavedCustomerRecipientInput(TypedDict):
    customer_id: str
    transport: Literal['sms', 'email']

class _ChimeEmailMessageInputOptional(TypedDict, total=False):
    html: str
    reply_to: str
    headers: dict[str, str]

_ChimeEmailMessageInputRequired = TypedDict('_ChimeEmailMessageInputRequired', {'subject': 'str', 'text': 'str', 'from': 'ChimeEmailMailboxInput'})

class ChimeEmailMessageInput(_ChimeEmailMessageInputOptional, _ChimeEmailMessageInputRequired):
    pass

class ChimeEmailMailboxInput(TypedDict, total=False):
    name: str
    address: str

class _MessageTemplateReferenceInputOptional(TypedDict, total=False):
    variables: MessageTemplateVariablesInput

class MessageTemplateReferenceInput(_MessageTemplateReferenceInputOptional):
    template_id: str

class SendChimeRequestRequestMeta(TypedDict, total=False):
    idempotency_key: str

class LookupChimeRequest(TypedDict):
    chime_id: str

class PageChimesRequest(TypedDict, total=False):
    customer_id: str
    page_number: int
    page_size: int
    recipient: str

class _ScheduleChimeRequestOptional(TypedDict, total=False):
    request_meta: ScheduleChimeRequestRequestMeta
    full_message: str
    email: ChimeEmailMessageInput
    message_template: MessageTemplateReferenceInput
    sender_id: str
    purpose: str

class ScheduleChimeRequest(_ScheduleChimeRequestOptional):
    recipients: list[ChimeRecipientInput]
    send_after: str

class ScheduleChimeRequestRequestMeta(TypedDict, total=False):
    idempotency_key: str

class _BroadcastRequestOptional(TypedDict, total=False):
    request_meta: BroadcastRequestRequestMeta
    message_template: str | MessageTemplateReferenceInput
    email: ChimeEmailMessageInput
    purpose: str
    sender: str

class BroadcastRequest(_BroadcastRequestOptional):
    recipients: list[ChimeRecipientInput]

class BroadcastRequestRequestMeta(TypedDict, total=False):
    idempotency_key: str

class LookupScheduleRequest(TypedDict):
    schedule_id: str

class CancelScheduleRequest(TypedDict):
    schedule_id: str

class LookupBroadcastRequest(TypedDict):
    broadcast_id: str

class CancelBroadcastRequest(TypedDict):
    broadcast_id: str

class _CreateSMSMessageTemplateRequestOptional(TypedDict, total=False):
    about: str
    locale: str
    variables: list[MessageTemplateVariableInput]

class CreateSMSMessageTemplateRequest(_CreateSMSMessageTemplateRequestOptional):
    channel: Literal['sms']
    name: str
    purpose: str
    sms: MessageTemplateSMSContentInput

class MessageTemplateSMSContentInput(TypedDict):
    message_template: str

class _MessageTemplateVariableInputOptional(TypedDict, total=False):
    required: bool
    default: Any
    about: str
    items: list[MessageTemplateVariableItemInput]

class MessageTemplateVariableInput(_MessageTemplateVariableInputOptional):
    name: str
    type: Literal['string', 'number', 'integer', 'boolean', 'url', 'email', 'phone', 'date', 'datetime', 'array']

class _MessageTemplateVariableItemInputOptional(TypedDict, total=False):
    about: str
    default: Any
    required: bool

class MessageTemplateVariableItemInput(_MessageTemplateVariableItemInputOptional):
    name: str
    type: Literal['string', 'number', 'integer', 'boolean', 'url', 'email', 'phone', 'date', 'datetime']

class _CreateEmailMessageTemplateRequestOptional(TypedDict, total=False):
    about: str
    attachments: MessageTemplateAttachmentIDsInput
    locale: str
    variables: list[MessageTemplateVariableInput]

class CreateEmailMessageTemplateRequest(_CreateEmailMessageTemplateRequestOptional):
    channel: Literal['email']
    email: MessageTemplateEmailContentInput
    name: str
    purpose: str

_MessageTemplateEmailContentInputOptional = TypedDict('_MessageTemplateEmailContentInputOptional', {'from': 'MessageTemplateMailboxInput', 'reply_to': 'MessageTemplateMailboxInput', 'headers': 'dict[str, str]'}, total=False)

class MessageTemplateEmailContentInput(_MessageTemplateEmailContentInputOptional):
    subject: str
    html: str

class _MessageTemplateMailboxInputOptional(TypedDict, total=False):
    name: str

class MessageTemplateMailboxInput(_MessageTemplateMailboxInputOptional):
    address: str

class _UpdateMessageTemplateRequestOptional(TypedDict, total=False):
    name: str
    about: str
    channel: Literal['sms', 'email']
    purpose: str
    locale: str
    variables: list[MessageTemplateVariableInput]
    sms: MessageTemplateSMSContentInput
    email: MessageTemplateEmailContentInput
    attachments: MessageTemplateAttachmentIDsInput

class UpdateMessageTemplateRequest(_UpdateMessageTemplateRequestOptional):
    id: str

class MessageTemplateIDRequest(TypedDict):
    id: str

class PageMessageTemplatesRequest(TypedDict, total=False):
    page: int
    size: int
    status: Literal['draft', 'published', 'archived']
    channel: Literal['sms', 'email']
    purpose: str
    locale: str

class RenderMessageTemplatePreviewRequest(TypedDict):
    message_template: MessageTemplateReferenceInput

class _CreateCustomerRequestOptional(TypedDict, total=False):
    billing_address: CustomerAddressInput
    custom_data: dict[str, Any]
    email_address: str
    phone_number: str
    reference: str
    shipping_address: CustomerAddressInput
    title: str

class CreateCustomerRequest(_CreateCustomerRequestOptional):
    name: str

class _CustomerAddressInputOptional(TypedDict, total=False):
    city: str
    line1: str
    line2: str
    name: str
    phone_number: str
    post_code: str
    region: str

class CustomerAddressInput(_CustomerAddressInputOptional):
    country: str

class LookupCustomerRequest(TypedDict):
    customer_id: str

class _UpdateCustomerRequestOptional(TypedDict, total=False):
    billing_address: CustomerAddressInput
    custom_data: dict[str, Any]
    email_address: str
    name: str
    phone_number: str
    reference: str
    shipping_address: CustomerAddressInput
    suffix: str
    title: str

class UpdateCustomerRequest(_UpdateCustomerRequestOptional):
    customer_id: str

class _PageCustomersRequestOptional(TypedDict, total=False):
    page_size: int

class PageCustomersRequest(_PageCustomersRequestOptional):
    page_number: int

class _CreateOrderNewCustomerInputOptional(TypedDict, total=False):
    number: str
    receipt_number: str
    statement_descriptor: str
    statement_descriptor_prefix: str
    execute_payment: bool
    finalize: bool
    request_meta: CreateOrderNewCustomerInputRequestMeta
    checkout_settings: CreateOrderNewCustomerInputCheckoutSettings
    invoice_settings: InvoiceSettingsInput
    payout_settings: OrderPayoutSettingsRequest
    custom_data: dict[str, str]
    billing_details: BillingDetailsInput
    shipping: ShippingInput

class CreateOrderNewCustomerInput(_CreateOrderNewCustomerInputOptional):
    customer_data: CustomerDataInput
    line_items: list[LineItemInput]

class _CustomerDataInputOptional(TypedDict, total=False):
    reference: str
    custom_data: dict[str, Any]

class CustomerDataInput(_CustomerDataInputOptional):
    name: str
    email_address: str
    phone_number: str

class CreateOrderNewCustomerInputRequestMeta(TypedDict, total=False):
    idempotency_key: str

class CreateOrderNewCustomerInputCheckoutSettings(TypedDict, total=False):
    redirect_url: str
    cancel_url: str

class InvoiceSettingsInput(TypedDict, total=False):
    number: str
    memo: str
    footer: str
    custom_data: dict[str, str]

class OrderPayoutSettingsRequest(TypedDict, total=False):
    destination: OrderPayoutSettingsRequestDestination
    enable_fx: Literal[False]

class OrderPayoutSettingsRequestDestination(TypedDict):
    financial_account_id: str

class ProductLineItemInput(TypedDict):
    type: Literal['product']
    product: ProductDetailsInput

class _InlineProductDetailsInputOptional(TypedDict, total=False):
    about: str
    custom_data: dict[str, Any]
    reference: str
    tax_code: str

class InlineProductDetailsInput(_InlineProductDetailsInputOptional):
    name: str
    price: MoneyInput
    quantity: int
    type: Literal['physical', 'digital', 'service', 'voucher', 'custom', 'cause']

class MoneyInput(TypedDict):
    currency: str
    value: int

class CatalogProductWithPriceDataInput(TypedDict):
    price: MoneyInput
    product_id: str
    quantity: int

class CatalogProductWithPriceReferenceInput(TypedDict):
    price_id: str
    product_id: str
    quantity: int

class FeeLineItemInput(TypedDict):
    type: Literal['fee']
    fee: FeeDetailsInput

class _FeeDetailsInputOptional(TypedDict, total=False):
    id: str
    label: str
    tax_code: str
    description: str
    custom_data: dict[str, Any]

class FeeDetailsInput(_FeeDetailsInputOptional):
    amount: MoneyInput

class ShippingLineItemInput(TypedDict):
    type: Literal['shipping']
    shipping: ShippingDetailsInput

class _ShippingDetailsInputOptional(TypedDict, total=False):
    id: str
    tax_code: str
    custom_data: dict[str, Any]

class ShippingDetailsInput(_ShippingDetailsInputOptional):
    fee: MoneyInput

class _BillingDetailsInputOptional(TypedDict, total=False):
    address: AddressInput

class BillingDetailsInput(_BillingDetailsInputOptional):
    name: str
    email_address: str
    phone_number: str

class _AddressInputOptional(TypedDict, total=False):
    line2: str
    region: str
    district: str
    post_code: str

class AddressInput(_AddressInputOptional):
    name: str
    phone_number: str
    line1: str
    town: str
    country: str

class ShippingInput(TypedDict):
    address: AddressInput

class _CreateOrderExistingCustomerInputOptional(TypedDict, total=False):
    payment_method_id: str
    receipt_number: str
    statement_descriptor: str
    statement_descriptor_prefix: str
    execute_payment: bool
    finalize: bool
    request_meta: CreateOrderExistingCustomerInputRequestMeta
    checkout_settings: CreateOrderExistingCustomerInputCheckoutSettings
    invoice_settings: InvoiceSettingsInput
    payout_settings: OrderPayoutSettingsRequest
    custom_data: dict[str, str]
    billing_details: BillingDetailsInput
    shipping: ShippingInput

class CreateOrderExistingCustomerInput(_CreateOrderExistingCustomerInputOptional):
    customer_id: str
    line_items: list[LineItemInput]

class CreateOrderExistingCustomerInputRequestMeta(TypedDict, total=False):
    idempotency_key: str

class CreateOrderExistingCustomerInputCheckoutSettings(TypedDict, total=False):
    redirect_url: str
    cancel_url: str

class LookupOrderRequest(TypedDict):
    order_id: str

class _UpdateOrderRequestOptional(TypedDict, total=False):
    clear_payment_method: bool
    custom_data: dict[str, str]
    invoice_settings: InvoiceSettingsInput
    finalize: bool
    line_items: list[LineItemInput]
    number: str
    receipt_number: str
    payment_method_data: UpdateOrderRequestPaymentMethodData
    payment_method_id: str
    statement_descriptor: str
    statement_descriptor_prefix: str

class UpdateOrderRequest(_UpdateOrderRequestOptional):
    order_id: str

class _UpdateOrderRequestPaymentMethodDataOptional(TypedDict, total=False):
    mobile_money: UpdateOrderRequestPaymentMethodDataMobileMoney

class UpdateOrderRequestPaymentMethodData(_UpdateOrderRequestPaymentMethodDataOptional):
    type: Literal['mobile_money']

class UpdateOrderRequestPaymentMethodDataMobileMoney(TypedDict):
    network: Literal['airtel', 'mtn', 'telecel', 'vodafone']
    account_number: str

class _PayOrderRequestOptional(TypedDict, total=False):
    payment_method_data: PaymentMethodDataInput
    payment_method_id: str
    paid_out_of_band: bool

class PayOrderRequest(_PayOrderRequestOptional):
    order_id: str

class _PaymentMethodDataInputOptional(TypedDict, total=False):
    mobile_money: PaymentMethodDataInputMobileMoney

class PaymentMethodDataInput(_PaymentMethodDataInputOptional):
    type: Literal['mobile_money']

class PaymentMethodDataInputMobileMoney(TypedDict):
    network: Literal['airtel', 'mtn', 'telecel', 'vodafone']
    account_number: str

class ConfirmPaymentRequest(TypedDict):
    order_id: str
    payment_id: str
    confirmation_id: str
    token: str

class RequestConfirmationRequest(TypedDict):
    order_id: str

class _CancelOrderRequestOptional(TypedDict, total=False):
    reason: str
    execute_refund: bool

class CancelOrderRequest(_CancelOrderRequestOptional):
    order_id: str

class FinalizeOrderRequest(TypedDict):
    order_id: str

class _CompleteOrderRequestOptional(TypedDict, total=False):
    paid_out_of_band: bool

class CompleteOrderRequest(_CompleteOrderRequestOptional):
    order_id: str

class OrderDocumentDeliveryRequest(TypedDict):
    order_id: str

class _PageOrdersRequestOptional(TypedDict, total=False):
    page_number: int
    customer_id: str

class PageOrdersRequest(_PageOrdersRequestOptional):
    page_size: int

class _CreateRefundRequestOptional(TypedDict, total=False):
    custom_data: dict[str, str]
    reason_details: str
    reference: str
    request_meta: RefundRequestMetaInput

class CreateRefundRequest(_CreateRefundRequestOptional):
    line_items: list[CreateRefundLineItemInput]
    order_id: str
    reason: RefundReasonInput

class _CreateRefundLineItemInputOptional(TypedDict, total=False):
    reason: RefundReasonInput
    reason_details: str

class CreateRefundLineItemInput(_CreateRefundLineItemInputOptional):
    order_line_item_id: str
    refund_amount: RefundMoneyInput

class RefundMoneyInput(TypedDict):
    currency: str
    value: int

class RefundRequestMetaInput(TypedDict, total=False):
    idempotency_key: str

class _CancelRefundRequestOptional(TypedDict, total=False):
    request_meta: RefundRequestMetaInput

class CancelRefundRequest(_CancelRefundRequestOptional):
    refund_id: str

class LookupRefundRequest(TypedDict):
    refund_id: str

class _PageRefundsRequestOptional(TypedDict, total=False):
    page_size: int

class PageRefundsRequest(_PageRefundsRequestOptional):
    page_number: int

class _CreateApplicationRequestOptional(TypedDict, total=False):
    alias: str
    description: str
    legal_entity_type: str
    placement_parent_application_id: str
    relationship_policy: CreateApplicationRequestRelationshipPolicy

class CreateApplicationRequest(_CreateApplicationRequestOptional):
    name: str

class CreateApplicationRequestRelationshipPolicy(TypedDict, total=False):
    child_standing: str
    management: Literal['parent', 'child']
    credentials: Literal['child', 'parent']

class UpdateApplicationRequest(TypedDict, total=False):
    name: str
    alias: str
    description: str
    legal_entity_type: str

class GenerateSecretKeyRequest(TypedDict, total=False):
    label: str

class PageSecretKeysRequest(TypedDict, total=False):
    page: int
    number: int
    size: int

class LookupSecretKeyRequest(TypedDict):
    secret_key_id: str

class UpdateSecretKeyRequest(TypedDict):
    label: str
    secret_key_id: str

class DestroySecretKeyRequest(TypedDict):
    secret_key_id: str

class _SecretKeyUsageRequestOptional(TypedDict, total=False):
    number: int
    page: int
    size: int

class SecretKeyUsageRequest(_SecretKeyUsageRequestOptional):
    secret_key_id: str

class _FinancialAccountWalletRequestOptional(TypedDict, total=False):
    custom_data: dict[str, Any]
    description: str
    pull_configuration: FinancialAccountWalletRequestPullConfiguration
    push_configuration: FinancialAccountWalletRequestPushConfiguration

class FinancialAccountWalletRequest(_FinancialAccountWalletRequestOptional):
    currency: str
    label: str
    owner: FinancialAccountOwnerInput
    reference: str
    type: Literal['wallet']
    wallet: FinancialAccountWalletRequestWallet

class FinancialAccountOwnerInput(TypedDict):
    name: str
    address: FinancialAccountOwnerInputAddress

class _FinancialAccountOwnerInputAddressOptional(TypedDict, total=False):
    city: str
    line_1: str
    line_2: str
    name: str
    phone: str
    post_code: str
    region: str

class FinancialAccountOwnerInputAddress(_FinancialAccountOwnerInputAddressOptional):
    country: str

class FinancialAccountWalletRequestPullConfiguration(TypedDict, total=False):
    enabled: bool

class FinancialAccountWalletRequestPushConfiguration(TypedDict, total=False):
    enabled: bool

class FinancialAccountWalletRequestWallet(TypedDict):
    type: Literal['mobile_money']
    mobile_money: FinancialAccountWalletRequestWalletMobileMoney

class FinancialAccountWalletRequestWalletMobileMoney(TypedDict):
    account_number: str
    network: Literal['airtel', 'mtn', 'telecel', 'vodafone']

class _FinancialAccountBankRequestOptional(TypedDict, total=False):
    custom_data: dict[str, Any]
    description: str
    owner: FinancialAccountOwnerInput
    pull_configuration: FinancialAccountBankRequestPullConfiguration
    push_configuration: FinancialAccountBankRequestPushConfiguration

class FinancialAccountBankRequest(_FinancialAccountBankRequestOptional):
    currency: str
    label: str
    reference: str
    type: Literal['bank_account']
    bank_account: FinancialAccountBankRequestBankAccount

class FinancialAccountBankRequestPullConfiguration(TypedDict, total=False):
    enabled: bool

class FinancialAccountBankRequestPushConfiguration(TypedDict, total=False):
    enabled: bool

class FinancialAccountBankRequestBankAccount(TypedDict):
    type: Literal['ghana_bank_account']
    ghana_bank_account: Any | Any

class _FinancialAccountDoshRequestOptional(TypedDict, total=False):
    custom_data: dict[str, Any]
    description: str
    pull_configuration: FinancialAccountDoshRequestPullConfiguration
    push_configuration: FinancialAccountDoshRequestPushConfiguration

class FinancialAccountDoshRequest(_FinancialAccountDoshRequestOptional):
    currency: str
    label: str
    owner: FinancialAccountOwnerInput
    reference: str
    type: Literal['dosh_account']
    dosh_account: dict[str, Any]

class FinancialAccountDoshRequestPullConfiguration(TypedDict, total=False):
    enabled: bool

class FinancialAccountDoshRequestPushConfiguration(TypedDict, total=False):
    enabled: bool

class FinancialAccountIDRequest(TypedDict):
    account_id: str

class _FinancialAccountPageRequestOptional(TypedDict, total=False):
    page_size: int

class FinancialAccountPageRequest(_FinancialAccountPageRequestOptional):
    page_number: int

class _FinancialAccountUpdateRequestOptional(TypedDict, total=False):
    custom_data: dict[str, Any]
    description: str
    label: str
    owner: FinancialAccountOwnerUpdateInput
    reference: str

class FinancialAccountUpdateRequest(_FinancialAccountUpdateRequestOptional):
    account_id: str

class FinancialAccountOwnerUpdateInput(TypedDict, total=False):
    name: str
    address: FinancialAccountOwnerUpdateInputAddress

class FinancialAccountOwnerUpdateInputAddress(TypedDict, total=False):
    city: str
    country: str
    line_1: str
    line_2: str
    name: str
    phone: str
    post_code: str
    region: str

class _FinancialAccountDisableRequestOptional(TypedDict, total=False):
    unset_as_payout_destination: bool

class FinancialAccountDisableRequest(_FinancialAccountDisableRequestOptional):
    account_id: str

class _FinancialAccountEnablePullRequestOptional(TypedDict, total=False):
    ip_address: str
    user_agent: str

class FinancialAccountEnablePullRequest(_FinancialAccountEnablePullRequestOptional):
    account_id: str

class LookupBalancesRequest(TypedDict):
    pass

class LookupBalanceTransactionRequest(TypedDict):
    transaction_id: str

class PageBalanceTransactionsRequest(TypedDict):
    page_number: int
    page_size: int

class _SchedulePayoutRequestOptional(TypedDict, total=False):
    execute_after: str
    max_amount: int

class SchedulePayoutRequest(_SchedulePayoutRequestOptional):
    destination_id: str
    reference: str

class LookupPayoutRequest(TypedDict):
    payout_id: str

class SetPayoutDestinationsRequest(TypedDict):
    destinations: dict[str, str]

class GetPayoutSettingsRequest(TypedDict):
    pass

class DisableAutomaticPayoutsRequest(TypedDict):
    pass

class EnableAutomaticPayoutsRequest(TypedDict):
    pass

class _PagePayoutsRequestOptional(TypedDict, total=False):
    page_size: int

class PagePayoutsRequest(_PagePayoutsRequestOptional):
    page_number: int

class CancelPayoutRequest(TypedDict):
    payout_id: str

class LookupFileRequest(TypedDict):
    file_id: str

class PageFilesRequest(TypedDict, total=False):
    purpose: str
    status: Literal['uploading', 'processing', 'available', 'failed', 'deleted']
    page_number: int
    page_size: int
    created_after: str
    created_before: str

class _FileContentsRequestOptional(TypedDict, total=False):
    disposition: Literal['attachment', 'inline']
    delivery: Literal['stream', 'redirect']

class FileContentsRequest(_FileContentsRequestOptional):
    file_id: str

class DeleteFileRequest(TypedDict):
    file_id: str

class _CreateFileLinkRequestOptional(TypedDict, total=False):
    delivery: FileLinkDeliveryInput
    access: FileLinkAccessRequest
    created_by: FileActorInput
    custom_data: dict[str, str]
    expires_at: str

class CreateFileLinkRequest(_CreateFileLinkRequestOptional):
    file_id: str

class FileLinkDeliveryInput(TypedDict, total=False):
    mode: Literal['redirect', 'download', 'inline']
    filename: str
    content_type: str
    disposition: str

class FileLinkAccessRequest(TypedDict, total=False):
    max_accesses: int
    allow_download: bool
    allowed_origins: list[str]
    allowed_ip_ranges: list[str]

class FileActorInput(TypedDict, total=False):
    email: str
    id: str
    name: str
    type: str

class LookupFileLinkRequest(TypedDict):
    id: str

class PageFileLinksRequest(TypedDict, total=False):
    file_id: str
    status: Literal['active', 'revoked', 'expired', 'disabled']
    page_number: int
    page_size: int

class _RevokeFileLinkRequestOptional(TypedDict, total=False):
    revoked_by: FileActorInput

class RevokeFileLinkRequest(_RevokeFileLinkRequestOptional):
    id: str

class _CreateUploadRequestRequestOptional(TypedDict, total=False):
    constraints: UploadRequestConstraintsInput
    display: UploadRequestDisplayInput
    subject: FilePartyInput
    recipient: FilePartyInput
    resource: FileResourceInput
    requester: FileActorInput
    attempts: UploadRequestAttemptsRequest
    custom_data: dict[str, str]
    expires_at: str

class CreateUploadRequestRequest(_CreateUploadRequestRequestOptional):
    purpose: str

class UploadRequestConstraintsInput(TypedDict, total=False):
    min_size: int
    max_size: int
    exact_size: int
    content_types: list[str]
    extensions: list[str]
    filename: str

class UploadRequestDisplayInput(TypedDict, total=False):
    title: str
    description: str
    help_text: str

class FilePartyInput(TypedDict, total=False):
    type: str
    id: str
    name: str
    email: str

class FileResourceInput(TypedDict, total=False):
    type: str
    id: str
    name: str

class UploadRequestAttemptsRequest(TypedDict, total=False):
    max_attempts: int

class LookupUploadRequestRequest(TypedDict):
    id: str

class PageUploadRequestsRequest(TypedDict, total=False):
    purpose: str
    status: Literal['pending', 'uploading', 'fulfilled', 'expired', 'canceled', 'failed']
    resource: FileResourceInput
    page_number: int
    page_size: int

class _CancelUploadRequestRequestOptional(TypedDict, total=False):
    canceled_by: FileActorInput

class CancelUploadRequestRequest(_CancelUploadRequestRequestOptional):
    id: str

class _ReviewUploadRequestAttemptByIDRequestOptional(TypedDict, total=False):
    public_message: str
    reasons: list[UploadRequestReviewReasonInput]

class ReviewUploadRequestAttemptByIDRequest(_ReviewUploadRequestAttemptByIDRequestOptional):
    attempt_id: str
    decision: Literal['approved', 'rejected']
    id: str

class _UploadRequestReviewReasonInputOptional(TypedDict, total=False):
    param: str

class UploadRequestReviewReasonInput(_UploadRequestReviewReasonInputOptional):
    code: str
    message: str

class _ReviewUploadRequestAttemptByOrdinalRequestOptional(TypedDict, total=False):
    public_message: str
    reasons: list[UploadRequestReviewReasonInput]

class ReviewUploadRequestAttemptByOrdinalRequest(_ReviewUploadRequestAttemptByOrdinalRequestOptional):
    attempt_ordinal: int
    decision: Literal['approved', 'rejected']
    id: str

class _FileReferenceReconcileRequestOptional(TypedDict, total=False):
    references: list[FileReferenceInput]

class FileReferenceReconcileRequest(_FileReferenceReconcileRequestOptional):
    resource_type: str
    resource_id: str

class _FileReferenceInputOptional(TypedDict, total=False):
    reference: str
    reference_kind: str
    purpose: str

class FileReferenceInput(_FileReferenceInputOptional):
    file_id: str
    field: str

class _TokenizeMobileMoneyPaymentMethodRequestOptional(TypedDict, total=False):
    custom_data: dict[str, str]

class TokenizeMobileMoneyPaymentMethodRequest(_TokenizeMobileMoneyPaymentMethodRequestOptional):
    customer_id: str
    type: Literal['mobile_money']
    mobile_money: TokenizeMobileMoneyPaymentMethodRequestMobileMoney
    owner: PaymentMethodOwnerInput

class TokenizeMobileMoneyPaymentMethodRequestMobileMoney(TypedDict):
    account_number: str
    network: Literal['airtel', 'mtn', 'telecel', 'vodafone']

class PaymentMethodOwnerInput(TypedDict):
    address: PaymentMethodOwnerInputAddress
    name: str

class _PaymentMethodOwnerInputAddressOptional(TypedDict, total=False):
    city: str
    line1: str
    line2: str
    name: str
    phone_number: str
    post_code: str
    region: str

class PaymentMethodOwnerInputAddress(_PaymentMethodOwnerInputAddressOptional):
    country: str

class LookupPaymentMethodRequest(TypedDict):
    payment_method_id: str

class PaymentMethodPageRequest(TypedDict, total=False):
    customer_id: str
    page_number: int
    page_size: int

class _UpdatePaymentMethodRequestOptional(TypedDict, total=False):
    custom_data: dict[str, str | None]
    active: bool
    archived: bool
    owner: UpdatePaymentMethodRequestOwner

class UpdatePaymentMethodRequest(_UpdatePaymentMethodRequestOptional):
    payment_method_id: str

class UpdatePaymentMethodRequestOwner(TypedDict, total=False):
    name: str
    address: UpdatePaymentMethodRequestOwnerAddress

class UpdatePaymentMethodRequestOwnerAddress(TypedDict, total=False):
    city: str
    country: str
    line1: str
    line2: str
    name: str
    phone_number: str
    post_code: str
    region: str

class ActivatePaymentMethodRequest(TypedDict):
    payment_method_id: str

class DisactivatePaymentMethodRequest(TypedDict):
    payment_method_id: str

class ArchivePaymentMethodRequest(TypedDict):
    payment_method_id: str

class UnarchivePaymentMethodRequest(TypedDict):
    payment_method_id: str

class GetPaymentMethodSettingsRequest(TypedDict):
    pass

class _CreateProductRequestOptional(TypedDict, total=False):
    reference: str
    description: str
    about: str
    tax_code: str
    category: str
    shipment: ProductShipmentInput
    dimensions: ProductDimensionsInput
    unit_dimension: str
    media: ProductMediaInput
    attributes: list[ProductAttributeInput]
    publish: bool
    custom_data: dict[str, str]

class CreateProductRequest(_CreateProductRequestOptional):
    type: Literal['physical', 'digital', 'service', 'voucher', 'custom', 'cause']
    name: str

class ProductShipmentInput(TypedDict):
    type: Literal['delivery', 'download', 'render', 'stream']

class ProductDimensionsInput(TypedDict, total=False):
    physical: ProductDimensionsInputPhysical
    digital: ProductDimensionsInputDigital
    custom: ProductDimensionsInputCustom

class ProductDimensionsInputPhysical(TypedDict, total=False):
    weight_unit: str
    weight: float
    size: float
    volume_unit: str
    volume: float
    length: float
    height: float
    width: float

class ProductDimensionsInputDigital(TypedDict, total=False):
    bytes: float
    size_unit: str
    size: float

class ProductDimensionsInputCustom(TypedDict, total=False):
    size_unit: str
    size: float
    details: dict[str, str]

class ProductMediaInput(TypedDict, total=False):
    hero_image: str
    thumbnail: str
    web_page_url: str
    brand_logo: str
    infographic: str
    promo_video: str
    demo_video: str
    gallery: list[str]
    downloads: list[str]

class ProductAttributeInput(TypedDict):
    name: str
    value: str

class _AddProductPriceRequestOptional(TypedDict, total=False):
    label: str
    about: str

class AddProductPriceRequest(_AddProductPriceRequestOptional):
    product_id: str
    amount: AddProductPriceRequestAmount

class AddProductPriceRequestAmount(TypedDict):
    currency: str
    value: int

class LookupProductRequest(TypedDict):
    product_id: str

class _UpdateProductRequestOptional(TypedDict, total=False):
    type: Literal['physical', 'digital', 'service', 'voucher', 'custom', 'cause']
    name: str
    description: str
    about: str
    tax_code: str
    category: str
    shipment: ProductShipmentInput
    dimensions: ProductDimensionsInput
    unit_dimension: str
    media: ProductMediaInput
    images: list[str]
    attributes: list[ProductAttributeInput]
    custom_data: dict[str, str]

class UpdateProductRequest(_UpdateProductRequestOptional):
    product_id: str

class ProductActionRequest(TypedDict):
    product_id: str

class _PageProductsRequestOptional(TypedDict, total=False):
    page_size: int

class PageProductsRequest(_PageProductsRequestOptional):
    page_number: int

class _CreatePurchaseIntentRequestOptional(TypedDict, total=False):
    product: CreatePurchaseIntentRequestProduct
    product_id: str
    price: CreatePurchaseIntentRequestPrice
    price_id: str
    usage: CreatePurchaseIntentRequestUsage
    expires_at: str

class CreatePurchaseIntentRequest(_CreatePurchaseIntentRequestOptional):
    quantity: CreatePurchaseIntentRequestQuantity

class _CreatePurchaseIntentRequestProductOptional(TypedDict, total=False):
    variant_set_id: str

class CreatePurchaseIntentRequestProduct(_CreatePurchaseIntentRequestProductOptional):
    id: str

class CreatePurchaseIntentRequestPrice(TypedDict, total=False):
    id: str
    nominal: CreatePurchaseIntentRequestPriceNominal
    original: CreatePurchaseIntentRequestPriceOriginal
    original_id: str

class CreatePurchaseIntentRequestPriceNominal(TypedDict):
    currency: str
    value: int

class CreatePurchaseIntentRequestPriceOriginal(TypedDict, total=False):
    id: str
    nominal: CreatePurchaseIntentRequestPriceOriginalNominal

class CreatePurchaseIntentRequestPriceOriginalNominal(TypedDict):
    currency: str
    value: int

class _CreatePurchaseIntentRequestQuantityOptional(TypedDict, total=False):
    max: int

class CreatePurchaseIntentRequestQuantity(_CreatePurchaseIntentRequestQuantityOptional):
    min: int

class CreatePurchaseIntentRequestUsage(TypedDict, total=False):
    single_use: bool
    multi_use: bool

class UpdatePurchaseIntentRequest(TypedDict, total=False):
    expires_at: str | None
    id: str
    quantity: UpdatePurchaseIntentRequestQuantity
    purchase_intent_id: str
    reactivate: bool

class _UpdatePurchaseIntentRequestQuantityOptional(TypedDict, total=False):
    max: int

class UpdatePurchaseIntentRequestQuantity(_UpdatePurchaseIntentRequestQuantityOptional):
    min: int

class CancelPurchaseIntentRequest(TypedDict, total=False):
    id: str
    purchase_intent_id: str

class LookupPurchaseIntentRequest(TypedDict):
    id: str

class PagePurchaseIntentsRequest(TypedDict):
    page_number: int
    page_size: int

class _CreatePriceRequestOptional(TypedDict, total=False):
    product_id: str
    label: str
    about: str

class CreatePriceRequest(_CreatePriceRequestOptional):
    amount: MoneyInput

class LookupPriceRequest(TypedDict):
    price_id: str

class PricePageRequest(TypedDict, total=False):
    page_number: int
    page_size: int
    product_id: str

class _UpdatePriceRequestOptional(TypedDict, total=False):
    label: str
    about: str

class UpdatePriceRequest(_UpdatePriceRequestOptional):
    price_id: str

class PriceActionRequest(TypedDict):
    price_id: str

class ListCountrySpecsRequest(TypedDict):
    pass

ChimeInlineRecipientInput: TypeAlias = ChimeInlineRecipientInputVariant1 | ChimeInlineRecipientInputVariant2
ChimeRecipientInput: TypeAlias = ChimeInlineRecipientInput | ChimeSavedCustomerRecipientInput
MessageTemplateVariablesInput: TypeAlias = dict[str, Any]
MessageTemplateAttachmentIDsInput: TypeAlias = list[str]
CreateMessageTemplateRequest: TypeAlias = CreateSMSMessageTemplateRequest | CreateEmailMessageTemplateRequest
ProductDetailsInput: TypeAlias = InlineProductDetailsInput | CatalogProductWithPriceDataInput | CatalogProductWithPriceReferenceInput
LineItemInput: TypeAlias = ProductLineItemInput | FeeLineItemInput | ShippingLineItemInput
CreateOrderRequest: TypeAlias = CreateOrderNewCustomerInput | CreateOrderExistingCustomerInput
RefundReasonInput: TypeAlias = Literal['requested_by_customer', 'duplicate', 'fraudulent', 'order_canceled', 'item_returned', 'item_damaged', 'item_not_received', 'item_not_as_described', 'custom']
FinancialAccountCreateRequest: TypeAlias = FinancialAccountWalletRequest | FinancialAccountBankRequest | FinancialAccountDoshRequest
ReviewUploadRequestAttemptRequest: TypeAlias = ReviewUploadRequestAttemptByIDRequest | ReviewUploadRequestAttemptByOrdinalRequest

__all__ = [
    'ActivatePaymentMethodRequest',
    'AddProductPriceRequest',
    'AddProductPriceRequestAmount',
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
    'CreatePriceRequest',
    'CreateProductRequest',
    'CreatePurchaseIntentRequest',
    'CreatePurchaseIntentRequestPrice',
    'CreatePurchaseIntentRequestPriceNominal',
    'CreatePurchaseIntentRequestPriceOriginal',
    'CreatePurchaseIntentRequestPriceOriginalNominal',
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
    'MoneyInput',
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
    'RefundMoneyInput',
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
