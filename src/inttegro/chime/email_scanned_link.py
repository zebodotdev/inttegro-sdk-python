"""EmailScannedLink in the ``inttegro.chime`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class EmailScannedLink(ApiModel):
    """Typed email scanned link data in the chime resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``ChimeEmailScannedLink``.
    """
    raw: str | None = field(init=False)
    """The raw associated with this email scanned link. Optional; nullable. Python type: ``str | None``; wire name: ``raw``; JSON type: string"""
    scheme: str | None = field(init=False)
    """The scheme associated with this email scanned link. Optional; nullable. Python type: ``str | None``; wire name: ``scheme``; JSON type: string"""
    host: str | None = field(init=False)
    """The host associated with this email scanned link. Optional; nullable. Python type: ``str | None``; wire name: ``host``; JSON type: string"""
    status: Literal['allowed', 'rejected', 'quarantined'] | None = field(init=False)
    """Current lifecycle status of the email scanned link. Optional; nullable. Python type: ``Literal['allowed', 'rejected', 'quarantined'] | None``; wire name: ``status``; JSON type: string. Constraints: allowed values ``allowed``, ``rejected``, ``quarantined``"""
    reason: str | None = field(init=False)
    """The reason associated with this email scanned link. Optional; nullable. Python type: ``str | None``; wire name: ``reason``; JSON type: string"""
