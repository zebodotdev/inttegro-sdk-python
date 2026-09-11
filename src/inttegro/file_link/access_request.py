"""AccessRequest in the ``inttegro.file_link`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class AccessRequest(ApiRequest):
    """Parameters accepted by the access request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``FileLinkAccessRequest``.
    """
    max_accesses: int | UnsetType = field(default=UNSET)
    """The max accesses associated with this access request. Optional. Python type: ``int``; wire name: ``max_accesses``; JSON type: integer (int64)"""
    allow_download: bool | UnsetType = field(default=UNSET)
    """Whether allow download. Optional. Python type: ``bool``; wire name: ``allow_download``; JSON type: boolean"""
    allowed_origins: list[str] | UnsetType = field(default=UNSET)
    """The allowed origins associated with this access request. Optional. Python type: ``list[str]``; wire name: ``allowed_origins``; JSON type: array of string values"""
    allowed_ip_ranges: list[str] | UnsetType = field(default=UNSET)
    """The allowed ip ranges associated with this access request. Optional. Python type: ``list[str]``; wire name: ``allowed_ip_ranges``; JSON type: array of string values"""
