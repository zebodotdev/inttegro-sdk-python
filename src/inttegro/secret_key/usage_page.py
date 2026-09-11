"""UsagePage in the ``inttegro.secret_key`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UsagePage(ApiModel):
    """One page of usage resources.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``SecretKeyUsagePage``.
    """
    number: int = field(init=False)
    """Human-readable number assigned to the usage page. Required. Python type: ``int``; wire name: ``number``; JSON type: integer. Constraints: minimum 1"""
    size: int = field(init=False)
    """Numeric size used by this operation. Required. Python type: ``int``; wire name: ``size``; JSON type: integer. Constraints: minimum 0"""
    count: int = field(init=False)
    """The count associated with this usage page. Required. Python type: ``int``; wire name: ``count``; JSON type: integer. Constraints: minimum 0"""
    total: int = field(init=False)
    """Monetary total, represented by a currency and an integer minor-unit value. Required. Python type: ``int``; wire name: ``total``; JSON type: integer. Constraints: minimum 0"""
    has_more: bool = field(init=False)
    """Whether has more. Required. Python type: ``bool``; wire name: ``has_more``; JSON type: boolean"""
    rows: list[SecretKeyUsageRow] = field(init=False)
    """The rows associated with this usage page. Required. Python type: ``list[SecretKeyUsageRow]``; wire name: ``rows``; JSON type: array of object (SecretKeyUsageRow) values"""

from inttegro.secret_key.usage_row import UsageRow as SecretKeyUsageRow
