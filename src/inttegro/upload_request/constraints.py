"""Constraints in the ``inttegro.upload_request`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Constraints(ApiModel):
    """Typed constraints data in the upload request resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``UploadRequestConstraints``.
    """
    min_size: int | None = field(init=False)
    """The min size associated with this constraint. Optional; nullable. Python type: ``int | None``; wire name: ``min_size``; JSON type: integer (int64)"""
    max_size: int | None = field(init=False)
    """The max size associated with this constraint. Optional; nullable. Python type: ``int | None``; wire name: ``max_size``; JSON type: integer (int64)"""
    exact_size: int | None = field(init=False)
    """The exact size associated with this constraint. Optional; nullable. Python type: ``int | None``; wire name: ``exact_size``; JSON type: integer (int64)"""
    content_types: list[str] | None = field(init=False)
    """The content types associated with this constraint. Optional; nullable. Python type: ``list[str] | None``; wire name: ``content_types``; JSON type: array of string values"""
    extensions: list[str] | None = field(init=False)
    """The extensions associated with this constraint. Optional; nullable. Python type: ``list[str] | None``; wire name: ``extensions``; JSON type: array of string values"""
    filename: str | None = field(init=False)
    """The filename associated with this constraint. Optional; nullable. Python type: ``str | None``; wire name: ``filename``; JSON type: string"""
