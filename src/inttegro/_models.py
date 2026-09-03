"""Generated typed API response models. Do not edit by hand."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal, TypeAlias

from ._model_base import ApiModel
from .money import Amount
from .price_types import Price

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class InitiateOTPResponse(ApiModel):
    transaction: OTPTransaction = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class OTPTransaction(ApiModel):
    cancel_reason: str | None = field(init=False)
    canceled_at: str | None = field(init=False)
    expires_at: str = field(init=False)
    full_message: str = field(init=False)
    id: str = field(init=False)
    initiated_at: str = field(init=False)
    status: Literal['canceled', 'expired', 'pending', 'pending_delivery', 'pending_verification', 'verified'] = field(init=False)
    transmission: OTPTransmission | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class OTPTransmission(ApiModel):
    recipient: str = field(init=False)
    sender_id: str = field(init=False)
    sent_at: str | None = field(init=False)
    sent_via: Literal['sms'] | None = field(init=False)
    status: Literal['delivered', 'failed', 'submitted'] | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class OTPVerification(ApiModel):
    transaction: OTPTransaction = field(init=False)
    verification_attempt: OTPVerificationAttempt = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class OTPVerificationAttempt(ApiModel):
    attempted_at: str = field(init=False)
    id: str = field(init=False)
    presented_token: str = field(init=False)
    recipient: str = field(init=False)
    result: OTPVerificationAttemptResult = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class OTPVerificationAttemptResult(ApiModel):
    detail: str | None = field(init=False)
    verdict: Literal['fail', 'pass'] = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class LookupOTPResponse(ApiModel):
    transaction: OTPTransaction = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ChimeResponse(ApiModel):
    chime: Chime | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Chime(ApiModel):
    created_at: str = field(init=False)
    custom_data: dict[str, str] | None = field(init=False)
    customer_id: str | None = field(init=False)
    email: ChimeEmailMessage | None = field(init=False)
    full_message: str = field(init=False)
    id: str = field(init=False)
    idempotency_key: str | None = field(init=False)
    purpose: str | None = field(init=False)
    recipient: ChimeRecipient = field(init=False)
    sender_id: str = field(init=False)
    transmission: ChimeTransmission | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ChimeEmailMessage(ApiModel):
    subject: str | None = field(init=False)
    text: str | None = field(init=False)
    html: str | None = field(init=False)
    from_: ChimeEmailMailbox | None = field(init=False, metadata={"wire_name": 'from'})
    reply_to: ChimeEmailMailbox | None = field(init=False)
    headers: dict[str, str] | None = field(init=False)
    safety: ChimeEmailSafetyResult | None = field(init=False)
    schema: ChimeEmailSchemaMarkup | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ChimeEmailMailbox(ApiModel):
    name: str | None = field(init=False)
    address: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ChimeEmailSafetyResult(ApiModel):
    status: Literal['allowed', 'rejected', 'quarantined'] | None = field(init=False)
    reason_codes: list[str] | None = field(init=False)
    sanitized_html: str | None = field(init=False)
    normalized_text: str | None = field(init=False)
    links: list[ChimeEmailScannedLink] | None = field(init=False)
    scanner: str | None = field(init=False)
    content_hash: str | None = field(init=False)
    quarantine_notes: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ChimeEmailScannedLink(ApiModel):
    raw: str | None = field(init=False)
    scheme: str | None = field(init=False)
    host: str | None = field(init=False)
    status: Literal['allowed', 'rejected', 'quarantined'] | None = field(init=False)
    reason: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ChimeEmailSchemaMarkup(ApiModel):
    kind: Literal['gmail_view_action', 'schema_org_order', 'schema_org_invoice'] | None = field(init=False)
    json_ld: dict[str, Any] | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ChimeRecipient(ApiModel):
    type: Literal['phone', 'email'] = field(init=False)
    name: str | None = field(init=False)
    phone: ChimeRecipientPhone | None = field(init=False)
    email: ChimeRecipientEmail | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ChimeRecipientPhone(ApiModel):
    number: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ChimeRecipientEmail(ApiModel):
    address: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ChimeTransmission(ApiModel):
    address: str = field(init=False)
    created_at: str = field(init=False)
    delivered_at: str | None = field(init=False)
    email_events: list[ChimeEmailEvent] | None = field(init=False)
    email_failure_code: str | None = field(init=False)
    email_failure_reason: str | None = field(init=False)
    email_status: str | None = field(init=False)
    error: str | None = field(init=False)
    failed_at: str | None = field(init=False)
    gateway: str = field(init=False)
    gateway_message_id: str | None = field(init=False)
    id: str = field(init=False)
    initialized_at: str = field(init=False)
    last_email_event_at: str | None = field(init=False)
    mechanism: Literal['sms', 'email'] = field(init=False)
    sent_at: str | None = field(init=False)
    sent_via: Literal['sms', 'email'] | None = field(init=False)
    status: str = field(init=False)
    suppressed_at: str | None = field(init=False)
    suppression_reason: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ChimeEmailEvent(ApiModel):
    bounce_sub_type: str | None = field(init=False)
    bounce_type: str | None = field(init=False)
    complaint_sub_type: str | None = field(init=False)
    id: str = field(init=False)
    occurred_at: str = field(init=False)
    provider: str = field(init=False)
    provider_message_id: str = field(init=False)
    reason: str | None = field(init=False)
    reason_code: str | None = field(init=False)
    recipient: str | None = field(init=False)
    source: str | None = field(init=False)
    suppress_recipient: bool | None = field(init=False)
    temporary: bool | None = field(init=False)
    type: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PageChimesResponse(ApiModel):
    page: ChimePage | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ChimePage(ApiModel):
    number: int = field(init=False)
    size: int = field(init=False)
    chimes: list[Chime] = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ScheduleResponse(ApiModel):
    scheduled_chime: ScheduleCreationDetail | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ScheduleCreationDetail(ApiModel):
    created_at: str = field(init=False)
    customer_ids: list[str] | None = field(init=False)
    email: ChimeEmailMessage | None = field(init=False)
    executed_at: str | None = field(init=False)
    full_message: str = field(init=False)
    id: str = field(init=False)
    idempotency_key: str | None = field(init=False)
    purpose: str | None = field(init=False)
    recipients: list[str] | None = field(init=False)
    send_after: str = field(init=False)
    sender_id: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class BroadcastResponse(ApiModel):
    broadcast: BroadcastCreationDetail | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class BroadcastCreationDetail(ApiModel):
    content: str = field(init=False)
    created_at: str = field(init=False)
    customer_ids: list[str] | None = field(init=False)
    email: ChimeEmailMessage | None = field(init=False)
    id: str = field(init=False)
    idempotency_key: str | None = field(init=False)
    purpose: str | None = field(init=False)
    recipients: list[str] = field(init=False)
    send_after: str = field(init=False)
    sender_id: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ScheduleLookupResponse(ApiModel):
    scheduled_chime: ScheduleDetail | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ScheduleDetail(ApiModel):
    chime_ids: list[str] | None = field(init=False)
    content: str = field(init=False)
    created_at: str = field(init=False)
    customer_ids: list[str] | None = field(init=False)
    email: ChimeEmailMessage | None = field(init=False)
    errors: list[ScheduleError] | None = field(init=False)
    executed_at: str | None = field(init=False)
    id: str = field(init=False)
    idempotency_key: str | None = field(init=False)
    purpose: str | None = field(init=False)
    recipients: list[str] = field(init=False)
    send_after: str = field(init=False)
    sender_id: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ScheduleError(ApiModel):
    recipient: str | None = field(init=False)
    fix_code: str | None = field(init=False)
    type: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ScheduleCancelResponse(ApiModel):
    scheduled_chime: ScheduleCancelDetail | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ScheduleCancelDetail(ApiModel):
    chime_ids: list[str] | None = field(init=False)
    content: str = field(init=False)
    created_at: str = field(init=False)
    customer_ids: list[str] | None = field(init=False)
    email: ChimeEmailMessage | None = field(init=False)
    errors: list[ScheduleError] | None = field(init=False)
    executed_at: str | None = field(init=False)
    id: str = field(init=False)
    idempotency_key: str | None = field(init=False)
    purpose: str | None = field(init=False)
    recipients: list[str] = field(init=False)
    send_after: str = field(init=False)
    sender_id: str = field(init=False)
    canceled_at: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class LookupBroadcastResponse(ApiModel):
    broadcast: BroadcastDetail | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class BroadcastDetail(ApiModel):
    chime_ids: list[str] | None = field(init=False)
    content: str = field(init=False)
    created_at: str = field(init=False)
    customer_ids: list[str] | None = field(init=False)
    email: ChimeEmailMessage | None = field(init=False)
    errors: list[BroadcastError] | None = field(init=False)
    executed_at: str | None = field(init=False)
    id: str = field(init=False)
    idempotency_key: str | None = field(init=False)
    purpose: str | None = field(init=False)
    recipients: list[str] = field(init=False)
    send_after: str = field(init=False)
    sender_id: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class BroadcastError(ApiModel):
    recipient: str | None = field(init=False)
    fix_code: str | None = field(init=False)
    type: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class BroadcastCancelResponse(ApiModel):
    broadcast: BroadcastCancelDetail | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class BroadcastCancelDetail(ApiModel):
    chime_ids: list[str] | None = field(init=False)
    content: str = field(init=False)
    created_at: str = field(init=False)
    customer_ids: list[str] | None = field(init=False)
    email: ChimeEmailMessage | None = field(init=False)
    errors: list[BroadcastError] | None = field(init=False)
    executed_at: str | None = field(init=False)
    id: str = field(init=False)
    idempotency_key: str | None = field(init=False)
    purpose: str | None = field(init=False)
    recipients: list[str] = field(init=False)
    send_after: str = field(init=False)
    sender_id: str = field(init=False)
    canceled_at: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class MessageTemplateEnvelope(ApiModel):
    message_template: MessageTemplate = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class MessageTemplate(ApiModel):
    id: str = field(init=False)
    name: str = field(init=False)
    about: str | None = field(init=False)
    channel: Literal['sms', 'email'] = field(init=False)
    purpose: str = field(init=False)
    locale: str = field(init=False)
    status: Literal['draft', 'published', 'archived'] = field(init=False)
    version: int = field(init=False)
    published_version: int | None = field(init=False)
    draft_version: int = field(init=False)
    has_unpublished_changes: bool = field(init=False)
    variables: list[MessageTemplateVariable] | None = field(init=False)
    sms: MessageTemplateSMSContent | None = field(init=False)
    email: MessageTemplateEmailContent | None = field(init=False)
    attachments: MessageTemplateAttachmentIDs | None = field(init=False)
    created_at: str = field(init=False)
    updated_at: str = field(init=False)
    published_at: str | None = field(init=False)
    archived_at: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class MessageTemplateVariable(ApiModel):
    about: str | None = field(init=False)
    default: Any | None = field(init=False)
    items: list[MessageTemplateVariableItem] | None = field(init=False)
    name: str = field(init=False)
    required: bool = field(init=False)
    type: Literal['string', 'number', 'integer', 'boolean', 'url', 'email', 'phone', 'date', 'datetime', 'array'] = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class MessageTemplateVariableItem(ApiModel):
    about: str | None = field(init=False)
    default: Any | None = field(init=False)
    name: str = field(init=False)
    required: bool = field(init=False)
    type: Literal['string', 'number', 'integer', 'boolean', 'url', 'email', 'phone', 'date', 'datetime'] = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class MessageTemplateSMSContent(ApiModel):
    message_template: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class MessageTemplateEmailContent(ApiModel):
    subject: str = field(init=False)
    html: str = field(init=False)
    from_: MessageTemplateMailbox | None = field(init=False, metadata={"wire_name": 'from'})
    reply_to: MessageTemplateMailbox | None = field(init=False)
    headers: dict[str, str] | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class MessageTemplateMailbox(ApiModel):
    address: str = field(init=False)
    name: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class MessageTemplatesPageEnvelope(ApiModel):
    page: MessageTemplatesPage = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class MessageTemplatesPage(ApiModel):
    number: int = field(init=False)
    size: int = field(init=False)
    message_templates: list[MessageTemplate] = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class MessageTemplatePreview(ApiModel):
    message_template: MessageTemplate = field(init=False)
    rendered: RenderedMessageTemplate = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class RenderedMessageTemplate(ApiModel):
    channel: Literal['sms', 'email'] = field(init=False)
    attachments: MessageTemplateAttachmentIDs | None = field(init=False)
    sms: RenderedSMSMessageTemplate | None = field(init=False)
    email: RenderedEmailMessageTemplate | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class RenderedSMSMessageTemplate(ApiModel):
    full_message: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class RenderedEmailMessageTemplate(ApiModel):
    subject: str = field(init=False)
    text: str = field(init=False)
    html: str | None = field(init=False)
    from_: MessageTemplateMailbox | None = field(init=False, metadata={"wire_name": 'from'})
    reply_to: MessageTemplateMailbox | None = field(init=False)
    headers: dict[str, str] | None = field(init=False)
    safety: MessageTemplateSafetyResult | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class MessageTemplateSafetyResult(ApiModel):
    content_hash: str = field(init=False)
    links: list[MessageTemplateScannedLink] | None = field(init=False)
    normalized_text: str = field(init=False)
    quarantine_notes: str | None = field(init=False)
    reason_codes: list[str] | None = field(init=False)
    sanitized_html: str | None = field(init=False)
    scanner: str = field(init=False)
    status: Literal['allowed', 'rejected', 'quarantined'] = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class MessageTemplateScannedLink(ApiModel):
    host: str | None = field(init=False)
    raw: str = field(init=False)
    reason: str | None = field(init=False)
    scheme: str = field(init=False)
    status: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class CustomerResponse(ApiModel):
    customer: Customer | None = field(init=False)
    error: Error | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Customer(ApiModel):
    balance: dict[str, CustomerBalanceValue] = field(init=False)
    billing_address: CustomerAddress | None = field(init=False)
    created_at: str = field(init=False)
    custom_data: dict[str, str] | None = field(init=False)
    email_address: str | None = field(init=False)
    guest: bool = field(init=False)
    id: str = field(init=False)
    name: str = field(init=False)
    phone_number: str | None = field(init=False)
    reference: str | None = field(init=False)
    shipping_address: CustomerAddress | None = field(init=False)
    suffix: str | None = field(init=False)
    title: str | None = field(init=False)
    updated_at: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class CustomerBalanceValue(ApiModel):
    as_of: str = field(init=False)
    available: Amount = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class CustomerAddress(ApiModel):
    city: str | None = field(init=False)
    country: str = field(init=False)
    line1: str | None = field(init=False)
    line2: str | None = field(init=False)
    name: str | None = field(init=False)
    phone_number: str | None = field(init=False)
    post_code: str | None = field(init=False)
    region: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Error(ApiModel):
    message: str | None = field(init=False)
    fix_code: str | None = field(init=False)
    detail: str | None = field(init=False)
    cause: str | None = field(init=False)
    type: str = field(init=False)
    code: str = field(init=False)
    url: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PageCustomersResponse(ApiModel):
    page: CustomerPage | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class CustomerPage(ApiModel):
    customers: list[Customer] = field(init=False)
    number: int = field(init=False)
    size: int = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class OrderEnvelope(ApiModel):
    order: Order = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Order(ApiModel):
    canceled_at: str | None = field(init=False)
    checkout_settings: OrderCheckoutSettings | None = field(init=False)
    completed_at: str | None = field(init=False)
    created_from: OrderCreatedFrom | None = field(init=False)
    custom_data: dict[str, str] | None = field(init=False)
    customer: OrderCustomer = field(init=False)
    expires_at: str | None = field(init=False)
    id: str = field(init=False)
    initiated_at: str = field(init=False)
    invoice: OrderInvoice | None = field(init=False)
    number: str | None = field(init=False)
    receipt_number: str | None = field(init=False)
    refunds: list[Refund] | None = field(init=False)
    invoice_settings: InvoiceSettings | None = field(init=False)
    status: Literal['preparing', 'requires_payment', 'paid', 'completed', 'canceled', 'expired', 'unknown'] = field(init=False)
    sealed_at: str | None = field(init=False)
    line_item_group: OrderLineItemGroup | None = field(init=False)
    payment: Payment | None = field(init=False)
    paid_at: str | None = field(init=False)
    payment_due_at: str | None = field(init=False)
    payout_settings: dict[str, Any] | None = field(init=False)
    reference: str | None = field(init=False)
    shipping: dict[str, Any] | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class OrderCheckoutSettings(ApiModel):
    redirect_url: str | None = field(init=False)
    cancel_url: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class OrderCreatedFrom(ApiModel):
    source: str | None = field(init=False)
    resource_type: Literal['purchase_intent'] | None = field(init=False)
    resource_id: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class OrderCustomer(ApiModel):
    id: str = field(init=False)
    guest: bool = field(init=False)
    name: str = field(init=False)
    email_address: str | None = field(init=False)
    phone_number: str | None = field(init=False)
    billing_address: OrderAddress | None = field(init=False)
    shipping_address: OrderAddress | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class OrderAddress(ApiModel):
    name: str | None = field(init=False)
    phone_number: str | None = field(init=False)
    line1: str | None = field(init=False)
    line2: str | None = field(init=False)
    city: str | None = field(init=False)
    region: str | None = field(init=False)
    post_code: str | None = field(init=False)
    country: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class OrderInvoice(ApiModel):
    number: str | None = field(init=False)
    format: OrderInvoiceFormat | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class OrderInvoiceFormat(ApiModel):
    web: OrderDocumentFormat = field(init=False)
    pdf: OrderDocumentFormat = field(init=False)
    receipt: OrderDocumentFormat | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class OrderDocumentFormat(ApiModel):
    url: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Refund(ApiModel):
    canceled_at: str | None = field(init=False)
    created_at: str = field(init=False)
    custom_data: dict[str, str] | None = field(init=False)
    failed_at: str | None = field(init=False)
    id: str = field(init=False)
    line_items: list[RefundLineItem] = field(init=False)
    order_id: str = field(init=False)
    processing_at: str | None = field(init=False)
    reason: RefundReasonValue = field(init=False)
    reason_details: str | None = field(init=False)
    reference: str | None = field(init=False)
    status: Literal['canceled', 'failed', 'pending', 'processing', 'succeeded'] = field(init=False)
    succeeded_at: str | None = field(init=False)
    total: Amount = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class RefundLineItem(ApiModel):
    id: str = field(init=False)
    order_line_item_id: str = field(init=False)
    original_amount_paid: Amount = field(init=False)
    reason: RefundReasonValue | None = field(init=False)
    reason_details: str | None = field(init=False)
    refund_amount: Amount = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class InvoiceSettings(ApiModel):
    number: str | None = field(init=False)
    memo: str | None = field(init=False)
    footer: str | None = field(init=False)
    custom_data: dict[str, str] | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class OrderLineItemGroup(ApiModel):
    line_items: list[OrderLineItem] = field(init=False)
    total: Amount = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class OrderProductLineItem(ApiModel):
    type: Literal['product'] = field(init=False)
    product: OrderProductLineItemProduct = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class OrderProductLineItemProduct(ApiModel):
    id: str = field(init=False)
    product_id: str | None = field(init=False)
    price_id: str | None = field(init=False)
    reference: str | None = field(init=False)
    about: str | None = field(init=False)
    custom_data: dict[str, str] | None = field(init=False)
    tax_code: str | None = field(init=False)
    name: str = field(init=False)
    category: str | None = field(init=False)
    type: str | None = field(init=False)
    price: Price = field(init=False)
    quantity: int = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class OrderFeeLineItem(ApiModel):
    type: Literal['fee'] = field(init=False)
    fee: OrderFeeLineItemFee = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class OrderFeeLineItemFee(ApiModel):
    id: str = field(init=False)
    description: str | None = field(init=False)
    tax_code: str | None = field(init=False)
    amount: Amount = field(init=False)
    label: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class OrderShippingLineItem(ApiModel):
    type: Literal['shipping'] = field(init=False)
    shipping: OrderShippingLineItemShipping = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class OrderShippingLineItemShipping(ApiModel):
    id: str = field(init=False)
    tax_code: str | None = field(init=False)
    label: str | None = field(init=False)
    fee: Amount = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Payment(ApiModel):
    id: str = field(init=False)
    status: Literal['initiated', 'requires_action', 'overdue', 'executed', 'paid', 'canceled', 'expired', 'failed', 'unknown'] = field(init=False)
    statement_descriptor: str = field(init=False)
    amount: Amount = field(init=False)
    balance_transaction: BalanceTransaction | None = field(init=False)
    payment_method: PaymentMethodSnapshot | None = field(init=False)
    latest_attempt: PaymentAttempt | None = field(init=False)
    next_action: PaymentNextAction | None = field(init=False)
    initiated_at: str = field(init=False)
    executed_at: str | None = field(init=False)
    paid_at: str | None = field(init=False)
    canceled_at: str | None = field(init=False)
    due_at: str | None = field(init=False)
    expired_at: str | None = field(init=False)
    failed_at: str | None = field(init=False)
    paid_offline: bool | None = field(init=False)
    payment_method_types: list[str] | None = field(init=False)
    payout_configuration: PaymentPayoutConfiguration | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class BalanceTransaction(ApiModel):
    amount: BalanceTransactionAmount = field(init=False)
    available_at: str | None = field(init=False)
    claimed_at: str | None = field(init=False)
    created_at: str = field(init=False)
    id: str = field(init=False)
    order_id: str = field(init=False)
    paid_at: str | None = field(init=False)
    payment_id: str | None = field(init=False)
    payout_id: str | None = field(init=False)
    refund_id: str | None = field(init=False)
    type: Literal['payment', 'refund'] = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class BalanceTransactionAmount(ApiModel):
    currency: str = field(init=False)
    value: int = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentMethodSnapshot(ApiModel):
    id: str = field(init=False)
    bank_account: PaymentMethodSnapshotBankAccount | None = field(init=False)
    card: dict[str, Any] | None = field(init=False)
    created_at: str = field(init=False)
    customer_id: str = field(init=False)
    mobile_money: PaymentMethodSnapshotMobileMoney | None = field(init=False)
    owner: PaymentMethodSnapshotOwner | None = field(init=False)
    type: Literal['mobile_money', 'bank_account', 'card', 'motito'] = field(init=False)
    verified: bool = field(init=False)
    verified_at: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentMethodSnapshotBankAccount(ApiModel):
    type: str = field(init=False)
    ghana_bank_account: PaymentMethodSnapshotGhanaBankAccount | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentMethodSnapshotGhanaBankAccount(ApiModel):
    account_number: str = field(init=False)
    branch: str | None = field(init=False)
    name: str | None = field(init=False)
    sort_code: str | None = field(init=False)
    swift_code: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentMethodSnapshotMobileMoney(ApiModel):
    network: Literal['airtel', 'mtn', 'telecel', 'vodafone'] = field(init=False)
    account_number: str = field(init=False)
    last4: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentMethodSnapshotOwner(ApiModel):
    name: str = field(init=False)
    address: OrderAddress | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentAttempt(ApiModel):
    payment_method_type: str | None = field(init=False)
    payment_method_id: str | None = field(init=False)
    reference: str | None = field(init=False)
    status: Literal['initiated', 'executed', 'succeeded', 'canceled', 'expired', 'failed', 'unknown'] | None = field(init=False)
    initiated_at: str | None = field(init=False)
    succeeded_at: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentNextAction(ApiModel):
    type: Literal['confirm_payment', 'execute', 'redirect', 'authorize', 'none'] = field(init=False)
    confirm_payment: PaymentNextActionConfirmPayment | None = field(init=False)
    execute: dict[str, Any] | None = field(init=False)
    redirect: PaymentNextActionRedirect | None = field(init=False)
    authorize: PaymentNextActionAuthorize | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentNextActionConfirmPayment(ApiModel):
    expires_at: str | None = field(init=False)
    scheme: str | None = field(init=False)
    request: PaymentNextActionConfirmPaymentRequest | None = field(init=False)
    attempt: PaymentNextActionConfirmPaymentAttempt | None = field(init=False)
    confirmed: bool | None = field(init=False)
    status: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentNextActionConfirmPaymentRequest(ApiModel):
    id: str | None = field(init=False)
    recipient: str | None = field(init=False)
    sent_via: Literal['sms', 'email', 'push'] | None = field(init=False)
    token_size: int | None = field(init=False)
    sender_id: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentNextActionConfirmPaymentAttempt(ApiModel):
    status: str | None = field(init=False)
    confirmed: bool | None = field(init=False)
    reason: str | None = field(init=False)
    token: str | None = field(init=False)
    executed_at: str | None = field(init=False)
    created_at: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentNextActionRedirect(ApiModel):
    redirect_url: str | None = field(init=False)
    valid_until: str | None = field(init=False)
    latest_visit: PaymentNextActionRedirectLatestVisit | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentNextActionRedirectLatestVisit(ApiModel):
    user_agent: str | None = field(init=False)
    ip_address: str | None = field(init=False)
    at: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentNextActionAuthorize(ApiModel):
    beneficiary: str | None = field(init=False)
    scheme: str | None = field(init=False)
    expires_at: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentPayoutConfiguration(ApiModel):
    enable_fx: Literal[False] | None = field(init=False)
    destination: PaymentPayoutConfigurationDestination | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentPayoutConfigurationDestination(ApiModel):
    financial_account_id: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FinalizeOrderEnvelope(ApiModel):
    order: Order | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class CompleteOrderEnvelope(ApiModel):
    order: Order | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class OrderDocumentDeliveryResult(ApiModel):
    delivery: OrderDocumentDelivery | None = field(init=False)
    error: Error | None = field(init=False)
    order: Order | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class OrderDocumentDelivery(ApiModel):
    deliveries: list[OrderDocumentDeliveryAttempt] | None = field(init=False)
    document_kind: Literal['invoice', 'receipt'] | None = field(init=False)
    document_url: str | None = field(init=False)
    failed_channels: list[Literal['email', 'sms']] | None = field(init=False)
    failures: list[OrderDocumentDeliveryFailure] | None = field(init=False)
    sent_channels: list[Literal['email', 'sms']] | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class OrderDocumentDeliveryAttempt(ApiModel):
    channel: Literal['email', 'sms'] | None = field(init=False)
    chime_id: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class OrderDocumentDeliveryFailure(ApiModel):
    channel: Literal['email', 'sms'] | None = field(init=False)
    error: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PageOrdersEnvelope(ApiModel):
    page: OrderPage | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class OrderPage(ApiModel):
    number: int | None = field(init=False)
    size: int | None = field(init=False)
    orders: list[Order] | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class RefundResponse(ApiModel):
    refund: Refund = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class RefundPageResponse(ApiModel):
    page: RefundPage = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class RefundPage(ApiModel):
    number: int = field(init=False)
    refunds: list[Refund] = field(init=False)
    size: int = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class CreateApplicationResponse(ApiModel):
    app: Application = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Application(ApiModel):
    id: str = field(init=False)
    name: str = field(init=False)
    alias: str | None = field(init=False)
    description: str | None = field(init=False)
    created_at: str = field(init=False)
    updated_at: str | None = field(init=False)
    archived_at: str | None = field(init=False)
    secret_key: ApplicationSecretKey | None = field(init=False)
    relationship: ApplicationRelationship | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ApplicationSecretKey(ApiModel):
    id: str | None = field(init=False)
    token_type: str | None = field(init=False)
    issued_at: str | None = field(init=False)
    token: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ApplicationRelationship(ApiModel):
    id: str = field(init=False)
    kind: Literal['placement'] = field(init=False)
    policy_version: str = field(init=False)
    status: Literal['active', 'inactive', 'suspended', 'revoked'] = field(init=False)
    actor_app_id: str = field(init=False)
    creator_app_id: str = field(init=False)
    placement_parent_app_id: str = field(init=False)
    subject_app_id: str = field(init=False)
    child_app_id: str = field(init=False)
    child_standing: str = field(init=False)
    relationship_policy: ApplicationRelationshipPolicy = field(init=False)
    retained_creator_authority_exists: bool = field(init=False)
    created_at: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ApplicationRelationshipPolicy(ApiModel):
    child_standing: str = field(init=False)
    management: Literal['parent', 'child'] = field(init=False)
    credentials: Literal['child', 'parent'] = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class LookupApplicationResponse(ApiModel):
    app: LookupApplicationResponseApp = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class LookupApplicationResponseApp(ApiModel):
    id: str = field(init=False)
    name: str = field(init=False)
    alias: str | None = field(init=False)
    description: str | None = field(init=False)
    created_at: str = field(init=False)
    updated_at: str | None = field(init=False)
    archived_at: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UpdateApplicationResponse(ApiModel):
    app: UpdateApplicationResponseApp = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UpdateApplicationResponseApp(ApiModel):
    id: str = field(init=False)
    name: str = field(init=False)
    alias: str | None = field(init=False)
    description: str | None = field(init=False)
    created_at: str = field(init=False)
    updated_at: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class GenerateSecretKeyResponse(ApiModel):
    key: GeneratedSecretKey = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class GeneratedSecretKey(ApiModel):
    id: str = field(init=False)
    label: str | None = field(init=False)
    token_type: Literal['bearer'] = field(init=False)
    issued_at: str = field(init=False)
    token: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PageSecretKeysResponse(ApiModel):
    page: SecretKeyPage = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class SecretKeyPage(ApiModel):
    number: int = field(init=False)
    size: int = field(init=False)
    count: int = field(init=False)
    total: int = field(init=False)
    has_more: bool = field(init=False)
    keys: list[SecretKey] = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class SecretKey(ApiModel):
    id: str = field(init=False)
    label: str | None = field(init=False)
    token_type: Literal['bearer'] = field(init=False)
    issued_at: str = field(init=False)
    updated_at: str | None = field(init=False)
    expires_at: str | None = field(init=False)
    status: Literal['active', 'revoked', 'expired'] = field(init=False)
    active: bool = field(init=False)
    revoked_at: str | None = field(init=False)
    last_used_at: str | None = field(init=False)
    usage_count: int | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class LookupSecretKeyResponse(ApiModel):
    key: SecretKey = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UpdateSecretKeyResponse(ApiModel):
    key: SecretKey = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class DestroySecretKeyResponse(ApiModel):
    key: SecretKey = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class SecretKeyUsage(ApiModel):
    key: SecretKey = field(init=False)
    usage: SecretKeyUsagePage = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class SecretKeyUsagePage(ApiModel):
    number: int = field(init=False)
    size: int = field(init=False)
    count: int = field(init=False)
    total: int = field(init=False)
    has_more: bool = field(init=False)
    rows: list[SecretKeyUsageRow] = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class SecretKeyUsageRow(ApiModel):
    secret_key_id: str = field(init=False)
    occurred_at: str = field(init=False)
    auth_result: Literal['succeeded', 'failed'] = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class CreateFinancialAccountResponse(ApiModel):
    account: FinancialAccountCreateResponse | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FinancialAccountCreateResponse(ApiModel):
    app_customer_local_fingerprint: str | None = field(init=False)
    app_local_fingerprint: str | None = field(init=False)
    archived_at: str | None = field(init=False)
    created_at: str = field(init=False)
    currency: str = field(init=False)
    custom_data: dict[str, str] | None = field(init=False)
    description: str | None = field(init=False)
    id: str = field(init=False)
    institution: FinancialInstitution | None = field(init=False)
    label: str | None = field(init=False)
    pull_configuration: FinancialAccountPullConfiguration | None = field(init=False)
    push_configuration: FinancialAccountPushConfiguration | None = field(init=False)
    reference: str | None = field(init=False)
    supplied: ResourceSupply | None = field(init=False)
    type: Literal['wallet', 'bank_account', 'dosh_account'] = field(init=False)
    universal_fingerprint: str | None = field(init=False)
    verification: dict[str, Any] | None = field(init=False)
    bank_account: FinancialAccountBankCreateResponse | None = field(init=False)
    owner: FinancialAccountOwnerCreateResponse | None = field(init=False)
    wallet: FinancialAccountWallet | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FinancialInstitution(ApiModel):
    bank: FinancialInstitutionBank | None = field(init=False)
    country: str = field(init=False)
    id: str = field(init=False)
    mobile_money_provider: FinancialInstitutionMobileMoneyProvider | None = field(init=False)
    name: str = field(init=False)
    type: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FinancialInstitutionBank(ApiModel):
    bank_account_type: str = field(init=False)
    branch: FinancialInstitutionBankBranch | None = field(init=False)
    code_scheme: str = field(init=False)
    sort_code_prefix: str | None = field(init=False)
    swift_code: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FinancialInstitutionBankBranch(ApiModel):
    id: str = field(init=False)
    name: str = field(init=False)
    sort_code: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FinancialInstitutionMobileMoneyProvider(ApiModel):
    provider: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FinancialAccountPullConfiguration(ApiModel):
    enabled_at: str = field(init=False)
    mandate: FinancialAccountPullConfigurationMandate = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FinancialAccountPullConfigurationMandate(ApiModel):
    created_at: str = field(init=False)
    id: str = field(init=False)
    ip_address: str = field(init=False)
    user_agent: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FinancialAccountPushConfiguration(ApiModel):
    enabled_at: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ResourceSupply(ApiModel):
    attempt_id: str | None = field(init=False)
    by: str = field(init=False)
    channel: str | None = field(init=False)
    resource_id: str | None = field(init=False)
    resource_type: str | None = field(init=False)
    supplied_at: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FinancialAccountBankCreateResponse(ApiModel):
    id: str = field(init=False)
    type: Literal['ghana_bank_account'] = field(init=False)
    ghana_bank_account: GhanaBankAccountCreateResponse | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class GhanaBankAccountCreateResponse(ApiModel):
    branch: str | None = field(init=False)
    holder: FinancialAccountOwnerCreateResponse = field(init=False)
    name: str = field(init=False)
    number: str = field(init=False)
    sort_code: str | None = field(init=False)
    swift_code: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FinancialAccountOwnerCreateResponse(ApiModel):
    address: FinancialAccountAddressCreateResponse = field(init=False)
    name: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FinancialAccountAddressCreateResponse(ApiModel):
    application_id: str = field(init=False)
    city: str = field(init=False)
    country: str = field(init=False)
    id: str = field(init=False)
    line_1: str = field(init=False)
    line_2: str | None = field(init=False)
    name: str = field(init=False)
    phone: str | None = field(init=False)
    post_code: str | None = field(init=False)
    region: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FinancialAccountWallet(ApiModel):
    id: str = field(init=False)
    type: Literal['mobile_money'] = field(init=False)
    mobile_money: FinancialAccountWalletMobileMoney | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FinancialAccountWalletMobileMoney(ApiModel):
    account_number: str = field(init=False)
    network: Literal['airtel', 'mtn', 'telecel', 'vodafone'] = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class LookupFinancialAccountResponse(ApiModel):
    account: FinancialAccount | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FinancialAccount(ApiModel):
    app_customer_local_fingerprint: str | None = field(init=False)
    app_local_fingerprint: str | None = field(init=False)
    archived_at: str | None = field(init=False)
    created_at: str = field(init=False)
    currency: str = field(init=False)
    custom_data: dict[str, str] | None = field(init=False)
    description: str | None = field(init=False)
    id: str = field(init=False)
    institution: FinancialInstitution | None = field(init=False)
    label: str | None = field(init=False)
    pull_configuration: FinancialAccountPullConfiguration | None = field(init=False)
    push_configuration: FinancialAccountPushConfiguration | None = field(init=False)
    reference: str | None = field(init=False)
    supplied: ResourceSupply | None = field(init=False)
    type: Literal['wallet', 'bank_account', 'dosh_account'] = field(init=False)
    universal_fingerprint: str | None = field(init=False)
    verification: dict[str, Any] | None = field(init=False)
    bank_account: FinancialAccountBank | None = field(init=False)
    disconnected_at: str | None = field(init=False)
    dosh_account: dict[str, Any] | None = field(init=False)
    owner: FinancialAccountOwner | None = field(init=False)
    wallet: FinancialAccountWallet | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FinancialAccountBank(ApiModel):
    type: Literal['ghana_bank_account'] = field(init=False)
    ghana_bank_account: GhanaBankAccount | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class GhanaBankAccount(ApiModel):
    branch: str | None = field(init=False)
    holder: FinancialAccountOwner = field(init=False)
    name: str | None = field(init=False)
    number: str = field(init=False)
    sort_code: str | None = field(init=False)
    swift_code: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FinancialAccountOwner(ApiModel):
    address: FinancialAccountAddress = field(init=False)
    name: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FinancialAccountAddress(ApiModel):
    city: str = field(init=False)
    country: str = field(init=False)
    line_1: str = field(init=False)
    line_2: str | None = field(init=False)
    name: str | None = field(init=False)
    phone: str | None = field(init=False)
    post_code: str | None = field(init=False)
    region: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PageFinancialAccountsResponse(ApiModel):
    page: FinancialAccountPage | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FinancialAccountPage(ApiModel):
    accounts: list[FinancialAccount] = field(init=False)
    number: int = field(init=False)
    size: int = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ConnectFinancialAccountResponse(ApiModel):
    account: FinancialAccountConnectedResponse | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FinancialAccountConnectedResponse(ApiModel):
    app_customer_local_fingerprint: str | None = field(init=False)
    app_local_fingerprint: str | None = field(init=False)
    archived_at: str | None = field(init=False)
    created_at: str = field(init=False)
    currency: str = field(init=False)
    custom_data: dict[str, str] | None = field(init=False)
    description: str | None = field(init=False)
    id: str = field(init=False)
    institution: FinancialInstitution | None = field(init=False)
    label: str | None = field(init=False)
    pull_configuration: FinancialAccountPullConfiguration | None = field(init=False)
    push_configuration: FinancialAccountPushConfiguration | None = field(init=False)
    reference: str | None = field(init=False)
    supplied: ResourceSupply | None = field(init=False)
    type: Literal['wallet', 'bank_account', 'dosh_account'] = field(init=False)
    universal_fingerprint: str | None = field(init=False)
    verification: dict[str, Any] | None = field(init=False)
    bank_account: FinancialAccountBank | None = field(init=False)
    dosh_account: dict[str, Any] | None = field(init=False)
    owner: FinancialAccountOwner | None = field(init=False)
    wallet: FinancialAccountWallet | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UpdateFinancialAccountResponse(ApiModel):
    account: FinancialAccountUpdateResponse | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FinancialAccountUpdateResponse(ApiModel):
    app_customer_local_fingerprint: str | None = field(init=False)
    app_local_fingerprint: str | None = field(init=False)
    archived_at: str | None = field(init=False)
    created_at: str = field(init=False)
    currency: str = field(init=False)
    custom_data: dict[str, str] | None = field(init=False)
    description: str | None = field(init=False)
    id: str = field(init=False)
    institution: FinancialInstitution | None = field(init=False)
    label: str | None = field(init=False)
    pull_configuration: FinancialAccountPullConfiguration | None = field(init=False)
    push_configuration: FinancialAccountPushConfiguration | None = field(init=False)
    reference: str | None = field(init=False)
    supplied: ResourceSupply | None = field(init=False)
    type: Literal['wallet', 'bank_account', 'dosh_account'] = field(init=False)
    universal_fingerprint: str | None = field(init=False)
    verification: dict[str, Any] | None = field(init=False)
    bank_account: FinancialAccountBankUpdateResponse | None = field(init=False)
    disconnected_at: str | None = field(init=False)
    dosh_account: dict[str, Any] | None = field(init=False)
    owner: FinancialAccountOwnerUpdateResponse | None = field(init=False)
    wallet: FinancialAccountWalletRawResponse | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FinancialAccountBankUpdateResponse(ApiModel):
    id: str = field(init=False)
    type: Literal['ghana_bank_account'] = field(init=False)
    ghana_bank_account: GhanaBankAccountUpdateResponse | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class GhanaBankAccountUpdateResponse(ApiModel):
    branch: str | None = field(init=False)
    holder: FinancialAccountOwner = field(init=False)
    name: str = field(init=False)
    number: str = field(init=False)
    sort_code: str | None = field(init=False)
    swift_code: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FinancialAccountOwnerUpdateResponse(ApiModel):
    address: FinancialAccountAddressUpdateResponse = field(init=False)
    name: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FinancialAccountAddressUpdateResponse(ApiModel):
    city: str = field(init=False)
    country: str = field(init=False)
    id: str | None = field(init=False)
    line_1: str = field(init=False)
    line_2: str | None = field(init=False)
    name: str | None = field(init=False)
    phone: str | None = field(init=False)
    post_code: str | None = field(init=False)
    region: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FinancialAccountWalletRawResponse(ApiModel):
    id: str = field(init=False)
    type: Literal['mobile_money'] = field(init=False)
    mobile_money: FinancialAccountWalletRawResponseMobileMoney | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FinancialAccountWalletRawResponseMobileMoney(ApiModel):
    account_number: str = field(init=False)
    network: Literal['airtel', 'mtn', 'telecel', 'vodafone'] = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class EnableFinancialAccountPushResponse(ApiModel):
    account: FinancialAccountConnectedResponse | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class DisableFinancialAccountPushResponse(ApiModel):
    account: FinancialAccountConnectedResponse | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class DisconnectFinancialAccountResponse(ApiModel):
    account: FinancialAccountCompactResponse | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FinancialAccountCompactResponse(ApiModel):
    created_at: str = field(init=False)
    currency: str = field(init=False)
    description: str | None = field(init=False)
    disconnected_at: str | None = field(init=False)
    id: str = field(init=False)
    label: str | None = field(init=False)
    type: Literal['wallet', 'bank_account', 'dosh_account'] = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ReconnectFinancialAccountResponse(ApiModel):
    account: FinancialAccountCompactResponse | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class EnableFinancialAccountPullResponse(ApiModel):
    account: FinancialAccountConnectedResponse | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class DisableFinancialAccountPullResponse(ApiModel):
    account: FinancialAccountConnectedResponse | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class BalanceSnapshotResponse(ApiModel):
    balances: BalanceSnapshotResponseBalances = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class BalanceSnapshotResponseBalances(ApiModel):
    ghs: CurrencyBalanceSnapshot = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class CurrencyBalanceSnapshot(ApiModel):
    available: BalanceValue = field(init=False)
    includes_transactions_before: str = field(init=False)
    pending: BalanceValue = field(init=False)
    refund: CurrencyBalanceSnapshotRefund = field(init=False)
    reserved: CurrencyBalanceSnapshotReserved = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class BalanceValue(ApiModel):
    amount: int = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class CurrencyBalanceSnapshotRefund(ApiModel):
    amount: int = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class CurrencyBalanceSnapshotReserved(ApiModel):
    amount: int = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class BalanceTransactionResponse(ApiModel):
    transaction: BalanceTransaction = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class BalanceTransactionPageResponse(ApiModel):
    page: BalanceTransactionPage = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class BalanceTransactionPage(ApiModel):
    number: int = field(init=False)
    size: int = field(init=False)
    transactions: list[BalanceTransaction] | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class SchedulePayoutResponse(ApiModel):
    payout: Payout | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Payout(ApiModel):
    amount: Amount | None = field(init=False)
    balance_transactions: list[str] | None = field(init=False)
    canceled_at: str | None = field(init=False)
    custom_data: dict[str, str] | None = field(init=False)
    destination_id: str = field(init=False)
    error: PayoutError | None = field(init=False)
    execute_after: str = field(init=False)
    executed_by: str | None = field(init=False)
    expected_at: str | None = field(init=False)
    failed_at: str | None = field(init=False)
    id: str = field(init=False)
    initiated_at: str = field(init=False)
    initiated_by: str | None = field(init=False)
    max_amount: Amount = field(init=False)
    reference: str | None = field(init=False)
    schedule_id: str | None = field(init=False)
    scheduled_at: str | None = field(init=False)
    scheduled_by: str | None = field(init=False)
    sent_at: str | None = field(init=False)
    source_id: str | None = field(init=False)
    status: Literal['initialized', 'scheduled', 'processing', 'executing', 'succeeded', 'invalid', 'canceled'] = field(init=False)
    succeeded_at: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PayoutError(ApiModel):
    cause: str = field(init=False)
    message: str = field(init=False)
    occurred_at: str = field(init=False)
    type: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class LookupPayoutResponse(ApiModel):
    payout: Payout | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class SetPayoutDestinationsResponse(ApiModel):
    settings: PayoutSettingsMutation | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PayoutSettingsMutation(ApiModel):
    destinations: dict[str, str] | None = field(init=False)
    id: str | None = field(init=False)
    schedule: PayoutSettingsMutationSchedule | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PayoutSettingsMutationSchedule(ApiModel):
    description: str = field(init=False)
    id: str = field(init=False)
    interval: str = field(init=False)
    name: str = field(init=False)
    schedule_on: str = field(init=False)
    spec: PayoutSettingsMutationScheduleSpec = field(init=False)
    type: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PayoutSettingsMutationScheduleSpec(ApiModel):
    abide: str = field(init=False)
    id: str = field(init=False)
    label: str = field(init=False)
    t_plus: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class GetPayoutSettingsResponse(ApiModel):
    settings: PayoutSettingsLookup | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PayoutSettingsLookup(ApiModel):
    destinations: dict[str, str] = field(init=False)
    fx_enabled: bool | None = field(init=False)
    schedule: PayoutSettingsLookupSchedule | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PayoutSettingsLookupSchedule(ApiModel):
    aging_spec: PayoutSettingsLookupScheduleAgingSpec = field(init=False)
    description: str = field(init=False)
    interval: str = field(init=False)
    name: str = field(init=False)
    schedule_on: str = field(init=False)
    type: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PayoutSettingsLookupScheduleAgingSpec(ApiModel):
    abide: str = field(init=False)
    label: str = field(init=False)
    t_plus: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class DisableAutomaticPayoutsResponse(ApiModel):
    settings: PayoutSettingsMutation | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class EnableAutomaticPayoutsResponse(ApiModel):
    settings: PayoutSettingsMutation | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PagePayoutsResponse(ApiModel):
    page: PayoutPage | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PayoutPage(ApiModel):
    number: int = field(init=False)
    size: int = field(init=False)
    payouts: list[Payout] | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class CancelPayoutResponse(ApiModel):
    payout: Payout | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FileResponse(ApiModel):
    file: File = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class File(ApiModel):
    id: str = field(init=False)
    purpose: str = field(init=False)
    status: Literal['uploading', 'processing', 'available', 'failed', 'deleted'] = field(init=False)
    scan_status: Literal['pending', 'passed', 'failed', 'skipped'] = field(init=False)
    name: str | None = field(init=False)
    filename: str | None = field(init=False)
    content_type: str = field(init=False)
    size: int = field(init=False)
    checksum_sha256: str = field(init=False)
    created_by: FileActor = field(init=False)
    source: FileSource = field(init=False)
    media: FileMedia | None = field(init=False)
    storage: PublicFileStorage = field(init=False)
    delivery: FileDeliveryDetails | None = field(init=False)
    latest_error: FileLatestError | None = field(init=False)
    custom_data: dict[str, str] | None = field(init=False)
    metadata: dict[str, str] | None = field(init=False)
    created_at: str = field(init=False)
    updated_at: str = field(init=False)
    available_at: str | None = field(init=False)
    expires_at: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FileActor(ApiModel):
    type: str = field(init=False)
    id: str | None = field(init=False)
    name: str | None = field(init=False)
    email: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FileSource(ApiModel):
    type: Literal['direct', 'upload_request', 'service'] | None = field(init=False)
    service: str | None = field(init=False)
    upload_request_id: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FileMedia(ApiModel):
    kind: str | None = field(init=False)
    width: int | None = field(init=False)
    height: int | None = field(init=False)
    duration_ms: int | None = field(init=False)
    page_count: int | None = field(init=False)
    frame_count: int | None = field(init=False)
    color_space: str | None = field(init=False)
    has_alpha: bool | None = field(init=False)
    codec: str | None = field(init=False)
    aspect_ratio: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PublicFileStorage(ApiModel):
    encoding: Literal['identity', 'br'] = field(init=False)
    stored_size: int = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FileDeliveryDetails(ApiModel):
    public_url: str | None = field(init=False)
    cache_control: str | None = field(init=False)
    content_type: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FileLatestError(ApiModel):
    code: str | None = field(init=False)
    message: str | None = field(init=False)
    retryable: bool | None = field(init=False)
    at: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FilePageResponse(ApiModel):
    page: FilePage = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FilePage(ApiModel):
    number: int = field(init=False)
    size: int = field(init=False)
    files: list[File] = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FileLinkCreation(ApiModel):
    file_link: FileLink = field(init=False)
    url: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FileLink(ApiModel):
    id: str = field(init=False)
    kind: Literal['public'] = field(init=False)
    file_id: str = field(init=False)
    purpose: str = field(init=False)
    status: Literal['active', 'revoked', 'expired', 'disabled'] = field(init=False)
    active: bool = field(init=False)
    delivery: FileLinkDelivery = field(init=False)
    access: FileLinkAccess = field(init=False)
    created_by: FileLinkActor = field(init=False)
    revoked_by: FileLinkActor | None = field(init=False)
    custom_data: dict[str, str] | None = field(init=False)
    metadata: dict[str, str] | None = field(init=False)
    created_at: str = field(init=False)
    updated_at: str = field(init=False)
    expires_at: str = field(init=False)
    revoked_at: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FileLinkDelivery(ApiModel):
    mode: Literal['redirect', 'download', 'inline'] | None = field(init=False)
    filename: str | None = field(init=False)
    content_type: str | None = field(init=False)
    disposition: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FileLinkAccess(ApiModel):
    max_accesses: int | None = field(init=False)
    access_count: int | None = field(init=False)
    last_accessed_at: str | None = field(init=False)
    allow_download: bool | None = field(init=False)
    allowed_origins: list[str] | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FileLinkActor(ApiModel):
    email: str | None = field(init=False)
    id: str | None = field(init=False)
    name: str | None = field(init=False)
    type: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FileLinkResponse(ApiModel):
    file_link: FileLink = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FileLinkPageResponse(ApiModel):
    page: FileLinkPage = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FileLinkPage(ApiModel):
    number: int = field(init=False)
    size: int = field(init=False)
    file_links: list[FileLink] = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UploadRequestResponse(ApiModel):
    upload_request: UploadRequest = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UploadRequest(ApiModel):
    id: str = field(init=False)
    purpose: str = field(init=False)
    status: Literal['pending', 'uploading', 'fulfilled', 'expired', 'canceled', 'failed'] = field(init=False)
    active: bool = field(init=False)
    file_id: str | None = field(init=False)
    upload_url: str | None = field(init=False)
    constraints: UploadRequestConstraints = field(init=False)
    display: UploadRequestDisplay = field(init=False)
    subject: FileParty = field(init=False)
    recipient: FileParty = field(init=False)
    resource: FileResource = field(init=False)
    requester: UploadRequestActor = field(init=False)
    attempts: UploadRequestAttempts = field(init=False)
    latest_error: UploadRequestLatestError | None = field(init=False)
    canceled_by: UploadRequestActor | None = field(init=False)
    custom_data: dict[str, str] | None = field(init=False)
    metadata: dict[str, str] | None = field(init=False)
    created_at: str = field(init=False)
    updated_at: str = field(init=False)
    expires_at: str = field(init=False)
    uploading_at: str | None = field(init=False)
    fulfilled_at: str | None = field(init=False)
    expired_at: str | None = field(init=False)
    canceled_at: str | None = field(init=False)
    attempt: UploadRequestAttempt | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UploadRequestConstraints(ApiModel):
    min_size: int | None = field(init=False)
    max_size: int | None = field(init=False)
    exact_size: int | None = field(init=False)
    content_types: list[str] | None = field(init=False)
    extensions: list[str] | None = field(init=False)
    filename: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UploadRequestDisplay(ApiModel):
    title: str | None = field(init=False)
    description: str | None = field(init=False)
    help_text: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FileParty(ApiModel):
    type: str | None = field(init=False)
    id: str | None = field(init=False)
    name: str | None = field(init=False)
    email: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FileResource(ApiModel):
    type: str | None = field(init=False)
    id: str | None = field(init=False)
    name: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UploadRequestActor(ApiModel):
    email: str | None = field(init=False)
    id: str | None = field(init=False)
    name: str | None = field(init=False)
    type: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UploadRequestAttempts(ApiModel):
    max_attempts: int | None = field(init=False)
    attempt_count: int = field(init=False)
    failed_attempt_count: int = field(init=False)
    last_attempted_at: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UploadRequestLatestError(ApiModel):
    code: str | None = field(init=False)
    param: str | None = field(init=False)
    message: str | None = field(init=False)
    retryable: bool | None = field(init=False)
    at: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UploadRequestWithAttemptResponse(ApiModel):
    upload_request: UploadRequestWithAttemptObject = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UploadRequestWithAttemptObject(ApiModel):
    id: str = field(init=False)
    purpose: str = field(init=False)
    status: Literal['pending', 'uploading', 'fulfilled', 'expired', 'canceled', 'failed'] = field(init=False)
    active: bool = field(init=False)
    file_id: str | None = field(init=False)
    upload_url: str | None = field(init=False)
    constraints: UploadRequestConstraints = field(init=False)
    display: UploadRequestDisplay = field(init=False)
    subject: FileParty = field(init=False)
    recipient: FileParty = field(init=False)
    resource: FileResource = field(init=False)
    requester: UploadRequestActor = field(init=False)
    attempts: UploadRequestAttempts = field(init=False)
    latest_error: UploadRequestLatestError | None = field(init=False)
    canceled_by: UploadRequestActor | None = field(init=False)
    custom_data: dict[str, str] | None = field(init=False)
    metadata: dict[str, str] | None = field(init=False)
    created_at: str = field(init=False)
    updated_at: str = field(init=False)
    expires_at: str = field(init=False)
    uploading_at: str | None = field(init=False)
    fulfilled_at: str | None = field(init=False)
    expired_at: str | None = field(init=False)
    canceled_at: str | None = field(init=False)
    attempt: UploadRequestAttempt | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UploadRequestAttempt(ApiModel):
    attempted_at: str = field(init=False)
    content_type: str | None = field(init=False)
    declared_size: int | None = field(init=False)
    error: UploadRequestLatestError | None = field(init=False)
    failed_at: str | None = field(init=False)
    file_id: str | None = field(init=False)
    filename: str | None = field(init=False)
    id: str = field(init=False)
    ordinal: int = field(init=False)
    review: UploadRequestReview | None = field(init=False)
    status: str = field(init=False)
    succeeded_at: str | None = field(init=False)
    upload_request_id: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UploadRequestReview(ApiModel):
    created_at: str = field(init=False)
    decision: Literal['approved', 'rejected'] = field(init=False)
    file_id: str | None = field(init=False)
    public_message: str | None = field(init=False)
    reasons: list[UploadRequestReviewReason] | None = field(init=False)
    reviewed_at: str = field(init=False)
    type: Literal['automatic', 'manual'] = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UploadRequestReviewReason(ApiModel):
    code: str = field(init=False)
    message: str = field(init=False)
    param: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UploadRequestPageResponse(ApiModel):
    page: UploadRequestPage = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UploadRequestPage(ApiModel):
    number: int = field(init=False)
    size: int = field(init=False)
    upload_requests: list[UploadRequest] = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UploadFulfillment(ApiModel):
    upload_request: UploadRequest = field(init=False)
    file: FileUploadReceipt = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FileUploadReceipt(ApiModel):
    content_type: str = field(init=False)
    created_at: str = field(init=False)
    filename: str | None = field(init=False)
    id: str = field(init=False)
    name: str | None = field(init=False)
    size: int = field(init=False)
    status: Literal['uploading', 'processing', 'available', 'failed', 'deleted'] = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FileReferenceReconciliation(ApiModel):
    reconciled: Literal[True] = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class TokenizePaymentMethodResponse(ApiModel):
    payment_method: PaymentMethod | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentMethod(ApiModel):
    active: bool = field(init=False)
    app_customer_local_fingerprint: str | None = field(init=False)
    app_local_fingerprint: str | None = field(init=False)
    archived_at: str | None = field(init=False)
    bank_account: PaymentMethodBankAccount | None = field(init=False)
    created_at: str = field(init=False)
    custom_data: dict[str, str] | None = field(init=False)
    customer_id: str = field(init=False)
    ephemeral: bool | None = field(init=False)
    expires_on: str | None = field(init=False)
    id: str = field(init=False)
    mobile_money: PaymentMethodMobileMoney | None = field(init=False)
    owner: PaymentMethodOwner | None = field(init=False)
    type: Literal['mobile_money', 'bank_account', 'card', 'motito'] = field(init=False)
    supplied: PaymentMethodSupplied | None = field(init=False)
    universal_fingerprint: str | None = field(init=False)
    verification: PaymentMethodVerification | None = field(init=False)
    verified_at: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentMethodBankAccount(ApiModel):
    ghana_bank_account: PaymentMethodBankAccountGhanaBankAccount | None = field(init=False)
    type: Literal['ghana_bank_account'] = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentMethodBankAccountGhanaBankAccount(ApiModel):
    branch: str | None = field(init=False)
    name: str | None = field(init=False)
    account_number: str = field(init=False)
    sort_code: str | None = field(init=False)
    swift_code: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentMethodMobileMoney(ApiModel):
    account_number: str = field(init=False)
    last4: str = field(init=False)
    network: Literal['airtel', 'mtn', 'telecel', 'vodafone'] = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentMethodOwner(ApiModel):
    address: PaymentMethodOwnerAddress | None = field(init=False)
    name: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentMethodOwnerAddress(ApiModel):
    city: str | None = field(init=False)
    country: str = field(init=False)
    line_1: str | None = field(init=False)
    line_2: str | None = field(init=False)
    name: str | None = field(init=False)
    phone_number: str | None = field(init=False)
    post_code: str | None = field(init=False)
    region: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentMethodSupplied(ApiModel):
    attempt_id: str | None = field(init=False)
    by: str = field(init=False)
    channel: str | None = field(init=False)
    resource_id: str | None = field(init=False)
    resource_type: str | None = field(init=False)
    supplied_at: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentMethodVerification(ApiModel):
    completed_at: str | None = field(init=False)
    initiated_at: str = field(init=False)
    mechanism: str | None = field(init=False)
    request_id: str = field(init=False)
    type: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class LookupPaymentMethodResponse(ApiModel):
    payment_method: PaymentMethod | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentMethodPageResponse(ApiModel):
    page: PaymentMethodPage = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentMethodPage(ApiModel):
    number: int = field(init=False)
    payment_methods: list[PaymentMethod] = field(init=False)
    size: int = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UpdatePaymentMethodResponse(ApiModel):
    payment_method: PaymentMethod | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ActivatePaymentMethodResponse(ApiModel):
    payment_method: PaymentMethod | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class DisactivatePaymentMethodResponse(ApiModel):
    payment_method: PaymentMethod | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ArchivePaymentMethodResponse(ApiModel):
    payment_method: PaymentMethod | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UnarchivePaymentMethodResponse(ApiModel):
    payment_method: PaymentMethod | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class GetPaymentMethodSettingsResponse(ApiModel):
    settings: PaymentMethodSettings = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentMethodSettings(ApiModel):
    mobile_money: PaymentMethodTypeSetting | None = field(init=False)
    bank_account: PaymentMethodTypeSetting | None = field(init=False)
    card: PaymentMethodTypeSetting | None = field(init=False)
    motito: PaymentMethodTypeSetting | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentMethodTypeSetting(ApiModel):
    type: Literal['mobile_money', 'bank_account', 'card', 'motito'] | None = field(init=False)
    name: str | None = field(init=False)
    description: str | None = field(init=False)
    enabled: bool = field(init=False)
    confirms_use: bool = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentMethodVerificationSession(ApiModel):
    payment_method_id: str = field(init=False)
    status: str = field(init=False)
    token_sent_at: str | None = field(init=False)
    expires_at: str | None = field(init=False)
    delivery: dict[str, Any] | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentMethodDeletion(ApiModel):
    deleted: bool = field(init=False)
    payment_method_id: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ProductResponse(ApiModel):
    product: Product | None = field(init=False)
    error: Error | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Product(ApiModel):
    id: str = field(init=False)
    type: Literal['physical', 'digital', 'service', 'voucher', 'custom', 'cause'] = field(init=False)
    reference: str | None = field(init=False)
    name: str = field(init=False)
    description: str | None = field(init=False)
    about: str | None = field(init=False)
    tax_code: str | None = field(init=False)
    category: str | None = field(init=False)
    prices: list[ProductPriceSummary] | None = field(init=False)
    shipment: ProductShipment | None = field(init=False)
    media: ProductMedia | None = field(init=False)
    attributes: list[ProductAttribute] | None = field(init=False)
    dimensions: ProductDimensions | None = field(init=False)
    custom_data: dict[str, str] | None = field(init=False)
    active: bool = field(init=False)
    created_at: str = field(init=False)
    updated_at: str | None = field(init=False)
    archived_at: str | None = field(init=False)
    published_at: str | None = field(init=False)
    unit_dim: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ProductPriceSummary(ApiModel):
    id: str = field(init=False)
    active: bool = field(init=False)
    label: str | None = field(init=False)
    nominal: Amount = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ProductShipment(ApiModel):
    type: Literal['delivery', 'download', 'render', 'service', 'stream'] = field(init=False)
    delivery: dict[str, Any] | None = field(init=False)
    download: dict[str, Any] | None = field(init=False)
    render: dict[str, Any] | None = field(init=False)
    service: dict[str, Any] | None = field(init=False)
    stream: dict[str, Any] | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ProductMedia(ApiModel):
    hero_image: str | None = field(init=False)
    thumbnail: str | None = field(init=False)
    web_page_url: str | None = field(init=False)
    brand_logo: str | None = field(init=False)
    infographic: str | None = field(init=False)
    promo_video: str | None = field(init=False)
    demo_video: str | None = field(init=False)
    gallery: list[str] | None = field(init=False)
    downloads: list[str] | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ProductAttribute(ApiModel):
    name: str = field(init=False)
    value: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ProductDimensions(ApiModel):
    physical: ProductDimensionsPhysical | None = field(init=False)
    digital: ProductDimensionsDigital | None = field(init=False)
    custom: ProductDimensionsCustom | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ProductDimensionsPhysical(ApiModel):
    weight_unit: str | None = field(init=False)
    weight: float | None = field(init=False)
    size: float | None = field(init=False)
    volume_unit: str | None = field(init=False)
    volume: float | None = field(init=False)
    length: float | None = field(init=False)
    height: float | None = field(init=False)
    width: float | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ProductDimensionsDigital(ApiModel):
    bytes: float | None = field(init=False)
    size_unit: str | None = field(init=False)
    size: float | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ProductDimensionsCustom(ApiModel):
    size_unit: str | None = field(init=False)
    size: float | None = field(init=False)
    details: dict[str, str] | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class AddProductPriceResponse(ApiModel):
    price: CatalogPrice | None = field(init=False)
    error: Error | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UpdateProductResponse(ApiModel):
    product: UpdatedProduct | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UpdatedProduct(ApiModel):
    id: str = field(init=False)
    name: str = field(init=False)
    description: str | None = field(init=False)
    about: str | None = field(init=False)
    type: Literal['physical', 'digital', 'service', 'voucher', 'custom', 'cause'] = field(init=False)
    reference: str | None = field(init=False)
    tax_code: str | None = field(init=False)
    category: str | None = field(init=False)
    custom_data: dict[str, str] | None = field(init=False)
    dimensions: ProductDimensions | None = field(init=False)
    prices: list[ProductPriceSummary] | None = field(init=False)
    unit_dim: str | None = field(init=False)
    created_at: str = field(init=False)
    updated_at: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PageProductsResponse(ApiModel):
    page: ProductPage | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ProductPage(ApiModel):
    number: int | None = field(init=False)
    size: int | None = field(init=False)
    products: list[Product] | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PurchaseIntentResponse(ApiModel):
    purchase_intent: PurchaseIntent = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PurchaseIntent(ApiModel):
    activity: PurchaseIntentActivity | None = field(init=False)
    allow_variants: bool = field(init=False)
    application_id: str = field(init=False)
    created_at: str = field(init=False)
    expires_at: str | None = field(init=False)
    id: str = field(init=False)
    inactive_at: str | None = field(init=False)
    merchant: PurchaseIntentMerchant | None = field(init=False)
    price: PurchaseIntentPrice | None = field(init=False)
    product: PurchaseIntentProduct | None = field(init=False)
    quantity: PurchaseIntentQuantity = field(init=False)
    status: Literal['active', 'expired', 'inactive', 'used'] = field(init=False)
    updated_at: str | None = field(init=False)
    usage: PurchaseIntentUsage = field(init=False)
    variant_set: PurchaseIntentVariantSet | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PurchaseIntentActivity(ApiModel):
    recent: list[PurchaseIntentActivity] | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PurchaseIntentMerchant(ApiModel):
    app_id: str | None = field(init=False)
    app_name: str | None = field(init=False)
    organization_id: str | None = field(init=False)
    organization_name: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PurchaseIntentPrice(ApiModel):
    active: bool = field(init=False)
    id: str | None = field(init=False)
    label: str | None = field(init=False)
    nominal: Amount = field(init=False)
    original: PurchaseIntentOriginalPrice | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PurchaseIntentOriginalPrice(ApiModel):
    active: bool = field(init=False)
    id: str | None = field(init=False)
    label: str | None = field(init=False)
    nominal: Amount = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PurchaseIntentProduct(ApiModel):
    id: str = field(init=False)
    about: str | None = field(init=False)
    active: bool = field(init=False)
    archived_at: str | None = field(init=False)
    attributes: list[PurchaseIntentProductAttributesItem] | None = field(init=False)
    category: str | None = field(init=False)
    created_at: str = field(init=False)
    custom_data: dict[str, str] | None = field(init=False)
    description: str | None = field(init=False)
    dimensions: dict[str, Any] | None = field(init=False)
    media: dict[str, Any] | None = field(init=False)
    name: str = field(init=False)
    published_at: str | None = field(init=False)
    reference: str | None = field(init=False)
    shipment: dict[str, Any] | None = field(init=False)
    tax_code: str | None = field(init=False)
    type: Literal['physical', 'digital', 'service', 'voucher', 'custom', 'cause'] = field(init=False)
    unit_dim: str | None = field(init=False)
    updated_at: str | None = field(init=False)
    prices: list[ProductPriceSummary] | None = field(init=False)
    variant_set_id: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PurchaseIntentProductAttributesItem(ApiModel):
    name: str = field(init=False)
    value: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PurchaseIntentQuantity(ApiModel):
    min: int = field(init=False)
    max: int | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PurchaseIntentUsage(ApiModel):
    multi_use: bool | None = field(init=False)
    order: PurchaseIntentUsageOrder | None = field(init=False)
    single_use: bool | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PurchaseIntentUsageOrder(ApiModel):
    created_at: str = field(init=False)
    id: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PurchaseIntentVariantSet(ApiModel):
    active: bool = field(init=False)
    default_product_id: str | None = field(init=False)
    description: str | None = field(init=False)
    id: str = field(init=False)
    name: str = field(init=False)
    reference: str | None = field(init=False)
    variant_axes: list[PurchaseIntentVariantAxis] = field(init=False)
    variants: list[PurchaseIntentVariant] = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PurchaseIntentVariantAxis(ApiModel):
    key: str = field(init=False)
    label: str = field(init=False)
    position: int = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PurchaseIntentVariant(ApiModel):
    active: bool = field(init=False)
    position: int | None = field(init=False)
    price: PurchaseIntentPrice | None = field(init=False)
    product: PurchaseIntentProduct | None = field(init=False)
    product_id: str = field(init=False)
    variant_values: dict[str, str] = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PagePurchaseIntentsResponse(ApiModel):
    page: PurchaseIntentPage = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PurchaseIntentPage(ApiModel):
    number: int = field(init=False)
    purchase_intents: list[PurchaseIntent] = field(init=False)
    size: int = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PriceResponse(ApiModel):
    price: CatalogPrice | None = field(init=False)
    error: Error | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class CatalogPrice(ApiModel):
    id: str = field(init=False)
    label: str | None = field(init=False)
    about: str | None = field(init=False)
    active: bool = field(init=False)
    nominal: Amount = field(init=False)
    product: PriceEmbeddedProduct | None = field(init=False)
    created_at: str = field(init=False)
    updated_at: str | None = field(init=False)
    archived_at: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PriceEmbeddedProduct(ApiModel):
    id: str = field(init=False)
    about: str | None = field(init=False)
    active: bool = field(init=False)
    archived_at: str | None = field(init=False)
    attributes: list[PriceEmbeddedProductAttributesItem] | None = field(init=False)
    category: str | None = field(init=False)
    created_at: str = field(init=False)
    custom_data: dict[str, str] | None = field(init=False)
    description: str | None = field(init=False)
    dimensions: dict[str, Any] | None = field(init=False)
    media: dict[str, Any] | None = field(init=False)
    name: str = field(init=False)
    published_at: str | None = field(init=False)
    reference: str | None = field(init=False)
    shipment: dict[str, Any] | None = field(init=False)
    tax_code: str | None = field(init=False)
    type: Literal['physical', 'digital', 'service', 'voucher', 'custom', 'cause'] = field(init=False)
    unit_dim: str | None = field(init=False)
    updated_at: str | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PriceEmbeddedProductAttributesItem(ApiModel):
    name: str = field(init=False)
    value: str = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PricePageResponse(ApiModel):
    page: PricePage | None = field(init=False)
    error: Error | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PricePage(ApiModel):
    number: int | None = field(init=False)
    size: int | None = field(init=False)
    prices: list[PricePageItem] | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ListCountrySpecsResponse(ApiModel):
    countries: dict[str, CountrySpecification] = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class CountrySpecification(ApiModel):
    country_code: str = field(init=False)
    country_name: str = field(init=False)
    currencies: list[str] = field(init=False)
    payment_methods: list[str] = field(init=False)
    payout_schedules: list[str] = field(init=False)
    bt_aging_specs: list[str] = field(init=False)
    legal_entity_types: list[str] = field(init=False)
    financial_account_types: list[str] = field(init=False)
    id_document_types: list[str] = field(init=False)
    banks: CountryBankDirectory | None = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class CountryBankDirectory(ApiModel):
    bank_account_type: str = field(init=False)
    code_scheme: str = field(init=False)
    items: list[CountryBank] = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class CountryBank(ApiModel):
    id: str = field(init=False)
    name: str = field(init=False)
    swift_code: str | None = field(init=False)
    sort_code_prefix: str | None = field(init=False)
    branches: list[CountryBankBranch] = field(init=False)

@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class CountryBankBranch(ApiModel):
    id: str = field(init=False)
    name: str = field(init=False)
    sort_code: str = field(init=False)

MessageTemplateAttachmentIDs: TypeAlias = list[str]
RefundReasonValue: TypeAlias = Literal['requested_by_customer', 'duplicate', 'fraudulent', 'order_canceled', 'item_returned', 'item_damaged', 'item_not_received', 'item_not_as_described', 'custom']
OrderLineItem: TypeAlias = OrderProductLineItem | OrderFeeLineItem | OrderShippingLineItem
PricePageItem: TypeAlias = CatalogPrice

def _is_public_model(value: Any) -> bool:
    try:
        return isinstance(value, type) and issubclass(value, ApiModel) and value is not ApiModel
    except TypeError:
        return False


__all__ = sorted(
    name
    for name, value in globals().items()
    if (
        _is_public_model(value)
        or name in {
            "MessageTemplateAttachmentIDs",
            "OrderLineItem",
            "PricePageItem",
            "RefundReasonValue",
        }
    )
    and "Response" not in name
    and not name.endswith("Envelope")
    and not name.endswith("Object")
)
