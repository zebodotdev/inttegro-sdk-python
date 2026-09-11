"""PageRequest in the ``inttegro.file`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class PageRequest(ApiRequest):
    """Parameters accepted by the page request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``PageFilesRequest``.
    """
    purpose: str | UnsetType = field(default=UNSET)
    """The purpose associated with this page request. Optional. Python type: ``str``; wire name: ``purpose``; JSON type: string"""
    status: Literal['uploading', 'processing', 'available', 'failed', 'deleted', FileStatus.UPLOADING, FileStatus.PROCESSING, FileStatus.AVAILABLE, FileStatus.FAILED, FileStatus.DELETED] | UnsetType = field(default=UNSET)
    """Current lifecycle status of the page request. Optional. Python type: ``Literal['uploading', 'processing', 'available', 'failed', 'deleted', FileStatus.UPLOADING, FileStatus.PROCESSING, FileStatus.AVAILABLE, FileStatus.FAILED, FileStatus.DELETED]``; wire name: ``status``; JSON type: string. Constraints: allowed values ``uploading``, ``processing``, ``available``, ``failed``, ``deleted``"""
    page_number: int | UnsetType = field(default=UNSET)
    """The page number associated with this page request. Optional. Python type: ``int``; wire name: ``page_number``; JSON type: integer. Constraints: minimum 1"""
    page_size: int | UnsetType = field(default=UNSET)
    """The page size associated with this page request. Optional. Python type: ``int``; wire name: ``page_size``; JSON type: integer. Constraints: minimum 1"""
    created_after: datetime | UnsetType = field(default=UNSET)
    """Timestamp for created after. Optional. Python type: ``datetime``; wire name: ``created_after``; JSON type: string (date-time)"""
    created_before: datetime | UnsetType = field(default=UNSET)
    """Timestamp for created before. Optional. Python type: ``datetime``; wire name: ``created_before``; JSON type: string (date-time)"""

from inttegro.file.status import Status as FileStatus
