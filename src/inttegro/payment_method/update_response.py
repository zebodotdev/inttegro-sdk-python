"""UpdateResponse in the ``inttegro.payment_method`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UpdateResponse(ApiModel):
    """Payment information if payment was initiated.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``UpdatePaymentMethodResponse``.
    """
    payment_method: PaymentMethod | None = field(init=False)
    """A tokenized payment instrument tied to a customer. Required; nullable. Python type: ``PaymentMethod | None``; wire name: ``payment_method``; JSON type: object (PaymentMethodObject)"""

from inttegro.payment_method.payment_method import PaymentMethod
