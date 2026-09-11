"""BillingDetailsInput in the ``inttegro.shared`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class BillingDetailsInput(ApiRequest):
    """Parameters accepted by the billing details input operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.
    """
    address: AddressInput | UnsetType = field(default=UNSET)
    """The address associated with this billing details input. Optional. Python type: ``AddressInput``; wire name: ``address``; JSON type: object (Address)"""
    name: str
    """Billing contact name. Required. Python type: ``str``; wire name: ``name``; JSON type: string"""
    email_address: str
    """Billing email address. Required. Python type: ``str``; wire name: ``email_address``; JSON type: string (email)"""
    phone_number: str
    """Billing phone number. Required. Python type: ``str``; wire name: ``phone_number``; JSON type: string"""

from inttegro.shared.address_input import AddressInput
