"""LookupRequest in the ``inttegro.secret_key`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass
from inttegro._request_base import ApiRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class LookupRequest(ApiRequest):
    """Parameters accepted by the lookup request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``LookupSecretKeyRequest``.
    """
    secret_key_id: str
    """Secret key identifier. Typed `sk_...` IDs are accepted. Required. Python type: ``str``; wire name: ``secret_key_id``; JSON type: string"""
