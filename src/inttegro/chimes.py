"""Typed request objects for chime and broadcast operations."""

from .request_types import (
    BroadcastRequest,
    BroadcastRequestRequestMeta as BroadcastRequestMeta,
    ChimeEmailMailboxInput as EmailMailbox,
    ChimeEmailMessageInput as EmailMessage,
    ChimeInlineRecipientInputVariant1 as PhoneRecipient,
    ChimeInlineRecipientInputVariant1Phone as Phone,
    ChimeInlineRecipientInputVariant2 as EmailRecipient,
    ChimeInlineRecipientInputVariant2Email as Email,
    ChimeSavedCustomerRecipientInput as SavedCustomerRecipient,
    MessageTemplateReferenceInput as TemplateReference,
    PageChimesRequest as PageRequest,
    ScheduleChimeRequest as ScheduleRequest,
    ScheduleChimeRequestRequestMeta as ScheduleRequestMeta,
    SendChimeRequest as SendRequest,
    SendChimeRequestRequestMeta as SendRequestMeta,
)

__all__ = [
    "BroadcastRequest",
    "BroadcastRequestMeta",
    "Email",
    "EmailMailbox",
    "EmailMessage",
    "EmailRecipient",
    "PageRequest",
    "Phone",
    "PhoneRecipient",
    "SavedCustomerRecipient",
    "ScheduleRequest",
    "ScheduleRequestMeta",
    "SendRequest",
    "SendRequestMeta",
    "TemplateReference",
]
