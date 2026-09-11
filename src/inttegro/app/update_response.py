"""UpdateResponse in the ``inttegro.app`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UpdateResponse(ApiModel):
    """Typed response returned by the update operation.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``UpdateApplicationResponse``.
    """
    app: UpdateApplicationResponseApp = field(init=False)
    """The app associated with this update response. Required. Python type: ``UpdateApplicationResponseApp``; wire name: ``app``; JSON type: object"""

from inttegro.app.update_response_app import UpdateResponseApp as UpdateApplicationResponseApp
