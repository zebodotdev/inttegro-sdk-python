"""Merchant in the ``inttegro.purchase_intent`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Merchant(ApiModel):
    """Merchant identity captured for the hosted checkout. Individual fields are omitted when unavailable.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PurchaseIntentMerchant``.
    """
    app_name: str | None = field(init=False)
    """The app name associated with this merchant. Optional; nullable. Python type: ``str | None``; wire name: ``app_name``; JSON type: string"""
    organization_id: str | None = field(init=False)
    """Identifier of the related organization. Optional; nullable. Python type: ``str | None``; wire name: ``organization_id``; JSON type: string"""
    organization_name: str | None = field(init=False)
    """The organization name associated with this merchant. Optional; nullable. Python type: ``str | None``; wire name: ``organization_name``; JSON type: string"""
