"""VariableInput in the ``inttegro.message_template`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Literal
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class VariableInput(ApiRequest):
    """Parameters accepted by the variable input operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``MessageTemplateVariableInput``.
    """
    required: bool | UnsetType = field(default=UNSET)
    """Whether required. Optional. Python type: ``bool``; wire name: ``required``; JSON type: boolean"""
    default: Any | UnsetType = field(default=UNSET)
    """Default value used when this variable is omitted. Optional. Python type: ``Any``; wire name: ``default``; JSON type: object"""
    about: str | UnsetType = field(default=UNSET)
    """Optional description of the variable. Optional. Python type: ``str``; wire name: ``about``; JSON type: string"""
    items: list[MessageTemplateVariableItemInput] | UnsetType = field(default=UNSET)
    """Field schema for array item objects. Nested arrays are not supported. Optional. Python type: ``list[MessageTemplateVariableItemInput]``; wire name: ``items``; JSON type: array of object (MessageTemplateVariableItemInput) values"""
    name: str
    """Human-readable name of the variable input. Required. Python type: ``str``; wire name: ``name``; JSON type: string. Constraints: pattern ^[a-z][a-z0-9_]{0,63}$"""
    type: Literal['string', 'number', 'integer', 'boolean', 'url', 'email', 'phone', 'date', 'datetime', 'array', MessageTemplateVariableType.STRING, MessageTemplateVariableType.NUMBER, MessageTemplateVariableType.INTEGER, MessageTemplateVariableType.BOOLEAN, MessageTemplateVariableType.URL, MessageTemplateVariableType.EMAIL, MessageTemplateVariableType.PHONE, MessageTemplateVariableType.DATE, MessageTemplateVariableType.DATETIME, MessageTemplateVariableType.ARRAY]
    """Discriminator identifying the variable input type. Required. Python type: ``Literal['string', 'number', 'integer', 'boolean', 'url', 'email', 'phone', 'date', 'datetime', 'array', MessageTemplateVariableType.STRING, MessageTemplateVariableType.NUMBER, MessageTemplateVariableType.INTEGER, MessageTemplateVariableType.BOOLEAN, MessageTemplateVariableType.URL, MessageTemplateVariableType.EMAIL, MessageTemplateVariableType.PHONE, MessageTemplateVariableType.DATE, MessageTemplateVariableType.DATETIME, MessageTemplateVariableType.ARRAY]``; wire name: ``type``; JSON type: string. Constraints: allowed values ``string``, ``number``, ``integer``, ``boolean``, ``url``, ``email``, ``phone``, ``date``, ``datetime``, ``array``"""

from inttegro.message_template.variable_item_input import VariableItemInput as MessageTemplateVariableItemInput
from inttegro.message_template.variable_type import VariableType as MessageTemplateVariableType
