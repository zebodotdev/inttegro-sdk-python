"""CreateRequestPrice in the ``inttegro.purchase_intent`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType
from inttegro.price.inline_params import InlineParams as PriceParams


@dataclass(frozen=True, slots=True, kw_only=True)
class CreateRequestPrice(ApiRequest):
    """Price selection for the Buy link. Send exactly one of id or nominal and at most one of original or original_id.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``CreatePurchaseIntentRequestPrice``.
    """
    id: str | UnsetType = field(default=UNSET)
    """Active, unarchived app-owned price ID that belongs to the selected product. Optional. Python type: ``str``; wire name: ``id``; JSON type: string"""
    nominal: PriceParams | UnsetType = field(default=UNSET)
    """Inline offer amount when no price ID is provided. Optional. Python type: ``PriceParams``; wire name: ``nominal``; JSON type: object (PriceParams)"""
    original: CreatePurchaseIntentRequestPriceOriginal | UnsetType = field(default=UNSET)
    """Optional original price used for comparison display. Optional. Python type: ``CreatePurchaseIntentRequestPriceOriginal``; wire name: ``original``; JSON type: object"""
    original_id: str | UnsetType = field(default=UNSET)
    """App-owned comparison price ID when not using original.id. Optional. Python type: ``str``; wire name: ``original_id``; JSON type: string"""

from inttegro.purchase_intent.create_request_price_original import CreateRequestPriceOriginal as CreatePurchaseIntentRequestPriceOriginal
