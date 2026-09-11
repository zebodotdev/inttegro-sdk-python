"""VariableItemType in the ``inttegro.message_template`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class VariableItemType(WireEnum):
    """Typed variable item type data in the message template resource namespace.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``MessageTemplateVariableItemType``.
    """
    STRING = "string"
    """Wire value ``string`` (string)"""
    NUMBER = "number"
    """Wire value ``number`` (number)"""
    INTEGER = "integer"
    """Wire value ``integer`` (integer)"""
    BOOLEAN = "boolean"
    """Wire value ``boolean`` (boolean)"""
    URL = "url"
    """Wire value ``url`` (url)"""
    EMAIL = "email"
    """Wire value ``email`` (email)"""
    PHONE = "phone"
    """Wire value ``phone`` (phone)"""
    DATE = "date"
    """Wire value ``date`` (date)"""
    DATETIME = "datetime"
    """Wire value ``datetime`` (datetime)"""
