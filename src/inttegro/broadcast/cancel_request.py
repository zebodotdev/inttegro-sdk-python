"""CancelRequest in the ``inttegro.broadcast`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass
from inttegro._request_base import ApiRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class CancelRequest(ApiRequest):
    """Parameters accepted by the cancel request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``CancelBroadcastRequest``.
    """
    broadcast_id: str
    """Identifier of the related broadcast. Required. Python type: ``str``; wire name: ``broadcast_id``; JSON type: string"""
