"""Settings in the ``inttegro.payment_method`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Settings(ApiModel):
    """Payment method acceptance configuration for an application.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PaymentMethodSettings``.
    """
    mobile_money: PaymentMethodTypeSetting | None = field(init=False)
    """Settings for a specific payment method type. Optional; nullable. Python type: ``PaymentMethodTypeSetting | None``; wire name: ``mobile_money``; JSON type: object (PaymentMethodTypeSetting)"""
    bank_account: PaymentMethodTypeSetting | None = field(init=False)
    """Settings for a specific payment method type. Optional; nullable. Python type: ``PaymentMethodTypeSetting | None``; wire name: ``bank_account``; JSON type: object (PaymentMethodTypeSetting)"""
    card: PaymentMethodTypeSetting | None = field(init=False)
    """Settings for a specific payment method type. Optional; nullable. Python type: ``PaymentMethodTypeSetting | None``; wire name: ``card``; JSON type: object (PaymentMethodTypeSetting)"""
    motito: PaymentMethodTypeSetting | None = field(init=False)
    """Settings for a specific payment method type. Optional; nullable. Python type: ``PaymentMethodTypeSetting | None``; wire name: ``motito``; JSON type: object (PaymentMethodTypeSetting)"""

from inttegro.payment_method.type_setting import TypeSetting as PaymentMethodTypeSetting
