"""PageRequest in the ``inttegro.customer`` resource namespace.

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

    API contract schema: ``PageCustomersRequest``.
    """
    page_size: int | UnsetType = field(default=UNSET)
    """The page size associated with this page request. Optional. Python type: ``int``; wire name: ``page_size``; JSON type: integer. Constraints: minimum 1; maximum 256"""
    page_number: int
    """The page number associated with this page request. Required. Python type: ``int``; wire name: ``page_number``; JSON type: integer. Constraints: minimum 1; maximum 10"""
