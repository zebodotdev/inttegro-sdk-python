"""PageRequest in the ``inttegro.purchase_intent`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass
from inttegro._request_base import ApiRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class PageRequest(ApiRequest):
    """Parameters accepted by the page request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``PagePurchaseIntentsRequest``.
    """
    page_number: int
    """One-based page number to retrieve. Required. Python type: ``int``; wire name: ``page_number``; JSON type: integer. Constraints: minimum 1; maximum 10"""
    page_size: int
    """Maximum number of purchase intents to return on this page. Required. Python type: ``int``; wire name: ``page_size``; JSON type: integer. Constraints: minimum 1; maximum 256"""
