"""VerificationAttemptResult in the ``inttegro.otp`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class VerificationAttemptResult(ApiModel):
    """Typed verification attempt result data in the otp resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``OTPVerificationAttemptResult``.
    """
    detail: str | None = field(init=False)
    """Omitted when no detail is available. Optional; nullable. Python type: ``str | None``; wire name: ``detail``; JSON type: string"""
    verdict: Literal['fail', 'pass'] = field(init=False)
    """The verdict associated with this verification attempt result. Required. Python type: ``Literal['fail', 'pass']``; wire name: ``verdict``; JSON type: string. Constraints: allowed values ``fail``, ``pass``"""
