"""TypeSetting in the ``inttegro.payment_method`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class TypeSetting(ApiModel):
    """Settings for a specific payment method type.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PaymentMethodTypeSetting``.
    """
    type: Literal['mobile_money', 'bank_account', 'card', 'motito'] | None = field(init=False)
    """Payment method type. Optional; nullable. Python type: ``Literal['mobile_money', 'bank_account', 'card', 'motito'] | None``; wire name: ``type``; JSON type: string. Constraints: allowed values ``mobile_money``, ``bank_account``, ``card``, ``motito``"""
    name: str | None = field(init=False)
    """Human-readable name. Optional; nullable. Python type: ``str | None``; wire name: ``name``; JSON type: string"""
    description: str | None = field(init=False)
    """Description of this payment method. Optional; nullable. Python type: ``str | None``; wire name: ``description``; JSON type: string"""
    enabled: bool = field(init=False)
    """Whether this payment type can be used. Required. Python type: ``bool``; wire name: ``enabled``; JSON type: boolean"""
    confirms_use: bool = field(init=False)
    """Whether customers must explicitly agree before using. Required. Python type: ``bool``; wire name: ``confirms_use``; JSON type: boolean"""
