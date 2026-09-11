"""Page in the ``inttegro.payment_method`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Page(ApiModel):
    """One page of page resources.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PaymentMethodPage``.
    """
    number: int = field(init=False)
    """The page number returned. Required. Python type: ``int``; wire name: ``number``; JSON type: integer"""
    payment_methods: list[PaymentMethod] = field(init=False)
    """The payment methods associated with this page. Required. Python type: ``list[PaymentMethod]``; wire name: ``payment_methods``; JSON type: array of object (PaymentMethodObject) values"""
    size: int = field(init=False)
    """The number of payment methods in this page. Required. Python type: ``int``; wire name: ``size``; JSON type: integer"""

from inttegro.payment_method.payment_method import PaymentMethod
