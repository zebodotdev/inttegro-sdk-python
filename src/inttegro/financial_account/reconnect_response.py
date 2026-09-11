"""ReconnectResponse in the ``inttegro.financial_account`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class ReconnectResponse(ApiModel):
    """Typed response returned by the reconnect operation.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``ReconnectFinancialAccountResponse``.
    """
    account: FinancialAccountCompactResponse | None = field(init=False)
    """The account associated with this reconnect response. Optional; nullable. Python type: ``FinancialAccountCompactResponse | None``; wire name: ``account``; JSON type: object"""

from inttegro.financial_account.compact_response import CompactResponse as FinancialAccountCompactResponse
