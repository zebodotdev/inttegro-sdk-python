"""PageRequest in the ``inttegro.chime`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class PageRequest(ApiRequest):
    """Request to retrieve a page of chimes.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``PageChimesRequest``.
    """
    customer_id: str | UnsetType = field(default=UNSET)
    """Restrict the page to chimes associated with this customer. Optional. Python type: ``str``; wire name: ``customer_id``; JSON type: string"""
    page_number: int | UnsetType = field(default=UNSET)
    """1-based page index to fetch. Optional. Python type: ``int``; wire name: ``page_number``; JSON type: integer. Constraints: minimum 1; maximum 10"""
    page_size: int | UnsetType = field(default=UNSET)
    """Number of chimes to return. Optional. Python type: ``int``; wire name: ``page_size``; JSON type: integer. Constraints: minimum 1; maximum 256"""
    recipient: str | UnsetType = field(default=UNSET)
    """Restrict the page to chimes whose recipient exactly matches this phone number or email address. Optional. Python type: ``str``; wire name: ``recipient``; JSON type: string"""
