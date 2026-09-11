"""PageRequest in the ``inttegro.upload_request`` resource namespace.

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

    API contract schema: ``PageUploadRequestsRequest``.
    """
    purpose: str | UnsetType = field(default=UNSET)
    """The purpose associated with this page request. Optional. Python type: ``str``; wire name: ``purpose``; JSON type: string"""
    status: Literal['pending', 'uploading', 'fulfilled', 'expired', 'canceled', 'failed', UploadRequestStatus.PENDING, UploadRequestStatus.UPLOADING, UploadRequestStatus.FULFILLED, UploadRequestStatus.EXPIRED, UploadRequestStatus.CANCELED, UploadRequestStatus.FAILED] | UnsetType = field(default=UNSET)
    """Current lifecycle status of the page request. Optional. Python type: ``Literal['pending', 'uploading', 'fulfilled', 'expired', 'canceled', 'failed', UploadRequestStatus.PENDING, UploadRequestStatus.UPLOADING, UploadRequestStatus.FULFILLED, UploadRequestStatus.EXPIRED, UploadRequestStatus.CANCELED, UploadRequestStatus.FAILED]``; wire name: ``status``; JSON type: string. Constraints: allowed values ``pending``, ``uploading``, ``fulfilled``, ``expired``, ``canceled``, ``failed``"""
    resource: FileResourceInput | UnsetType = field(default=UNSET)
    """The resource associated with this page request. Optional. Python type: ``FileResourceInput``; wire name: ``resource``; JSON type: object (FileResource)"""
    page_number: int | UnsetType = field(default=UNSET)
    """The page number associated with this page request. Optional. Python type: ``int``; wire name: ``page_number``; JSON type: integer. Constraints: minimum 1"""
    page_size: int | UnsetType = field(default=UNSET)
    """The page size associated with this page request. Optional. Python type: ``int``; wire name: ``page_size``; JSON type: integer. Constraints: minimum 1"""

from inttegro.file.resource_input import ResourceInput as FileResourceInput
from inttegro.upload_request.status import Status as UploadRequestStatus
