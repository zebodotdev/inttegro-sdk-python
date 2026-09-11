"""MediaInput in the ``inttegro.product`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class MediaInput(ApiRequest):
    """Parameters accepted by the media input operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``ProductMediaInput``.
    """
    hero_image: str | UnsetType = field(default=UNSET)
    """The hero image associated with this media input. Optional. Python type: ``str``; wire name: ``hero_image``; JSON type: string"""
    thumbnail: str | UnsetType = field(default=UNSET)
    """The thumbnail associated with this media input. Optional. Python type: ``str``; wire name: ``thumbnail``; JSON type: string"""
    web_page_url: str | UnsetType = field(default=UNSET)
    """URL used for web page. Optional. Python type: ``str``; wire name: ``web_page_url``; JSON type: string"""
    brand_logo: str | UnsetType = field(default=UNSET)
    """The brand logo associated with this media input. Optional. Python type: ``str``; wire name: ``brand_logo``; JSON type: string"""
    infographic: str | UnsetType = field(default=UNSET)
    """The infographic associated with this media input. Optional. Python type: ``str``; wire name: ``infographic``; JSON type: string"""
    promo_video: str | UnsetType = field(default=UNSET)
    """The promo video associated with this media input. Optional. Python type: ``str``; wire name: ``promo_video``; JSON type: string"""
    demo_video: str | UnsetType = field(default=UNSET)
    """The demo video associated with this media input. Optional. Python type: ``str``; wire name: ``demo_video``; JSON type: string"""
    gallery: list[str] | UnsetType = field(default=UNSET)
    """The gallery associated with this media input. Optional. Python type: ``list[str]``; wire name: ``gallery``; JSON type: array of string values"""
    downloads: list[str] | UnsetType = field(default=UNSET)
    """The downloads associated with this media input. Optional. Python type: ``list[str]``; wire name: ``downloads``; JSON type: array of string values"""
