"""VariableItemInput in the ``inttegro.message_template`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Literal
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class VariableItemInput(ApiRequest):
    """Parameters accepted by the variable item input operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``MessageTemplateVariableItemInput``.
    """
    about: str | UnsetType = field(default=UNSET)
    """The about associated with this variable item input. Optional. Python type: ``str``; wire name: ``about``; JSON type: string"""
    default: Any | UnsetType = field(default=UNSET)
    """The default associated with this variable item input. Optional. Python type: ``Any``; wire name: ``default``; JSON type: object"""
    required: bool | UnsetType = field(default=UNSET)
    """Whether required. Optional. Python type: ``bool``; wire name: ``required``; JSON type: boolean"""
    name: str
    """Human-readable name of the variable item input. Required. Python type: ``str``; wire name: ``name``; JSON type: string. Constraints: pattern ^[a-z][a-z0-9_]{0,63}$"""
    type: Literal['string', 'number', 'integer', 'boolean', 'url', 'email', 'phone', 'date', 'datetime', MessageTemplateVariableItemType.STRING, MessageTemplateVariableItemType.NUMBER, MessageTemplateVariableItemType.INTEGER, MessageTemplateVariableItemType.BOOLEAN, MessageTemplateVariableItemType.URL, MessageTemplateVariableItemType.EMAIL, MessageTemplateVariableItemType.PHONE, MessageTemplateVariableItemType.DATE, MessageTemplateVariableItemType.DATETIME]
    """Discriminator identifying the variable item input type. Required. Python type: ``Literal['string', 'number', 'integer', 'boolean', 'url', 'email', 'phone', 'date', 'datetime', MessageTemplateVariableItemType.STRING, MessageTemplateVariableItemType.NUMBER, MessageTemplateVariableItemType.INTEGER, MessageTemplateVariableItemType.BOOLEAN, MessageTemplateVariableItemType.URL, MessageTemplateVariableItemType.EMAIL, MessageTemplateVariableItemType.PHONE, MessageTemplateVariableItemType.DATE, MessageTemplateVariableItemType.DATETIME]``; wire name: ``type``; JSON type: string. Constraints: allowed values ``string``, ``number``, ``integer``, ``boolean``, ``url``, ``email``, ``phone``, ``date``, ``datetime``"""

from inttegro.message_template.variable_item_type import VariableItemType as MessageTemplateVariableItemType
