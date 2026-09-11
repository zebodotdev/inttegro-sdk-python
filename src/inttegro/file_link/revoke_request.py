"""RevokeRequest in the ``inttegro.file_link`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class RevokeRequest(ApiRequest):
    """Parameters accepted by the revoke request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``RevokeFileLinkRequest``.
    """
    revoked_by: FileActorInput | UnsetType = field(default=UNSET)
    """The revoked by associated with this revoke request. Optional. Python type: ``FileActorInput``; wire name: ``revoked_by``; JSON type: object (FileActorInput)"""
    id: str
    """Unique identifier for this revoke request. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""

from inttegro.file.actor_input import ActorInput as FileActorInput
