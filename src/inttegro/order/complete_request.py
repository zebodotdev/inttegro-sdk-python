"""CompleteRequest in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class CompleteRequest(ApiRequest):
    """Parameters accepted by the complete request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``CompleteOrderRequest``.
    """
    paid_out_of_band: bool | UnsetType = field(default=UNSET)
    """Whether paid out of band. Optional. Python type: ``bool``; wire name: ``paid_out_of_band``; JSON type: boolean"""
    order_id: str
    """The finalized Order to inspect or pay. Required. Python type: ``str``; wire name: ``order_id``; JSON type: string. Constraints: minimum length 1"""
