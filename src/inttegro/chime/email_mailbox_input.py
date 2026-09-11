"""EmailMailboxInput in the ``inttegro.chime`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class EmailMailboxInput(ApiRequest):
    """Parameters accepted by the email mailbox input operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``ChimeEmailMailboxInput``.
    """
    name: str | UnsetType = field(default=UNSET)
    """Optional display name. Optional. Python type: ``str``; wire name: ``name``; JSON type: string"""
    address: str | UnsetType = field(default=UNSET)
    """Email address. Optional. Python type: ``str``; wire name: ``address``; JSON type: string (email)"""
