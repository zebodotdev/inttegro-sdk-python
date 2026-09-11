"""Usage in the ``inttegro.secret_key`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Usage(ApiModel):
    """Typed usage data in the secret key resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``SecretKeyUsage``.
    """
    key: SecretKey = field(init=False)
    """Public secret key metadata. The bearer token is never returned by read or mutation endpoints. Required. Python type: ``SecretKey``; wire name: ``key``; JSON type: object (SecretKey)"""
    usage: SecretKeyUsagePage = field(init=False)
    """The usage associated with this usage. Required. Python type: ``SecretKeyUsagePage``; wire name: ``usage``; JSON type: object (SecretKeyUsagePage)"""

from inttegro.secret_key.secret_key import SecretKey
from inttegro.secret_key.usage_page import UsagePage as SecretKeyUsagePage
