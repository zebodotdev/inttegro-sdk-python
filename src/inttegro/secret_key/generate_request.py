"""GenerateRequest in the ``inttegro.secret_key`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class GenerateRequest(ApiRequest):
    """Optional public input for secret key generation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``GenerateSecretKeyRequest``.
    """
    label: str | UnsetType = field(default=UNSET)
    """Optional human-readable label. Surrounding whitespace is trimmed; an empty value creates an unlabeled key. Optional. Python type: ``str``; wire name: ``label``; JSON type: string"""
