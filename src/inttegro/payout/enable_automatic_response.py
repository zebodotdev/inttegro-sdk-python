"""EnableAutomaticResponse in the ``inttegro.payout`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class EnableAutomaticResponse(ApiModel):
    """Typed response returned by the enable automatic operation.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``EnableAutomaticPayoutsResponse``.
    """
    settings: PayoutSettingsMutation | None = field(init=False)
    """The settings associated with this enable automatic response. Optional; nullable. Python type: ``PayoutSettingsMutation | None``; wire name: ``settings``; JSON type: object"""

from inttegro.payout.settings_mutation import SettingsMutation as PayoutSettingsMutation
