"""RenderedSMS in the ``inttegro.message_template`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class RenderedSMS(ApiModel):
    """Typed rendered sms data in the message template resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``RenderedSMSMessageTemplate``.
    """
    full_message: str = field(init=False)
    """The full message associated with this rendered sm. Required. Python type: ``str``; wire name: ``full_message``; JSON type: string. Constraints: maximum length 120"""
