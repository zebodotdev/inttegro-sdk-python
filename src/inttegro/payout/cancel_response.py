"""CancelResponse in the ``inttegro.payout`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class CancelResponse(ApiModel):
    """Typed response returned by the cancel operation.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``CancelPayoutResponse``.
    """
    payout: Payout | None = field(init=False)
    """The payout associated with this cancel response. Optional; nullable. Python type: ``Payout | None``; wire name: ``payout``; JSON type: object"""

from inttegro.payout.payout import Payout
