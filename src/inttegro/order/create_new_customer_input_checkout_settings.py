"""CreateNewCustomerInputCheckoutSettings in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class CreateNewCustomerInputCheckoutSettings(ApiRequest):
    """Checkout and payment flow configuration. Strongly recommended to provide both redirect_url and cancel_url for a delightful customer experience.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``CreateOrderNewCustomerInputCheckoutSettings``.
    """
    redirect_url: str | UnsetType = field(default=UNSET)
    """URL to redirect customer after payment completion. Optional. Python type: ``str``; wire name: ``redirect_url``; JSON type: string (uri)"""
    cancel_url: str | UnsetType = field(default=UNSET)
    """URL to redirect customer if they cancel payment. Optional. Python type: ``str``; wire name: ``cancel_url``; JSON type: string (uri)"""
