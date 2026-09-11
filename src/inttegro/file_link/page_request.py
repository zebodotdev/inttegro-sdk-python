"""PageRequest in the ``inttegro.file_link`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class PageRequest(ApiRequest):
    """Parameters accepted by the page request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``PageFileLinksRequest``.
    """
    file_id: str | UnsetType = field(default=UNSET)
    """Identifier of the related file. Optional. Python type: ``str``; wire name: ``file_id``; JSON type: string"""
    status: Literal['active', 'revoked', 'expired', 'disabled', FileLinkStatus.ACTIVE, FileLinkStatus.REVOKED, FileLinkStatus.EXPIRED, FileLinkStatus.DISABLED] | UnsetType = field(default=UNSET)
    """Current lifecycle status of the page request. Optional. Python type: ``Literal['active', 'revoked', 'expired', 'disabled', FileLinkStatus.ACTIVE, FileLinkStatus.REVOKED, FileLinkStatus.EXPIRED, FileLinkStatus.DISABLED]``; wire name: ``status``; JSON type: string. Constraints: allowed values ``active``, ``revoked``, ``expired``, ``disabled``"""
    page_number: int | UnsetType = field(default=UNSET)
    """The page number associated with this page request. Optional. Python type: ``int``; wire name: ``page_number``; JSON type: integer. Constraints: minimum 1"""
    page_size: int | UnsetType = field(default=UNSET)
    """The page size associated with this page request. Optional. Python type: ``int``; wire name: ``page_size``; JSON type: integer. Constraints: minimum 1"""

from inttegro.file_link.status import Status as FileLinkStatus
