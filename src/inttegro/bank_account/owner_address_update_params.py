"""OwnerAddressUpdateParams in the ``inttegro.bank_account`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class OwnerAddressUpdateParams(ApiRequest):
    """Parameters accepted by the owner address update params operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``FinancialAccountOwnerUpdateInputAddress``.
    """
    city: str | UnsetType = field(default=UNSET)
    """The city associated with this owner address update param. Optional. Python type: ``str``; wire name: ``city``; JSON type: string"""
    country: str | UnsetType = field(default=UNSET)
    """The country associated with this owner address update param. Optional. Python type: ``str``; wire name: ``country``; JSON type: string"""
    line_1: str | UnsetType = field(default=UNSET)
    """The line 1 associated with this owner address update param. Optional. Python type: ``str``; wire name: ``line_1``; JSON type: string"""
    line_2: str | UnsetType = field(default=UNSET)
    """The line 2 associated with this owner address update param. Optional. Python type: ``str``; wire name: ``line_2``; JSON type: string"""
    name: str | UnsetType = field(default=UNSET)
    """Human-readable name of the owner address update param. Optional. Python type: ``str``; wire name: ``name``; JSON type: string"""
    phone: str | UnsetType = field(default=UNSET)
    """The phone associated with this owner address update param. Optional. Python type: ``str``; wire name: ``phone``; JSON type: string"""
    post_code: str | UnsetType = field(default=UNSET)
    """The post code associated with this owner address update param. Optional. Python type: ``str``; wire name: ``post_code``; JSON type: string"""
    region: str | UnsetType = field(default=UNSET)
    """The region associated with this owner address update param. Optional. Python type: ``str``; wire name: ``region``; JSON type: string"""
