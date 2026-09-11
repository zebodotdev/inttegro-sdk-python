"""FeeLineItemFee in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel
from inttegro.money import Amount


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class FeeLineItemFee(ApiModel):
    """Typed fee line item fee data in the order resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``OrderFeeLineItemFee``.
    """
    id: str = field(init=False)
    """Immutable order-line identifier with the `oli_` prefix. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    description: str | None = field(init=False)
    """Human-readable description of the fee line item fee. Optional; nullable. Python type: ``str | None``; wire name: ``description``; JSON type: string"""
    tax_code: str | None = field(init=False)
    """The tax code associated with this fee line item fee. Optional; nullable. Python type: ``str | None``; wire name: ``tax_code``; JSON type: string"""
    amount: Amount = field(init=False)
    """Monetary amount, represented by a currency and an integer minor-unit value. Required. Python type: ``Amount``; wire name: ``amount``; JSON type: object (Amount)"""
    label: str = field(init=False)
    """The label associated with this fee line item fee. Required. Python type: ``str``; wire name: ``label``; JSON type: string"""
