"""FeeLineItemInput in the ``inttegro.shared`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Literal
from inttegro._request_base import ApiRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class FeeLineItemInput(ApiRequest):
    """Parameters accepted by the fee line item input operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.
    """
    type: Literal['fee', LineItemType.FEE]
    """Line item type discriminator. Required. Python type: ``Literal['fee', LineItemType.FEE]``; wire name: ``type``; JSON type: string. Constraints: allowed values ``fee``"""
    fee: FeeDetailsInput
    """The fee associated with this fee line item input. Required. Python type: ``FeeDetailsInput``; wire name: ``fee``; JSON type: object (FeeDetails)"""

from inttegro.shared.fee_details_input import FeeDetailsInput
from inttegro.order.line_item_type import LineItemType
