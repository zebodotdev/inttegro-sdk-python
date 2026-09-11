"""OwnerParams in the ``inttegro.bank_account`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass
from inttegro._request_base import ApiRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class OwnerParams(ApiRequest):
    """Parameters accepted by the owner params operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``FinancialAccountOwnerInput``.
    """
    name: str
    """Human-readable name of the owner param. Required. Python type: ``str``; wire name: ``name``; JSON type: string. Constraints: minimum length 1"""
    address: FinancialAccountOwnerInputAddress
    """The address associated with this owner param. Required. Python type: ``FinancialAccountOwnerInputAddress``; wire name: ``address``; JSON type: object"""

from inttegro.bank_account.owner_address_params import OwnerAddressParams as FinancialAccountOwnerInputAddress
