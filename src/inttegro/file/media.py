"""Media in the ``inttegro.file`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Media(ApiModel):
    """Typed media data in the file resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``FileMedia``.
    """
    kind: str | None = field(init=False)
    """The kind associated with this media. Optional; nullable. Python type: ``str | None``; wire name: ``kind``; JSON type: string"""
    width: int | None = field(init=False)
    """The width associated with this media. Optional; nullable. Python type: ``int | None``; wire name: ``width``; JSON type: integer (int64)"""
    height: int | None = field(init=False)
    """The height associated with this media. Optional; nullable. Python type: ``int | None``; wire name: ``height``; JSON type: integer (int64)"""
    duration_ms: int | None = field(init=False)
    """The duration ms associated with this media. Optional; nullable. Python type: ``int | None``; wire name: ``duration_ms``; JSON type: integer (int64)"""
    page_count: int | None = field(init=False)
    """The page count associated with this media. Optional; nullable. Python type: ``int | None``; wire name: ``page_count``; JSON type: integer (int64)"""
    frame_count: int | None = field(init=False)
    """The frame count associated with this media. Optional; nullable. Python type: ``int | None``; wire name: ``frame_count``; JSON type: integer (int64)"""
    color_space: str | None = field(init=False)
    """The color space associated with this media. Optional; nullable. Python type: ``str | None``; wire name: ``color_space``; JSON type: string"""
    has_alpha: bool | None = field(init=False)
    """Whether has alpha. Optional; nullable. Python type: ``bool | None``; wire name: ``has_alpha``; JSON type: boolean"""
    codec: str | None = field(init=False)
    """The codec associated with this media. Optional; nullable. Python type: ``str | None``; wire name: ``codec``; JSON type: string"""
    aspect_ratio: str | None = field(init=False)
    """The aspect ratio associated with this media. Optional; nullable. Python type: ``str | None``; wire name: ``aspect_ratio``; JSON type: string"""
