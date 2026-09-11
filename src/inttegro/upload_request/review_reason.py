"""ReviewReason in the ``inttegro.upload_request`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ReviewReason(ApiModel):
    """Typed review reason data in the upload request resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``UploadRequestReviewReason``.
    """
    code: str = field(init=False)
    """The code associated with this review reason. Required. Python type: ``str``; wire name: ``code``; JSON type: string. Constraints: minimum length 1"""
    message: str = field(init=False)
    """The message associated with this review reason. Required. Python type: ``str``; wire name: ``message``; JSON type: string. Constraints: minimum length 1"""
    param: str | None = field(init=False)
    """The param associated with this review reason. Optional; nullable. Python type: ``str | None``; wire name: ``param``; JSON type: string"""
