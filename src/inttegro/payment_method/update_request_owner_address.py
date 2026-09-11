"""UpdateRequestOwnerAddress in the ``inttegro.payment_method`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class UpdateRequestOwnerAddress(ApiRequest):
    """Parameters accepted by the update request owner address operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``UpdatePaymentMethodRequestOwnerAddress``.
    """
    city: str | UnsetType = field(default=UNSET)
    """The city associated with this update request owner address. Optional. Python type: ``str``; wire name: ``city``; JSON type: string"""
    country: str | UnsetType = field(default=UNSET)
    """Country associated with the owner address. Optional. Python type: ``str``; wire name: ``country``; JSON type: string. Constraints: minimum length 1"""
    line1: str | UnsetType = field(default=UNSET)
    """The line1 associated with this update request owner address. Optional. Python type: ``str``; wire name: ``line1``; JSON type: string"""
    line2: str | UnsetType = field(default=UNSET)
    """The line2 associated with this update request owner address. Optional. Python type: ``str``; wire name: ``line2``; JSON type: string"""
    name: str | UnsetType = field(default=UNSET)
    """Human-readable name of the update request owner address. Optional. Python type: ``str``; wire name: ``name``; JSON type: string"""
    phone_number: str | UnsetType = field(default=UNSET)
    """Customer or recipient phone number in international form. Optional. Python type: ``str``; wire name: ``phone_number``; JSON type: string"""
    post_code: str | UnsetType = field(default=UNSET)
    """The post code associated with this update request owner address. Optional. Python type: ``str``; wire name: ``post_code``; JSON type: string"""
    region: str | UnsetType = field(default=UNSET)
    """The region associated with this update request owner address. Optional. Python type: ``str``; wire name: ``region``; JSON type: string"""
