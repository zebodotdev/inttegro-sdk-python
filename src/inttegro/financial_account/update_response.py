"""UpdateResponse in the ``inttegro.financial_account`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class UpdateResponse(ApiModel):
    """Typed response returned by the update operation.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``UpdateFinancialAccountResponse``.
    """
    account: FinancialAccountUpdateResponse | None = field(init=False)
    """The account associated with this update response. Optional; nullable. Python type: ``FinancialAccountUpdateResponse | None``; wire name: ``account``; JSON type: object"""

from inttegro.financial_account.updated import Updated as FinancialAccountUpdateResponse
