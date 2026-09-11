"""ScannedLink in the ``inttegro.message_template`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ScannedLink(ApiModel):
    """Typed scanned link data in the message template resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``MessageTemplateScannedLink``.
    """
    host: str | None = field(init=False)
    """The host associated with this scanned link. Optional; nullable. Python type: ``str | None``; wire name: ``host``; JSON type: string"""
    raw: str = field(init=False)
    """The raw associated with this scanned link. Required. Python type: ``str``; wire name: ``raw``; JSON type: string"""
    reason: str | None = field(init=False)
    """The reason associated with this scanned link. Optional; nullable. Python type: ``str | None``; wire name: ``reason``; JSON type: string"""
    scheme: str = field(init=False)
    """The scheme associated with this scanned link. Required. Python type: ``str``; wire name: ``scheme``; JSON type: string"""
    status: str = field(init=False)
    """Current lifecycle status of the scanned link. Required. Python type: ``str``; wire name: ``status``; JSON type: string"""
