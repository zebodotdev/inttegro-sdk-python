"""UsageRequest in the ``inttegro.secret_key`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class UsageRequest(ApiRequest):
    """Parameters accepted by the usage request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``SecretKeyUsageRequest``.
    """
    number: int | UnsetType = field(default=UNSET)
    """Page number. Omitted or 0 is normalized to 1. Optional. Python type: ``int``; wire name: ``number``; JSON type: integer. Constraints: minimum 0"""
    page: int | UnsetType = field(default=UNSET)
    """Page number alias. Omitted or 0 is normalized to 1. Optional. Python type: ``int``; wire name: ``page``; JSON type: integer. Constraints: minimum 0"""
    size: int | UnsetType = field(default=UNSET)
    """Requested page size. Omitted or 0 becomes 50; values above 100 are capped at 100. Optional. Python type: ``int``; wire name: ``size``; JSON type: integer. Constraints: minimum 0"""
    secret_key_id: str
    """Secret key identifier whose recent activity should be returned. Required. Python type: ``str``; wire name: ``secret_key_id``; JSON type: string"""
