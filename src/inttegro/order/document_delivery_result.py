"""DocumentDeliveryResult in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class DocumentDeliveryResult(ApiModel):
    """Response returned by deliberate order document delivery endpoints.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``OrderDocumentDeliveryResult``.
    """
    delivery: OrderDocumentDelivery | None = field(init=False)
    """Delivery result for one hosted order document link. Optional; nullable. Python type: ``OrderDocumentDelivery | None``; wire name: ``delivery``; JSON type: object (OrderDocumentDelivery)"""
    error: Error | None = field(init=False)
    """Standard error response structure returned by all API endpoints. Provides machine-readable codes, human-readable messages, and actionable guidance for resolution. Optional; nullable. Python type: ``Error | None``; wire name: ``error``; JSON type: object (Error)"""
    order: Order | None = field(init=False)
    """Complete order record with line items, customer details, payment state, and fulfillment information. Optional; nullable. Python type: ``Order | None``; wire name: ``order``; JSON type: object (Order)"""

from inttegro.shared.error import Error
from inttegro.order.order import Order
from inttegro.order.document_delivery import DocumentDelivery as OrderDocumentDelivery
