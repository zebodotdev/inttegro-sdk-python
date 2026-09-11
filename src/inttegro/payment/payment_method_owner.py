"""PaymentMethodOwner in the ``inttegro.payment`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PaymentMethodOwner(ApiModel):
    """Typed payment method owner data in the payment resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PaymentMethodSnapshotOwner``.
    """
    name: str = field(init=False)
    """Payment method owner's name. Required. Python type: ``str``; wire name: ``name``; JSON type: string. Constraints: minimum length 1"""
    address: OrderAddress | None = field(init=False)
    """The address associated with this payment method owner. Required; nullable. Python type: ``OrderAddress | None``; wire name: ``address``; JSON type: object"""

from inttegro.order.address import Address as OrderAddress
