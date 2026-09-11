"""AddressInput in the ``inttegro.shared`` resource namespace.

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
    """
    line2: str | UnsetType = field(default=UNSET)
    """Street address line 2 (optional). Optional. Python type: ``str``; wire name: ``line2``; JSON type: string"""
    region: str | UnsetType = field(default=UNSET)
    """State, province, or region. Optional. Python type: ``str``; wire name: ``region``; JSON type: string"""
    district: str | UnsetType = field(default=UNSET)
    """District or area. Optional. Python type: ``str``; wire name: ``district``; JSON type: string"""
    post_code: str | UnsetType = field(default=UNSET)
    """Postal/ZIP code. Optional. Python type: ``str``; wire name: ``post_code``; JSON type: string"""
    name: str
    """Recipient name. Required. Python type: ``str``; wire name: ``name``; JSON type: string"""
    phone_number: str
    """Contact phone number. Required. Python type: ``str``; wire name: ``phone_number``; JSON type: string"""
    line1: str
    """Street address line 1. Required. Python type: ``str``; wire name: ``line1``; JSON type: string"""
    town: str
    """City or town. Required. Python type: ``str``; wire name: ``town``; JSON type: string"""
    country: str
    """Country name. Required. Python type: ``str``; wire name: ``country``; JSON type: string"""
