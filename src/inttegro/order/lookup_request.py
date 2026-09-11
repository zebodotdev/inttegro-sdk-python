"""LookupRequest in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass
from inttegro._request_base import ApiRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class LookupRequest(ApiRequest):
    """Parameters accepted by the lookup request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``LookupOrderRequest``.
    """
    order_id: str
    """The finalized Order to inspect or pay. Required. Python type: ``str``; wire name: ``order_id``; JSON type: string. Constraints: minimum length 1"""
