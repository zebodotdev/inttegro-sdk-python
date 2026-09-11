"""CreateLineItemInput in the ``inttegro.refund`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType
from inttegro.money import AmountParams


@dataclass(frozen=True, slots=True, kw_only=True)
class CreateLineItemInput(ApiRequest):
    """Parameters accepted by the create line item input operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``CreateRefundLineItemInput``.
    """
    reason: RefundReasonInput | UnsetType = field(default=UNSET)
    """The reason associated with this create line item input. Optional. Python type: ``RefundReasonInput``; wire name: ``reason``; JSON type: object (RefundReason)"""
    reason_details: str | UnsetType = field(default=UNSET)
    """Line-specific explanation. Requires a line-level reason; required when that reason is `custom`. Optional. Python type: ``str``; wire name: ``reason_details``; JSON type: string. Constraints: maximum length 2048"""
    order_line_item_id: str
    """Strong identifier for the paid order line item being refunded. Required. Python type: ``str``; wire name: ``order_line_item_id``; JSON type: string"""
    refund_amount: AmountParams
    """Monetary refund amount, represented by a currency and an integer minor-unit value. Required. Python type: ``AmountParams``; wire name: ``refund_amount``; JSON type: object (AmountParams)"""

from inttegro.refund.reason_input import ReasonInput as RefundReasonInput
