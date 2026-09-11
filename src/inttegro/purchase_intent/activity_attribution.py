"""ActivityAttribution in the ``inttegro.purchase_intent`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ActivityAttribution(ApiModel):
    """Typed activity attribution data in the purchase intent resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PurchaseIntentActivityAttribution``.
    """
    campaign: str | None = field(init=False)
    """The campaign associated with this activity attribution. Optional; nullable. Python type: ``str | None``; wire name: ``campaign``; JSON type: string"""
    channel: str | None = field(init=False)
    """The channel associated with this activity attribution. Optional; nullable. Python type: ``str | None``; wire name: ``channel``; JSON type: string"""
    content: str | None = field(init=False)
    """The content associated with this activity attribution. Optional; nullable. Python type: ``str | None``; wire name: ``content``; JSON type: string"""
    landing_url: str | None = field(init=False)
    """URL used for landing. Optional; nullable. Python type: ``str | None``; wire name: ``landing_url``; JSON type: string"""
    medium: str | None = field(init=False)
    """The medium associated with this activity attribution. Optional; nullable. Python type: ``str | None``; wire name: ``medium``; JSON type: string"""
    referrer: str | None = field(init=False)
    """The referrer associated with this activity attribution. Optional; nullable. Python type: ``str | None``; wire name: ``referrer``; JSON type: string"""
    referrer_host: str | None = field(init=False)
    """The referrer host associated with this activity attribution. Optional; nullable. Python type: ``str | None``; wire name: ``referrer_host``; JSON type: string"""
    source: str | None = field(init=False)
    """The source associated with this activity attribution. Optional; nullable. Python type: ``str | None``; wire name: ``source``; JSON type: string"""
    term: str | None = field(init=False)
    """The term associated with this activity attribution. Optional; nullable. Python type: ``str | None``; wire name: ``term``; JSON type: string"""
