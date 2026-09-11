"""AttributeInput in the ``inttegro.product`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass
from inttegro._request_base import ApiRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class AttributeInput(ApiRequest):
    """Parameters accepted by the attribute input operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``ProductAttributeInput``.
    """
    name: str
    """Human-readable name of the attribute input. Required. Python type: ``str``; wire name: ``name``; JSON type: string. Constraints: maximum length 100"""
    value: str
    """The value associated with this attribute input. Required. Python type: ``str``; wire name: ``value``; JSON type: string. Constraints: maximum length 500"""
