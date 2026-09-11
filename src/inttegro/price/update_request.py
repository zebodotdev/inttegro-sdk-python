"""UpdateRequest in the ``inttegro.price`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class UpdateRequest(ApiRequest):
    """Parameters accepted by the update request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``UpdatePriceRequest``.
    """
    label: str | UnsetType = field(default=UNSET)
    """Optional short label for the new price. Optional. Python type: ``str``; wire name: ``label``; JSON type: string. Constraints: maximum length 100"""
    about: str | UnsetType = field(default=UNSET)
    """Optional internal description for the new price. Optional. Python type: ``str``; wire name: ``about``; JSON type: string. Constraints: maximum length 500"""
    price_id: str
    """Identifier of the related price. Required. Python type: ``str``; wire name: ``price_id``; JSON type: string"""
