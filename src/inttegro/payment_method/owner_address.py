"""OwnerAddress in the ``inttegro.payment_method`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class OwnerAddress(ApiModel):
    """Postal address for the owner when available.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PaymentMethodOwnerAddress``.
    """
    city: str | None = field(init=False)
    """City or locality. Optional; nullable. Python type: ``str | None``; wire name: ``city``; JSON type: string"""
    country: str = field(init=False)
    """Two-letter ISO country code. Required. Python type: ``str``; wire name: ``country``; JSON type: string"""
    line_1: str | None = field(init=False)
    """First line of the street address. Optional; nullable. Python type: ``str | None``; wire name: ``line_1``; JSON type: string"""
    line_2: str | None = field(init=False)
    """Second line of the street address. Optional; nullable. Python type: ``str | None``; wire name: ``line_2``; JSON type: string"""
    name: str | None = field(init=False)
    """Recipient name at this address, if different from owner name. Optional; nullable. Python type: ``str | None``; wire name: ``name``; JSON type: string"""
    phone_number: str | None = field(init=False)
    """Phone number for this address. Optional; nullable. Python type: ``str | None``; wire name: ``phone_number``; JSON type: string"""
    post_code: str | None = field(init=False)
    """Postal or ZIP code. Optional; nullable. Python type: ``str | None``; wire name: ``post_code``; JSON type: string"""
    region: str | None = field(init=False)
    """Region, state, or province. Optional; nullable. Python type: ``str | None``; wire name: ``region``; JSON type: string"""
