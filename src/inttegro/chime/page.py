"""Page in the ``inttegro.chime`` resource namespace.

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

    API contract schema: ``ChimePage``.
    """
    number: int = field(init=False)
    """Page number returned. Required. Python type: ``int``; wire name: ``number``; JSON type: integer"""
    size: int = field(init=False)
    """Page size returned. Required. Python type: ``int``; wire name: ``size``; JSON type: integer"""
    chimes: list[Chime] = field(init=False)
    """Chimes in this page. Required. Python type: ``list[Chime]``; wire name: ``chimes``; JSON type: array of object (Chime) values"""

from inttegro.chime.chime import Chime
