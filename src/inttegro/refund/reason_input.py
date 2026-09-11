"""ReasonInput in the ``inttegro.refund`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from typing import Literal, TypeAlias
from inttegro.refund.reason import Reason as RefundReason


ReasonInput: TypeAlias = Literal[
    'requested_by_customer',
    'duplicate',
    'fraudulent',
    'order_canceled',
    'item_returned',
    'item_damaged',
    'item_not_received',
    'item_not_as_described',
    'custom',
    RefundReason.REQUESTED_BY_CUSTOMER,
    RefundReason.DUPLICATE,
    RefundReason.FRAUDULENT,
    RefundReason.ORDER_CANCELED,
    RefundReason.ITEM_RETURNED,
    RefundReason.ITEM_DAMAGED,
    RefundReason.ITEM_NOT_RECEIVED,
    RefundReason.ITEM_NOT_AS_DESCRIBED,
    RefundReason.CUSTOM,
]
"""A refund reason accepted as either a :class:`Reason` member or its lowercase wire string. ``custom`` requires the operation's corresponding ``reason_details`` value."""
