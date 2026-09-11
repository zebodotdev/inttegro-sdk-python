"""DisplayInput in the ``inttegro.upload_request`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class DisplayInput(ApiRequest):
    """Parameters accepted by the display input operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``UploadRequestDisplayInput``.
    """
    title: str | UnsetType = field(default=UNSET)
    """The title associated with this display input. Optional. Python type: ``str``; wire name: ``title``; JSON type: string"""
    description: str | UnsetType = field(default=UNSET)
    """Human-readable description of the display input. Optional. Python type: ``str``; wire name: ``description``; JSON type: string"""
    help_text: str | UnsetType = field(default=UNSET)
    """The help text associated with this display input. Optional. Python type: ``str``; wire name: ``help_text``; JSON type: string"""
