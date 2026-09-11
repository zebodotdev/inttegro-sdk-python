"""PaymentMethod in the ``inttegro.payment`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentMethod(ApiModel):
    """Typed payment method data in the payment resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PaymentMethodSnapshot``.
    """
    id: str = field(init=False)
    """Unique identifier for this payment method. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    bank_account: PaymentMethodSnapshotBankAccount | None = field(init=False)
    """The bank account associated with this payment method. Optional; nullable. Python type: ``PaymentMethodSnapshotBankAccount | None``; wire name: ``bank_account``; JSON type: object"""
    card: PaymentMethodCard | None = field(init=False)
    """Card marker. Nested card credentials are not returned. Optional; nullable. Python type: ``PaymentMethodCard | None``; wire name: ``card``; JSON type: object (PaymentMethodCard)"""
    created_at: datetime = field(init=False)
    """When the payment method was created. Required. Python type: ``datetime``; wire name: ``created_at``; JSON type: string (date-time)"""
    customer_id: str = field(init=False)
    """Identifier of the related customer. Required. Python type: ``str``; wire name: ``customer_id``; JSON type: string"""
    mobile_money: PaymentMethodSnapshotMobileMoney | None = field(init=False)
    """The mobile money associated with this payment method. Optional; nullable. Python type: ``PaymentMethodSnapshotMobileMoney | None``; wire name: ``mobile_money``; JSON type: object"""
    owner: PaymentMethodSnapshotOwner | None = field(init=False)
    """The owner associated with this payment method. Optional; nullable. Python type: ``PaymentMethodSnapshotOwner | None``; wire name: ``owner``; JSON type: object"""
    type: Literal['mobile_money', 'bank_account', 'card', 'motito'] = field(init=False)
    """Discriminator identifying the payment method type. Required. Python type: ``Literal['mobile_money', 'bank_account', 'card', 'motito']``; wire name: ``type``; JSON type: string. Constraints: allowed values ``mobile_money``, ``bank_account``, ``card``, ``motito``"""
    verified: bool = field(init=False)
    """Whether verified. Required. Python type: ``bool``; wire name: ``verified``; JSON type: boolean"""
    verified_at: datetime | None = field(init=False)
    """Timestamp for verified at. Optional; nullable. Python type: ``datetime | None``; wire name: ``verified_at``; JSON type: string (date-time)"""

from inttegro.payment_method.card import Card as PaymentMethodCard
from inttegro.payment.payment_method_bank_account import PaymentMethodBankAccount as PaymentMethodSnapshotBankAccount
from inttegro.payment.payment_method_mobile_money import PaymentMethodMobileMoney as PaymentMethodSnapshotMobileMoney
from inttegro.payment.payment_method_owner import PaymentMethodOwner as PaymentMethodSnapshotOwner
