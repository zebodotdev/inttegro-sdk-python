"""CreatedOwnerAddress in the ``inttegro.bank_account`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class CreatedOwnerAddress(ApiModel):
    """Typed created owner address data in the bank account resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``FinancialAccountAddressCreateResponse``.
    """
    application_id: str = field(init=False)
    """Identifier of the related application. Required. Python type: ``str``; wire name: ``application_id``; JSON type: string"""
    city: str = field(init=False)
    """The city associated with this created owner address. Required. Python type: ``str``; wire name: ``city``; JSON type: string"""
    country: str = field(init=False)
    """The country associated with this created owner address. Required. Python type: ``str``; wire name: ``country``; JSON type: string"""
    id: str = field(init=False)
    """Empty in the current create response. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    line_1: str = field(init=False)
    """The line 1 associated with this created owner address. Required. Python type: ``str``; wire name: ``line_1``; JSON type: string"""
    line_2: str | None = field(init=False)
    """The line 2 associated with this created owner address. Optional; nullable. Python type: ``str | None``; wire name: ``line_2``; JSON type: string"""
    name: str = field(init=False)
    """Human-readable name of the created owner address. Required. Python type: ``str``; wire name: ``name``; JSON type: string"""
    phone: str | None = field(init=False)
    """The phone associated with this created owner address. Optional; nullable. Python type: ``str | None``; wire name: ``phone``; JSON type: string"""
    post_code: str | None = field(init=False)
    """The post code associated with this created owner address. Optional; nullable. Python type: ``str | None``; wire name: ``post_code``; JSON type: string"""
    region: str = field(init=False)
    """The region associated with this created owner address. Required. Python type: ``str``; wire name: ``region``; JSON type: string"""
