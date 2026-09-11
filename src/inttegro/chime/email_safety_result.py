"""EmailSafetyResult in the ``inttegro.chime`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class EmailSafetyResult(ApiModel):
    """Result of the email safety scan.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``ChimeEmailSafetyResult``.
    """
    status: Literal['allowed', 'rejected', 'quarantined'] | None = field(init=False)
    """Safety decision for the email content. Optional; nullable. Python type: ``Literal['allowed', 'rejected', 'quarantined'] | None``; wire name: ``status``; JSON type: string. Constraints: allowed values ``allowed``, ``rejected``, ``quarantined``"""
    reason_codes: list[str] | None = field(init=False)
    """Machine-readable reasons for non-allowed results. Optional; nullable. Python type: ``list[str] | None``; wire name: ``reason_codes``; JSON type: array of string values"""
    sanitized_html: str | None = field(init=False)
    """Sanitized HTML body used for provider send when present. Optional; nullable. Python type: ``str | None``; wire name: ``sanitized_html``; JSON type: string"""
    normalized_text: str | None = field(init=False)
    """Normalized plain-text body used by the scanner. Optional; nullable. Python type: ``str | None``; wire name: ``normalized_text``; JSON type: string"""
    links: list[ChimeEmailScannedLink] | None = field(init=False)
    """The links associated with this email safety result. Optional; nullable. Python type: ``list[ChimeEmailScannedLink] | None``; wire name: ``links``; JSON type: array of object (ChimeEmailScannedLink) values"""
    scanner: str | None = field(init=False)
    """Safety scanner identifier. Optional; nullable. Python type: ``str | None``; wire name: ``scanner``; JSON type: string"""
    content_hash: str | None = field(init=False)
    """Hash of the scanned email content. Optional; nullable. Python type: ``str | None``; wire name: ``content_hash``; JSON type: string"""
    quarantine_notes: str | None = field(init=False)
    """The quarantine notes associated with this email safety result. Optional; nullable. Python type: ``str | None``; wire name: ``quarantine_notes``; JSON type: string"""

from inttegro.chime.email_scanned_link import EmailScannedLink as ChimeEmailScannedLink
