"""UpdateRequestOwner in the ``inttegro.payment_method`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class UpdateRequestOwner(ApiRequest):
    """Parameters accepted by the update request owner operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``UpdatePaymentMethodRequestOwner``.
    """
    name: str | UnsetType = field(default=UNSET)
    """Payment method owner's name. Optional. Python type: ``str``; wire name: ``name``; JSON type: string. Constraints: minimum length 1"""
    address: UpdatePaymentMethodRequestOwnerAddress | UnsetType = field(default=UNSET)
    """The address associated with this update request owner. Optional. Python type: ``UpdatePaymentMethodRequestOwnerAddress``; wire name: ``address``; JSON type: object"""

from inttegro.payment_method.update_request_owner_address import UpdateRequestOwnerAddress as UpdatePaymentMethodRequestOwnerAddress
