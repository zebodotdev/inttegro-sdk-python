"""Customer in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Customer(ApiModel):
    """Typed customer data in the order resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``OrderCustomer``.
    """
    id: str = field(init=False)
    """Unique identifier for this customer. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    guest: bool = field(init=False)
    """Whether guest. Required. Python type: ``bool``; wire name: ``guest``; JSON type: boolean"""
    name: str = field(init=False)
    """Human-readable name of the customer. Required. Python type: ``str``; wire name: ``name``; JSON type: string"""
    email_address: str | None = field(init=False)
    """Customer or recipient email address. Optional; nullable. Python type: ``str | None``; wire name: ``email_address``; JSON type: string (email)"""
    phone_number: str | None = field(init=False)
    """Customer or recipient phone number in international form. Optional; nullable. Python type: ``str | None``; wire name: ``phone_number``; JSON type: string"""
    billing_address: OrderAddress | None = field(init=False)
    """The billing address associated with this customer. Optional; nullable. Python type: ``OrderAddress | None``; wire name: ``billing_address``; JSON type: object (OrderAddress)"""
    shipping_address: OrderAddress | None = field(init=False)
    """The shipping address associated with this customer. Optional; nullable. Python type: ``OrderAddress | None``; wire name: ``shipping_address``; JSON type: object (OrderAddress)"""

from inttegro.order.address import Address as OrderAddress
