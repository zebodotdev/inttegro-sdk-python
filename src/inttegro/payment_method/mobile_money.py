"""MobileMoney in the ``inttegro.payment_method`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class MobileMoney(ApiModel):
    """Masked mobile-money wallet details (present when type is mobile_money).

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PaymentMethodMobileMoney``.
    """
    account_number: str = field(init=False)
    """Masked wallet number. The full account number is never returned. Required. Python type: ``str``; wire name: ``account_number``; JSON type: string"""
    last4: str = field(init=False)
    """Last four numeric digits of the normalized wallet number. Required. Python type: ``str``; wire name: ``last4``; JSON type: string"""
    network: Literal['airtel', 'mtn', 'telecel', 'vodafone'] = field(init=False)
    """Mobile network operator. Required. Python type: ``Literal['airtel', 'mtn', 'telecel', 'vodafone']``; wire name: ``network``; JSON type: string. Constraints: allowed values ``airtel``, ``mtn``, ``telecel``, ``vodafone``"""
