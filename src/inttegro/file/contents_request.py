"""ContentsRequest in the ``inttegro.file`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class ContentsRequest(ApiRequest):
    """Parameters accepted by the contents request operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``FileContentsRequest``.
    """
    disposition: Literal['attachment', 'inline', FileDisposition.ATTACHMENT, FileDisposition.INLINE] | UnsetType = field(default=UNSET)
    """The disposition associated with this contents request. Optional. Python type: ``Literal['attachment', 'inline', FileDisposition.ATTACHMENT, FileDisposition.INLINE]``; wire name: ``disposition``; JSON type: string. Constraints: allowed values ``attachment``, ``inline``"""
    delivery: Literal['stream', 'redirect', FileDelivery.STREAM, FileDelivery.REDIRECT] | UnsetType = field(default=UNSET)
    """The delivery associated with this contents request. Optional. Python type: ``Literal['stream', 'redirect', FileDelivery.STREAM, FileDelivery.REDIRECT]``; wire name: ``delivery``; JSON type: string. Constraints: allowed values ``stream``, ``redirect``"""
    file_id: str
    """Identifier of the related file. Required. Python type: ``str``; wire name: ``file_id``; JSON type: string"""

from inttegro.file.delivery import Delivery as FileDelivery
from inttegro.file.disposition import Disposition as FileDisposition
