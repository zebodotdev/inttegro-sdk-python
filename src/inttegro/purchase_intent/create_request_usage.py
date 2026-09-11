"""CreateRequestUsage in the ``inttegro.purchase_intent`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class CreateRequestUsage(ApiRequest):
    """Optional link-use policy. Omit to create a reusable Buy link.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``CreatePurchaseIntentRequestUsage``.
    """
    single_use: bool | UnsetType = field(default=UNSET)
    """Creating the first order consumes the Buy link. Optional. Python type: ``bool``; wire name: ``single_use``; JSON type: boolean"""
    multi_use: bool | UnsetType = field(default=UNSET)
    """The Buy link may create multiple orders. Optional. Python type: ``bool``; wire name: ``multi_use``; JSON type: boolean"""
