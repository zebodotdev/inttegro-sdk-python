"""WithAttemptResponse in the ``inttegro.upload_request`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class WithAttemptResponse(ApiModel):
    """Typed response returned by the with attempt operation.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``UploadRequestWithAttemptResponse``.
    """
    upload_request: UploadRequestWithAttemptObject = field(init=False)
    """The upload request associated with this with attempt response. Required. Python type: ``UploadRequestWithAttemptObject``; wire name: ``upload_request``; JSON type: object (UploadRequestWithAttemptObject)"""

from inttegro.upload_request.with_attempt_object import WithAttemptObject as UploadRequestWithAttemptObject
