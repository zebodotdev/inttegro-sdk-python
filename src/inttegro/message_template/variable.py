"""Variable in the ``inttegro.message_template`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Variable(ApiModel):
    """Typed variable data in the message template resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``MessageTemplateVariable``.
    """
    about: str | None = field(init=False)
    """The about associated with this variable. Optional; nullable. Python type: ``str | None``; wire name: ``about``; JSON type: string"""
    default: Any | None = field(init=False)
    """The default associated with this variable. Optional; nullable. Python type: ``Any | None``; wire name: ``default``; JSON type: object"""
    items: list[MessageTemplateVariableItem] | None = field(init=False)
    """The items associated with this variable. Optional; nullable. Python type: ``list[MessageTemplateVariableItem] | None``; wire name: ``items``; JSON type: array of object (MessageTemplateVariableItem) values"""
    name: str = field(init=False)
    """Human-readable name of the variable. Required. Python type: ``str``; wire name: ``name``; JSON type: string"""
    required: bool = field(init=False)
    """Whether required. Required. Python type: ``bool``; wire name: ``required``; JSON type: boolean"""
    type: Literal['string', 'number', 'integer', 'boolean', 'url', 'email', 'phone', 'date', 'datetime', 'array'] = field(init=False)
    """Discriminator identifying the variable type. Required. Python type: ``Literal['string', 'number', 'integer', 'boolean', 'url', 'email', 'phone', 'date', 'datetime', 'array']``; wire name: ``type``; JSON type: string. Constraints: allowed values ``string``, ``number``, ``integer``, ``boolean``, ``url``, ``email``, ``phone``, ``date``, ``datetime``, ``array``"""

from inttegro.message_template.variable_item import VariableItem as MessageTemplateVariableItem
