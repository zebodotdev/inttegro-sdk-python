"""ReconcileRequest in the ``inttegro.file_reference`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class ReconcileRequest(ApiRequest):
    """Parameters accepted by the reconcile request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``FileReferenceReconcileRequest``.
    """
    references: list[FileReferenceInput] | UnsetType = field(default=UNSET)
    """The references associated with this reconcile request. Optional. Python type: ``list[FileReferenceInput]``; wire name: ``references``; JSON type: array of object (FileReferenceInput) values"""
    resource_type: str
    """Non-blank resource type after trimming. Required. Python type: ``str``; wire name: ``resource_type``; JSON type: string. Constraints: minimum length 1"""
    resource_id: str
    """Non-blank resource ID after trimming. Required. Python type: ``str``; wire name: ``resource_id``; JSON type: string. Constraints: minimum length 1"""

from inttegro.file_reference.input import Input as FileReferenceInput
