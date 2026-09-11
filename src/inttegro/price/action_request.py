"""ActionRequest in the ``inttegro.price`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass
from inttegro._request_base import ApiRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class ActionRequest(ApiRequest):
    """Parameters accepted by the action request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``PriceActionRequest``.
    """
    price_id: str
    """Price ID to perform the action on. Required. Python type: ``str``; wire name: ``price_id``; JSON type: string"""
