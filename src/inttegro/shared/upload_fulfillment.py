"""UploadFulfillment in the ``inttegro.shared`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UploadFulfillment(ApiModel):
    """Typed upload fulfillment data in the shared resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.
    """
    upload_request: UploadRequest = field(init=False)
    """The upload request associated with this upload fulfillment. Required. Python type: ``UploadRequest``; wire name: ``upload_request``; JSON type: object (UploadRequestWithAttemptObject)"""
    file: FileUploadReceipt = field(init=False)
    """The file associated with this upload fulfillment. Required. Python type: ``FileUploadReceipt``; wire name: ``file``; JSON type: object (FileUploadReceipt)"""

from inttegro.file.upload_receipt import UploadReceipt as FileUploadReceipt
from inttegro.upload_request.upload_request import UploadRequest
