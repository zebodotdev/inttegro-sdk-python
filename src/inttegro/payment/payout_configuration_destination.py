"""PayoutConfigurationDestination in the ``inttegro.payment`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PayoutConfigurationDestination(ApiModel):
    """Typed payout configuration destination data in the payment resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PaymentPayoutConfigurationDestination``.
    """
    financial_account_id: str = field(init=False)
    """Same-currency financial account with push capability enabled. Required. Python type: ``str``; wire name: ``financial_account_id``; JSON type: string"""
