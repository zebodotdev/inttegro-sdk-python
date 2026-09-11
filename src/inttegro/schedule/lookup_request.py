"""LookupRequest in the ``inttegro.schedule`` resource namespace.

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

    API contract schema: ``LookupScheduleRequest``.
    """
    schedule_id: str
    """Identifier of the related schedule. Required. Python type: ``str``; wire name: ``schedule_id``; JSON type: string"""
