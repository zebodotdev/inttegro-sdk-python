"""FeeLineItem in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FeeLineItem(ApiModel):
    """Typed fee line item data in the order resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``OrderFeeLineItem``.
    """
    type: Literal['fee'] = field(init=False)
    """Discriminator identifying the fee line item type. Required. Python type: ``Literal['fee']``; wire name: ``type``; JSON type: string. Constraints: allowed values ``fee``"""
    fee: OrderFeeLineItemFee = field(init=False)
    """The fee associated with this fee line item. Required. Python type: ``OrderFeeLineItemFee``; wire name: ``fee``; JSON type: object"""

from inttegro.order.fee_line_item_fee import FeeLineItemFee as OrderFeeLineItemFee
