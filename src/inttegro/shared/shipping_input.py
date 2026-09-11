"""ShippingInput in the ``inttegro.shared`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass
from inttegro._request_base import ApiRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class ShippingInput(ApiRequest):
    """Parameters accepted by the shipping input operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.
    """
    address: AddressInput
    """The address associated with this shipping input. Required. Python type: ``AddressInput``; wire name: ``address``; JSON type: object (Address)"""

from inttegro.shared.address_input import AddressInput
