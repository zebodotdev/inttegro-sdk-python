"""PayoutConfiguration in the ``inttegro.payment`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PayoutConfiguration(ApiModel):
    """Typed payout configuration data in the payment resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PaymentPayoutConfiguration``.
    """
    enable_fx: Literal[False] = field(init=False)
    """The enable fx associated with this payout configuration. Required. Python type: ``Literal[False]``; wire name: ``enable_fx``; JSON type: boolean. Constraints: allowed values ``False``"""
    destination: PaymentPayoutConfigurationDestination = field(init=False)
    """The destination associated with this payout configuration. Required. Python type: ``PaymentPayoutConfigurationDestination``; wire name: ``destination``; JSON type: object"""

from inttegro.payment.payout_configuration_destination import PayoutConfigurationDestination as PaymentPayoutConfigurationDestination
