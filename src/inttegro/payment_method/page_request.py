"""PageRequest in the ``inttegro.payment_method`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class PageRequest(ApiRequest):
    """Parameters accepted by the page request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``PaymentMethodPageRequest``.
    """
    customer_id: str | UnsetType = field(default=UNSET)
    """Optional customer ID to scope the page to a single customer. Optional. Python type: ``str``; wire name: ``customer_id``; JSON type: string"""
    page_number: int | UnsetType = field(default=UNSET)
    """Page index to fetch. `0` is accepted and normalized to page 1; returned pages are numbered 1-10. Optional. Python type: ``int``; wire name: ``page_number``; JSON type: integer. Constraints: minimum 0; maximum 10"""
    page_size: int | UnsetType = field(default=UNSET)
    """Number of payment methods per page (1-256). Optional. Python type: ``int``; wire name: ``page_size``; JSON type: integer. Constraints: minimum 1; maximum 256"""
