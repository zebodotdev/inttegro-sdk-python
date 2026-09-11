"""ReasonValue in the ``inttegro.refund`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from typing import Literal, TypeAlias


ReasonValue: TypeAlias = Literal['requested_by_customer', 'duplicate', 'fraudulent', 'order_canceled', 'item_returned', 'item_damaged', 'item_not_received', 'item_not_as_described', 'custom']
"""The lowercase refund-reason wire string returned by the API. Use :class:`Reason` when enum behavior is preferred."""
