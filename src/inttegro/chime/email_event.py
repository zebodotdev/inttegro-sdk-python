"""EmailEvent in the ``inttegro.chime`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class EmailEvent(ApiModel):
    """Typed email event data in the chime resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``ChimeEmailEvent``.
    """
    bounce_sub_type: str | None = field(init=False)
    """The bounce sub type associated with this email event. Optional; nullable. Python type: ``str | None``; wire name: ``bounce_sub_type``; JSON type: string"""
    bounce_type: str | None = field(init=False)
    """The bounce type associated with this email event. Optional; nullable. Python type: ``str | None``; wire name: ``bounce_type``; JSON type: string"""
    complaint_sub_type: str | None = field(init=False)
    """The complaint sub type associated with this email event. Optional; nullable. Python type: ``str | None``; wire name: ``complaint_sub_type``; JSON type: string"""
    id: str = field(init=False)
    """Unique identifier for this email event. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    occurred_at: datetime = field(init=False)
    """Timestamp for occurred at. Required. Python type: ``datetime``; wire name: ``occurred_at``; JSON type: string (date-time)"""
    provider: str = field(init=False)
    """The provider associated with this email event. Required. Python type: ``str``; wire name: ``provider``; JSON type: string"""
    provider_message_id: str = field(init=False)
    """Identifier of the related provider message. Required. Python type: ``str``; wire name: ``provider_message_id``; JSON type: string"""
    reason: str | None = field(init=False)
    """The reason associated with this email event. Optional; nullable. Python type: ``str | None``; wire name: ``reason``; JSON type: string"""
    reason_code: str | None = field(init=False)
    """The reason code associated with this email event. Optional; nullable. Python type: ``str | None``; wire name: ``reason_code``; JSON type: string"""
    recipient: str | None = field(init=False)
    """The recipient associated with this email event. Optional; nullable. Python type: ``str | None``; wire name: ``recipient``; JSON type: string"""
    source: str | None = field(init=False)
    """The source associated with this email event. Optional; nullable. Python type: ``str | None``; wire name: ``source``; JSON type: string"""
    suppress_recipient: bool | None = field(init=False)
    """Whether suppress recipient. Optional; nullable. Python type: ``bool | None``; wire name: ``suppress_recipient``; JSON type: boolean"""
    temporary: bool | None = field(init=False)
    """Whether temporary. Optional; nullable. Python type: ``bool | None``; wire name: ``temporary``; JSON type: boolean"""
    type: str = field(init=False)
    """Discriminator identifying the email event type. Required. Python type: ``str``; wire name: ``type``; JSON type: string"""
