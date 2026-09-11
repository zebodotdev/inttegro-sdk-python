"""SettingsMutationSchedule in the ``inttegro.payout`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class SettingsMutationSchedule(ApiModel):
    """Updated payout schedule.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PayoutSettingsMutationSchedule``.
    """
    description: str = field(init=False)
    """Human-readable description of the settings mutation schedule. Required. Python type: ``str``; wire name: ``description``; JSON type: string"""
    id: str = field(init=False)
    """Unique identifier for this settings mutation schedule. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    interval: str = field(init=False)
    """The interval associated with this settings mutation schedule. Required. Python type: ``str``; wire name: ``interval``; JSON type: string"""
    name: str = field(init=False)
    """Human-readable name of the settings mutation schedule. Required. Python type: ``str``; wire name: ``name``; JSON type: string"""
    schedule_on: str = field(init=False)
    """The schedule on associated with this settings mutation schedule. Required. Python type: ``str``; wire name: ``schedule_on``; JSON type: string"""
    spec: PayoutSettingsMutationScheduleSpec = field(init=False)
    """The spec associated with this settings mutation schedule. Required. Python type: ``PayoutSettingsMutationScheduleSpec``; wire name: ``spec``; JSON type: object"""
    type: str = field(init=False)
    """Discriminator identifying the settings mutation schedule type. Required. Python type: ``str``; wire name: ``type``; JSON type: string"""

from inttegro.payout.settings_mutation_schedule_spec import SettingsMutationScheduleSpec as PayoutSettingsMutationScheduleSpec
