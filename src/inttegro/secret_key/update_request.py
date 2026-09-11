"""UpdateRequest in the ``inttegro.secret_key`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass
from inttegro._request_base import ApiRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class UpdateRequest(ApiRequest):
    """Parameters accepted by the update request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``UpdateSecretKeyRequest``.
    """
    label: str
    """Human-readable label for the secret key. Send an empty string to clear the label. Required. Python type: ``str``; wire name: ``label``; JSON type: string"""
    secret_key_id: str
    """Secret key identifier to update. Required. Python type: ``str``; wire name: ``secret_key_id``; JSON type: string"""
