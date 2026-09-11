"""PaymentMethodBankAccount in the ``inttegro.payment`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentMethodBankAccount(ApiModel):
    """Bank account details (present when type is bank_account).

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PaymentMethodSnapshotBankAccount``.
    """
    type: str = field(init=False)
    """Bank account sub-type. Required. Python type: ``str``; wire name: ``type``; JSON type: string. Constraints: allowed values ``ghana_bank_account``"""
    ghana_bank_account: PaymentMethodSnapshotGhanaBankAccount | None = field(init=False)
    """Ghana bank account details. Optional; nullable. Python type: ``PaymentMethodSnapshotGhanaBankAccount | None``; wire name: ``ghana_bank_account``; JSON type: object"""

from inttegro.payment.payment_method_ghana_bank_account import PaymentMethodGhanaBankAccount as PaymentMethodSnapshotGhanaBankAccount
