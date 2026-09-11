"""Page in the ``inttegro.price`` resource namespace.

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

    API contract schema: ``PricePage``.
    """
    number: int | None = field(init=False)
    """The page number returned. Optional; nullable. Python type: ``int | None``; wire name: ``number``; JSON type: integer"""
    size: int | None = field(init=False)
    """The number of prices in this page. Optional; nullable. Python type: ``int | None``; wire name: ``size``; JSON type: integer"""
    prices: list[PricePageItem] | None = field(init=False)
    """The prices associated with this page. Optional; nullable. Python type: ``list[PricePageItem] | None``; wire name: ``prices``; JSON type: array of object (PricePageItem) values"""

from inttegro.price.page_item import PageItem as PricePageItem
