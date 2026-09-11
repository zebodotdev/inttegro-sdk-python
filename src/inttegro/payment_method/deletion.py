"""Deletion in the ``inttegro.payment_method`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Deletion(ApiModel):
    """Typed deletion data in the payment method resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PaymentMethodDeletion``.
    """
    deleted: bool = field(init=False)
    """Whether deleted. Optional. Python type: ``bool``; wire name: ``deleted``; JSON type: boolean"""
    payment_method_id: str = field(init=False)
    """Identifier of the related payment method. Required. Python type: ``str``; wire name: ``payment_method_id``; JSON type: string"""
