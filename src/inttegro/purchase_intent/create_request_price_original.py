"""CreateRequestPriceOriginal in the ``inttegro.purchase_intent`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType
from inttegro.price.inline_params import InlineParams as PriceParams


@dataclass(frozen=True, slots=True, kw_only=True)
class CreateRequestPriceOriginal(ApiRequest):
    """Optional original price used for comparison display.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``CreatePurchaseIntentRequestPriceOriginal``.
    """
    id: str | UnsetType = field(default=UNSET)
    """App-owned comparison price ID that belongs to the selected product. Optional. Python type: ``str``; wire name: ``id``; JSON type: string"""
    nominal: PriceParams | UnsetType = field(default=UNSET)
    """Inline original price amount. Optional. Python type: ``PriceParams``; wire name: ``nominal``; JSON type: object (PriceParams)"""
