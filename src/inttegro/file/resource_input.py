"""ResourceInput in the ``inttegro.file`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class ResourceInput(ApiRequest):
    """Parameters accepted by the resource input operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``FileResourceInput``.
    """
    type: str | UnsetType = field(default=UNSET)
    """Discriminator identifying the resource input type. Optional. Python type: ``str``; wire name: ``type``; JSON type: string"""
    id: str | UnsetType = field(default=UNSET)
    """Unique identifier for this resource input. Optional. Python type: ``str``; wire name: ``id``; JSON type: string"""
    name: str | UnsetType = field(default=UNSET)
    """Human-readable name of the resource input. Optional. Python type: ``str``; wire name: ``name``; JSON type: string"""
