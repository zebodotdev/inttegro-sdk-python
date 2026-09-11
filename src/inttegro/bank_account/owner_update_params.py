"""OwnerUpdateParams in the ``inttegro.bank_account`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class OwnerUpdateParams(ApiRequest):
    """Parameters accepted by the owner update params operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``FinancialAccountOwnerUpdateInput``.
    """
    name: str | UnsetType = field(default=UNSET)
    """Human-readable name of the owner update param. Optional. Python type: ``str``; wire name: ``name``; JSON type: string"""
    address: FinancialAccountOwnerUpdateInputAddress | UnsetType = field(default=UNSET)
    """The address associated with this owner update param. Optional. Python type: ``FinancialAccountOwnerUpdateInputAddress``; wire name: ``address``; JSON type: object"""

from inttegro.bank_account.owner_address_update_params import OwnerAddressUpdateParams as FinancialAccountOwnerUpdateInputAddress
