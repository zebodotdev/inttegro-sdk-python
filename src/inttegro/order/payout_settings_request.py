"""PayoutSettingsRequest in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class PayoutSettingsRequest(ApiRequest):
    """Parameters accepted by the payout settings request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``OrderPayoutSettingsRequest``.
    """
    destination: OrderPayoutSettingsRequestDestination | UnsetType = field(default=UNSET)
    """The destination associated with this payout settings request. Optional. Python type: ``OrderPayoutSettingsRequestDestination``; wire name: ``destination``; JSON type: object"""
    enable_fx: Literal[False] | UnsetType = field(default=UNSET)
    """Omit this field or set it to false. Cross-currency payouts are not currently available. Optional. Python type: ``Literal[False]``; wire name: ``enable_fx``; JSON type: boolean. Constraints: allowed values ``False``"""

from inttegro.order.payout_settings_request_destination import PayoutSettingsRequestDestination as OrderPayoutSettingsRequestDestination
