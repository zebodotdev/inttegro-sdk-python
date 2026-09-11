"""AddressInput in the ``inttegro.customer`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class AddressInput(ApiRequest):
    """Parameters accepted by the address input operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``CustomerAddressInput``.
    """
    city: str | UnsetType = field(default=UNSET)
    """The city associated with this address input. Optional. Python type: ``str``; wire name: ``city``; JSON type: string"""
    line1: str | UnsetType = field(default=UNSET)
    """The line1 associated with this address input. Optional. Python type: ``str``; wire name: ``line1``; JSON type: string"""
    line2: str | UnsetType = field(default=UNSET)
    """The line2 associated with this address input. Optional. Python type: ``str``; wire name: ``line2``; JSON type: string"""
    name: str | UnsetType = field(default=UNSET)
    """Human-readable name of the address input. Optional. Python type: ``str``; wire name: ``name``; JSON type: string"""
    phone_number: str | UnsetType = field(default=UNSET)
    """Customer or recipient phone number in international form. Optional. Python type: ``str``; wire name: ``phone_number``; JSON type: string"""
    post_code: str | UnsetType = field(default=UNSET)
    """The post code associated with this address input. Optional. Python type: ``str``; wire name: ``post_code``; JSON type: string"""
    region: str | UnsetType = field(default=UNSET)
    """The region associated with this address input. Optional. Python type: ``str``; wire name: ``region``; JSON type: string"""
    country: str
    """The country associated with this address input. Required. Python type: ``str``; wire name: ``country``; JSON type: string"""
