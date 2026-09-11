"""Invoice in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Invoice(ApiModel):
    """Typed invoice data in the order resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``OrderInvoice``.
    """
    number: str | None = field(init=False)
    """Human-readable number assigned to the invoice. Optional; nullable. Python type: ``str | None``; wire name: ``number``; JSON type: string"""
    format: OrderInvoiceFormat = field(init=False)
    """The format associated with this invoice. Required. Python type: ``OrderInvoiceFormat``; wire name: ``format``; JSON type: object"""

from inttegro.order.invoice_format import InvoiceFormat as OrderInvoiceFormat
