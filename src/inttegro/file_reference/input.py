"""Input in the ``inttegro.file_reference`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class Input(ApiRequest):
    """Parameters accepted by the input operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``FileReferenceInput``.
    """
    reference: str | UnsetType = field(default=UNSET)
    """Caller-supplied file or file link reference. Optional. Python type: ``str``; wire name: ``reference``; JSON type: string"""
    reference_kind: str | UnsetType = field(default=UNSET)
    """Caller-defined reference kind; `file` and `file_link` are recommended. Optional. Python type: ``str``; wire name: ``reference_kind``; JSON type: string"""
    purpose: str | UnsetType = field(default=UNSET)
    """The purpose associated with this input. Optional. Python type: ``str``; wire name: ``purpose``; JSON type: string"""
    file_id: str
    """Non-blank file ID after trimming. Required. Python type: ``str``; wire name: ``file_id``; JSON type: string. Constraints: minimum length 1"""
    field: str
    """Non-blank resource field after trimming. Required. Python type: ``str``; wire name: ``field``; JSON type: string. Constraints: minimum length 1"""
