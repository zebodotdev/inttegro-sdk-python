"""SafetyResult in the ``inttegro.message_template`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class SafetyResult(ApiModel):
    """Result of the email safety scan.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``MessageTemplateSafetyResult``.
    """
    content_hash: str = field(init=False)
    """The content hash associated with this safety result. Required. Python type: ``str``; wire name: ``content_hash``; JSON type: string"""
    links: list[MessageTemplateScannedLink] | None = field(init=False)
    """The links associated with this safety result. Optional; nullable. Python type: ``list[MessageTemplateScannedLink] | None``; wire name: ``links``; JSON type: array of object (MessageTemplateScannedLink) values"""
    normalized_text: str = field(init=False)
    """The normalized text associated with this safety result. Required. Python type: ``str``; wire name: ``normalized_text``; JSON type: string"""
    quarantine_notes: str | None = field(init=False)
    """The quarantine notes associated with this safety result. Optional; nullable. Python type: ``str | None``; wire name: ``quarantine_notes``; JSON type: string"""
    reason_codes: list[str] | None = field(init=False)
    """The reason codes associated with this safety result. Optional; nullable. Python type: ``list[str] | None``; wire name: ``reason_codes``; JSON type: array of string values"""
    sanitized_html: str | None = field(init=False)
    """The sanitized html associated with this safety result. Optional; nullable. Python type: ``str | None``; wire name: ``sanitized_html``; JSON type: string"""
    scanner: str = field(init=False)
    """The scanner associated with this safety result. Required. Python type: ``str``; wire name: ``scanner``; JSON type: string"""
    status: Literal['allowed', 'rejected', 'quarantined'] = field(init=False)
    """Current lifecycle status of the safety result. Required. Python type: ``Literal['allowed', 'rejected', 'quarantined']``; wire name: ``status``; JSON type: string. Constraints: allowed values ``allowed``, ``rejected``, ``quarantined``"""

from inttegro.message_template.scanned_link import ScannedLink as MessageTemplateScannedLink
