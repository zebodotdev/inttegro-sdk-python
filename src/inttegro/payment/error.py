"""Error in the ``inttegro.payment`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Error(ApiModel):
    """Typed error data in the payment resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PaymentError``.
    """
    message: str = field(init=False)
    """The message associated with this error. Required. Python type: ``str``; wire name: ``message``; JSON type: string"""
    docs_url: str = field(init=False)
    """URL used for docs. Required. Python type: ``str``; wire name: ``docs_url``; JSON type: string (uri)"""
    source: str = field(init=False)
    """The source associated with this error. Required. Python type: ``str``; wire name: ``source``; JSON type: string"""
    type: str = field(init=False)
    """Discriminator identifying the error type. Required. Python type: ``str``; wire name: ``type``; JSON type: string"""
    code: str = field(init=False)
    """The code associated with this error. Required. Python type: ``str``; wire name: ``code``; JSON type: string"""
