"""Response in the ``inttegro.balance_transaction`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Response(ApiModel):
    """Typed response returned by the response operation.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``BalanceTransactionResponse``.
    """
    transaction: BalanceTransaction = field(init=False)
    """Merchant balance entry caused by a payment or refund. `type` describes the semantic source, not direction. A payment transaction contains `payment_id`; a refund transaction contains `refund_id`. Exactly one matching reference is present. Required. Python type: ``BalanceTransaction``; wire name: ``transaction``; JSON type: object (BalanceTransaction)"""

from inttegro.balance_transaction.balance_transaction import BalanceTransaction
