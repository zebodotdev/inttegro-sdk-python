"""Response in the ``inttegro.file_link`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Response(ApiModel):
    """Typed response returned by the response operation.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``FileLinkResponse``.
    """
    file_link: FileLink = field(init=False)
    """Public file link metadata. Token hashes and provider URLs are not exposed. Required. Python type: ``FileLink``; wire name: ``file_link``; JSON type: object (FileLinkObject)"""

from inttegro.file_link.file_link import FileLink
