"""DeliveryInput in the ``inttegro.file_link`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class DeliveryInput(ApiRequest):
    """Parameters accepted by the delivery input operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``FileLinkDeliveryInput``.
    """
    mode: Literal['redirect', 'download', 'inline', FileLinkDeliveryMode.REDIRECT, FileLinkDeliveryMode.DOWNLOAD, FileLinkDeliveryMode.INLINE] | UnsetType = field(default=UNSET)
    """The mode associated with this delivery input. Optional. Python type: ``Literal['redirect', 'download', 'inline', FileLinkDeliveryMode.REDIRECT, FileLinkDeliveryMode.DOWNLOAD, FileLinkDeliveryMode.INLINE]``; wire name: ``mode``; JSON type: string. Constraints: allowed values ``redirect``, ``download``, ``inline``"""
    filename: str | UnsetType = field(default=UNSET)
    """The filename associated with this delivery input. Optional. Python type: ``str``; wire name: ``filename``; JSON type: string"""
    content_type: str | UnsetType = field(default=UNSET)
    """The content type associated with this delivery input. Optional. Python type: ``str``; wire name: ``content_type``; JSON type: string"""
    disposition: str | UnsetType = field(default=UNSET)
    """The disposition associated with this delivery input. Optional. Python type: ``str``; wire name: ``disposition``; JSON type: string"""

from inttegro.file_link.delivery_mode import DeliveryMode as FileLinkDeliveryMode
