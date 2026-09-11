"""PageResponse in the ``inttegro.upload_request`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PageResponse(ApiModel):
    """Typed response returned by the page operation.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``UploadRequestPageResponse``.
    """
    page: UploadRequestPage = field(init=False)
    """Numeric page used by this operation. Required. Python type: ``UploadRequestPage``; wire name: ``page``; JSON type: object (UploadRequestPage)"""

from inttegro.upload_request.page import Page as UploadRequestPage
