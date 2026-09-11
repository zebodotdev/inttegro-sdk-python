"""SettingsLookupSchedule in the ``inttegro.payout`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class SettingsLookupSchedule(ApiModel):
    """Active payout schedule.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PayoutSettingsLookupSchedule``.
    """
    aging_spec: PayoutSettingsLookupScheduleAgingSpec = field(init=False)
    """The aging spec associated with this settings lookup schedule. Required. Python type: ``PayoutSettingsLookupScheduleAgingSpec``; wire name: ``aging_spec``; JSON type: object"""
    description: str = field(init=False)
    """Human-readable description of the settings lookup schedule. Required. Python type: ``str``; wire name: ``description``; JSON type: string"""
    interval: str = field(init=False)
    """The interval associated with this settings lookup schedule. Required. Python type: ``str``; wire name: ``interval``; JSON type: string"""
    name: str = field(init=False)
    """Human-readable name of the settings lookup schedule. Required. Python type: ``str``; wire name: ``name``; JSON type: string"""
    schedule_on: str = field(init=False)
    """The schedule on associated with this settings lookup schedule. Required. Python type: ``str``; wire name: ``schedule_on``; JSON type: string"""
    type: str = field(init=False)
    """Discriminator identifying the settings lookup schedule type. Required. Python type: ``str``; wire name: ``type``; JSON type: string"""

from inttegro.payout.settings_lookup_schedule_aging_spec import SettingsLookupScheduleAgingSpec as PayoutSettingsLookupScheduleAgingSpec
