"""MobileMoney in the ``inttegro.wallet`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class MobileMoney(ApiModel):
    """Typed mobile money data in the wallet resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``FinancialAccountWalletMobileMoney``.
    """
    account_number: str = field(init=False)
    """The account number associated with this mobile money. Required. Python type: ``str``; wire name: ``account_number``; JSON type: string"""
    network: Literal['airtel', 'mtn', 'telecel', 'vodafone'] = field(init=False)
    """The network associated with this mobile money. Required. Python type: ``Literal['airtel', 'mtn', 'telecel', 'vodafone']``; wire name: ``network``; JSON type: string. Constraints: allowed values ``airtel``, ``mtn``, ``telecel``, ``vodafone``"""
