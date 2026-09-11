"""Envelope in the ``inttegro.message_template`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Envelope(ApiModel):
    """Typed envelope data in the message template resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``MessageTemplateEnvelope``.
    """
    message_template: MessageTemplate = field(init=False)
    """The message template associated with this envelope. Required. Python type: ``MessageTemplate``; wire name: ``message_template``; JSON type: object (MessageTemplate)"""

from inttegro.message_template.message_template import MessageTemplate
