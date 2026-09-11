"""ActivityVisitor in the ``inttegro.purchase_intent`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ActivityVisitor(ApiModel):
    """Typed activity visitor data in the purchase intent resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PurchaseIntentActivityVisitor``.
    """
    browser: str | None = field(init=False)
    """The browser associated with this activity visitor. Optional; nullable. Python type: ``str | None``; wire name: ``browser``; JSON type: string"""
    city: str | None = field(init=False)
    """The city associated with this activity visitor. Optional; nullable. Python type: ``str | None``; wire name: ``city``; JSON type: string"""
    country: str | None = field(init=False)
    """The country associated with this activity visitor. Optional; nullable. Python type: ``str | None``; wire name: ``country``; JSON type: string"""
    device: str | None = field(init=False)
    """The device associated with this activity visitor. Optional; nullable. Python type: ``str | None``; wire name: ``device``; JSON type: string"""
    ip_address: str | None = field(init=False)
    """Request IP address when retained for the activity type. Optional; nullable. Python type: ``str | None``; wire name: ``ip_address``; JSON type: string"""
    os: str | None = field(init=False)
    """The os associated with this activity visitor. Optional; nullable. Python type: ``str | None``; wire name: ``os``; JSON type: string"""
    region: str | None = field(init=False)
    """The region associated with this activity visitor. Optional; nullable. Python type: ``str | None``; wire name: ``region``; JSON type: string"""
    session_id: str | None = field(init=False)
    """Identifier of the related session. Optional; nullable. Python type: ``str | None``; wire name: ``session_id``; JSON type: string"""
    timezone: str | None = field(init=False)
    """The timezone associated with this activity visitor. Optional; nullable. Python type: ``str | None``; wire name: ``timezone``; JSON type: string"""
    user_agent: str | None = field(init=False)
    """The user agent associated with this activity visitor. Optional; nullable. Python type: ``str | None``; wire name: ``user_agent``; JSON type: string"""
    visitor_id: str | None = field(init=False)
    """Identifier of the related visitor. Optional; nullable. Python type: ``str | None``; wire name: ``visitor_id``; JSON type: string"""
