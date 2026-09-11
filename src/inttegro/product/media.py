"""Media in the ``inttegro.product`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Media(ApiModel):
    """Typed media data in the product resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``ProductMedia``.
    """
    hero_image: str | None = field(init=False)
    """The hero image associated with this media. Optional; nullable. Python type: ``str | None``; wire name: ``hero_image``; JSON type: string"""
    thumbnail: str | None = field(init=False)
    """The thumbnail associated with this media. Optional; nullable. Python type: ``str | None``; wire name: ``thumbnail``; JSON type: string"""
    web_page_url: str | None = field(init=False)
    """URL used for web page. Optional; nullable. Python type: ``str | None``; wire name: ``web_page_url``; JSON type: string"""
    brand_logo: str | None = field(init=False)
    """The brand logo associated with this media. Optional; nullable. Python type: ``str | None``; wire name: ``brand_logo``; JSON type: string"""
    infographic: str | None = field(init=False)
    """The infographic associated with this media. Optional; nullable. Python type: ``str | None``; wire name: ``infographic``; JSON type: string"""
    promo_video: str | None = field(init=False)
    """The promo video associated with this media. Optional; nullable. Python type: ``str | None``; wire name: ``promo_video``; JSON type: string"""
    demo_video: str | None = field(init=False)
    """The demo video associated with this media. Optional; nullable. Python type: ``str | None``; wire name: ``demo_video``; JSON type: string"""
    gallery: list[str] | None = field(init=False)
    """The gallery associated with this media. Optional; nullable. Python type: ``list[str] | None``; wire name: ``gallery``; JSON type: array of string values"""
    downloads: list[str] | None = field(init=False)
    """The downloads associated with this media. Optional; nullable. Python type: ``list[str] | None``; wire name: ``downloads``; JSON type: array of string values"""
