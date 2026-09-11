"""Page in the ``inttegro.message_template`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Page(ApiModel):
    """One page of page resources.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``MessageTemplatesPage``.
    """
    number: int = field(init=False)
    """Human-readable number assigned to the page. Required. Python type: ``int``; wire name: ``number``; JSON type: integer"""
    size: int = field(init=False)
    """Number of templates returned in this page after filters are applied. Required. Python type: ``int``; wire name: ``size``; JSON type: integer"""
    message_templates: list[MessageTemplate] = field(init=False)
    """The message templates associated with this page. Required. Python type: ``list[MessageTemplate]``; wire name: ``message_templates``; JSON type: array of object (MessageTemplate) values"""

from inttegro.message_template.message_template import MessageTemplate
