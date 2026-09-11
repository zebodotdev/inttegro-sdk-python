"""Delivery in the ``inttegro.file_link`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Delivery(ApiModel):
    """Typed delivery data in the file link resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``FileLinkDelivery``.
    """
    mode: Literal['redirect', 'download', 'inline'] | None = field(init=False)
    """The mode associated with this delivery. Optional; nullable. Python type: ``Literal['redirect', 'download', 'inline'] | None``; wire name: ``mode``; JSON type: string. Constraints: allowed values ``redirect``, ``download``, ``inline``"""
    filename: str | None = field(init=False)
    """The filename associated with this delivery. Optional; nullable. Python type: ``str | None``; wire name: ``filename``; JSON type: string"""
    content_type: str | None = field(init=False)
    """The content type associated with this delivery. Optional; nullable. Python type: ``str | None``; wire name: ``content_type``; JSON type: string"""
    disposition: str | None = field(init=False)
    """The disposition associated with this delivery. Optional; nullable. Python type: ``str | None``; wire name: ``disposition``; JSON type: string"""
