"""DocumentDelivery in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class DocumentDelivery(ApiModel):
    """Delivery result for one hosted order document link.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``OrderDocumentDelivery``.
    """
    deliveries: list[OrderDocumentDeliveryAttempt] | None = field(init=False)
    """Chime messages that were accepted for delivery. Optional; nullable. Python type: ``list[OrderDocumentDeliveryAttempt] | None``; wire name: ``deliveries``; JSON type: array of object (OrderDocumentDeliveryAttempt) values"""
    document_kind: Literal['invoice', 'receipt'] | None = field(init=False)
    """Hosted document that was delivered. Optional; nullable. Python type: ``Literal['invoice', 'receipt'] | None``; wire name: ``document_kind``; JSON type: string. Constraints: allowed values ``invoice``, ``receipt``"""
    document_url: str | None = field(init=False)
    """Hosted invoice or receipt URL sent to the customer. Receipt URLs use the hosted receipt path, not the invoice PDF path. Optional; nullable. Python type: ``str | None``; wire name: ``document_url``; JSON type: string (uri)"""
    failed_channels: list[Literal['email', 'sms']] | None = field(init=False)
    """Channels that failed to send. Optional; nullable. Python type: ``list[Literal['email', 'sms']] | None``; wire name: ``failed_channels``; JSON type: array of string values"""
    failures: list[OrderDocumentDeliveryFailure] | None = field(init=False)
    """Per-channel delivery failures. Optional; nullable. Python type: ``list[OrderDocumentDeliveryFailure] | None``; wire name: ``failures``; JSON type: array of object (OrderDocumentDeliveryFailure) values"""
    sent_channels: list[Literal['email', 'sms']] | None = field(init=False)
    """Channels accepted by Chime. Optional; nullable. Python type: ``list[Literal['email', 'sms']] | None``; wire name: ``sent_channels``; JSON type: array of string values"""

from inttegro.order.document_delivery_attempt import DocumentDeliveryAttempt as OrderDocumentDeliveryAttempt
from inttegro.order.document_delivery_failure import DocumentDeliveryFailure as OrderDocumentDeliveryFailure
