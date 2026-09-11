"""PageResponse in the ``inttegro.balance_transaction`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PageResponse(ApiModel):
    """Typed response returned by the page operation.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``BalanceTransactionPageResponse``.
    """
    page: BalanceTransactionPage = field(init=False)
    """Numeric page used by this operation. Required. Python type: ``BalanceTransactionPage``; wire name: ``page``; JSON type: object"""

from inttegro.balance_transaction.page import Page as BalanceTransactionPage
