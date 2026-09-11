"""UploadReceipt in the ``inttegro.file`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UploadReceipt(ApiModel):
    """Typed upload receipt data in the file resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``FileUploadReceipt``.
    """
    content_type: str = field(init=False)
    """The content type associated with this upload receipt. Required. Python type: ``str``; wire name: ``content_type``; JSON type: string"""
    created_at: datetime = field(init=False)
    """When the upload receipt was created. Required. Python type: ``datetime``; wire name: ``created_at``; JSON type: string (date-time)"""
    filename: str | None = field(init=False)
    """The filename associated with this upload receipt. Optional; nullable. Python type: ``str | None``; wire name: ``filename``; JSON type: string"""
    id: str = field(init=False)
    """Unique identifier for this upload receipt. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    name: str | None = field(init=False)
    """Human-readable name of the upload receipt. Optional; nullable. Python type: ``str | None``; wire name: ``name``; JSON type: string"""
    size: int = field(init=False)
    """Numeric size used by this operation. Required. Python type: ``int``; wire name: ``size``; JSON type: integer (int64). Constraints: minimum 0"""
    status: Literal['uploading', 'processing', 'available', 'failed', 'deleted'] = field(init=False)
    """Current lifecycle status of the upload receipt. Required. Python type: ``Literal['uploading', 'processing', 'available', 'failed', 'deleted']``; wire name: ``status``; JSON type: string. Constraints: allowed values ``uploading``, ``processing``, ``available``, ``failed``, ``deleted``"""
