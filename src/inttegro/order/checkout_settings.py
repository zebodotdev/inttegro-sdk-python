"""CheckoutSettings in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class CheckoutSettings(ApiModel):
    """Checkout and payment flow configuration for this order.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``OrderCheckoutSettings``.
    """
    redirect_url: str | None = field(init=False)
    """URL to redirect the customer after payment completion. Optional; nullable. Python type: ``str | None``; wire name: ``redirect_url``; JSON type: string (uri)"""
    cancel_url: str | None = field(init=False)
    """URL to redirect the customer after canceling checkout. Optional; nullable. Python type: ``str | None``; wire name: ``cancel_url``; JSON type: string (uri)"""
