"""OwnerInput in the ``inttegro.payment_method`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass
from inttegro._request_base import ApiRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class OwnerInput(ApiRequest):
    """Parameters accepted by the owner input operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``PaymentMethodOwnerInput``.
    """
    address: PaymentMethodOwnerInputAddress
    """The address associated with this owner input. Required. Python type: ``PaymentMethodOwnerInputAddress``; wire name: ``address``; JSON type: object"""
    name: str
    """Payment method owner's name. Required. Python type: ``str``; wire name: ``name``; JSON type: string. Constraints: minimum length 1"""

from inttegro.payment_method.owner_input_address import OwnerInputAddress as PaymentMethodOwnerInputAddress
