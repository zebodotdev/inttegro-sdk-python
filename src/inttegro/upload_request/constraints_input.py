"""ConstraintsInput in the ``inttegro.upload_request`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class ConstraintsInput(ApiRequest):
    """Parameters accepted by the constraints input operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``UploadRequestConstraintsInput``.
    """
    min_size: int | UnsetType = field(default=UNSET)
    """The min size associated with this constraints input. Optional. Python type: ``int``; wire name: ``min_size``; JSON type: integer (int64)"""
    max_size: int | UnsetType = field(default=UNSET)
    """The max size associated with this constraints input. Optional. Python type: ``int``; wire name: ``max_size``; JSON type: integer (int64)"""
    exact_size: int | UnsetType = field(default=UNSET)
    """The exact size associated with this constraints input. Optional. Python type: ``int``; wire name: ``exact_size``; JSON type: integer (int64)"""
    content_types: list[str] | UnsetType = field(default=UNSET)
    """The content types associated with this constraints input. Optional. Python type: ``list[str]``; wire name: ``content_types``; JSON type: array of string values"""
    extensions: list[str] | UnsetType = field(default=UNSET)
    """The extensions associated with this constraints input. Optional. Python type: ``list[str]``; wire name: ``extensions``; JSON type: array of string values"""
    filename: str | UnsetType = field(default=UNSET)
    """The filename associated with this constraints input. Optional. Python type: ``str``; wire name: ``filename``; JSON type: string"""
