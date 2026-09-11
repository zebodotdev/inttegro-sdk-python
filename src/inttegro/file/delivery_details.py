"""DeliveryDetails in the ``inttegro.file`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class DeliveryDetails(ApiModel):
    """Purpose-authorized public delivery metadata for browser-rendered assets. Callers should store file IDs as canonical references and treat these URLs as render URLs.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``FileDeliveryDetails``.
    """
    public_url: str | None = field(init=False)
    """Unsigned CDN URL for public-safe assets such as product images. Optional; nullable. Python type: ``str | None``; wire name: ``public_url``; JSON type: string (uri)"""
    cache_control: str | None = field(init=False)
    """The cache control associated with this delivery detail. Optional; nullable. Python type: ``str | None``; wire name: ``cache_control``; JSON type: string"""
    content_type: str | None = field(init=False)
    """The content type associated with this delivery detail. Optional; nullable. Python type: ``str | None``; wire name: ``content_type``; JSON type: string"""
