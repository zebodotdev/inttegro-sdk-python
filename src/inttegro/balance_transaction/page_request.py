"""PageRequest in the ``inttegro.balance_transaction`` resource namespace.

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

    API contract schema: ``PageBalanceTransactionsRequest``.
    """
    page_number: int
    """The page number associated with this page request. Required. Python type: ``int``; wire name: ``page_number``; JSON type: integer. Constraints: minimum 1; maximum 10"""
    page_size: int
    """The page size associated with this page request. Required. Python type: ``int``; wire name: ``page_size``; JSON type: integer. Constraints: minimum 1; maximum 256"""
