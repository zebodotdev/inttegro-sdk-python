"""PageRequest in the ``inttegro.price`` resource namespace.

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

    API contract schema: ``PricePageRequest``.
    """
    page_number: int | UnsetType = field(default=UNSET)
    """Page index to fetch. Omit it or send 0 to request page 1; otherwise use 1 through 10. Optional. Python type: ``int``; wire name: ``page_number``; JSON type: integer. Constraints: minimum 0; maximum 10"""
    page_size: int | UnsetType = field(default=UNSET)
    """Number of prices per page (1-256). Optional. Python type: ``int``; wire name: ``page_size``; JSON type: integer. Constraints: minimum 1; maximum 256"""
    product_id: str | UnsetType = field(default=UNSET)
    """Optional product ID to scope the page to a single product. Optional. Python type: ``str``; wire name: ``product_id``; JSON type: string"""
