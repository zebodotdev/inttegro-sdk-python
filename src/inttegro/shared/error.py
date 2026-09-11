"""Error in the ``inttegro.shared`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Error(ApiModel):
    """Standard error response structure returned by all API endpoints. Provides machine-readable codes, human-readable messages, and actionable guidance for resolution.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.
    """
    message: str | None = field(init=False)
    """Concise, caller-safe explanation of why the request was rejected or could not finish. Optional; nullable. Python type: ``str | None``; wire name: ``message``; JSON type: string"""
    fix_code: str | None = field(init=False)
    """Machine-readable suggestion for how to resolve the error (e.g., "retry_with_exponential_backoff", "change_request_parameters"). Optional; nullable. Python type: ``str | None``; wire name: ``fix_code``; JSON type: string"""
    detail: str | None = field(init=False)
    """Explanation of the relevant rule and next safe action. It never contains raw dependency, storage, or implementation errors. Optional; nullable. Python type: ``str | None``; wire name: ``detail``; JSON type: string"""
    cause: str | None = field(init=False)
    """Stable category describing the reason for failure, such as invalid input, an unmet precondition, or a state conflict. Optional; nullable. Python type: ``str | None``; wire name: ``cause``; JSON type: string"""
    type: str = field(init=False)
    """Broad error category to help clients determine retry strategies (e.g., "invalid_request_parameter", "transient_error"). Required. Python type: ``str``; wire name: ``type``; JSON type: string"""
    code: str = field(init=False)
    """Unique machine-readable identifier for this specific error condition. Unlike type and cause which group errors, code pinpoints the exact problem. Required. Python type: ``str``; wire name: ``code``; JSON type: string"""
    url: str = field(init=False)
    """Link to error reference documentation with detailed explanation, common causes, and resolution guidance. Required. Python type: ``str``; wire name: ``url``; JSON type: string (uri)"""
