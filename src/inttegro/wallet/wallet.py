"""Wallet in the ``inttegro.wallet`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Wallet(ApiModel):
    """Typed wallet data in the wallet resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``FinancialAccountWallet``.
    """
    id: str = field(init=False)
    """Unique identifier for this wallet. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    type: Literal['mobile_money'] = field(init=False)
    """Discriminator identifying the wallet type. Required. Python type: ``Literal['mobile_money']``; wire name: ``type``; JSON type: string. Constraints: allowed values ``mobile_money``"""
    mobile_money: FinancialAccountWalletMobileMoney | None = field(init=False)
    """The mobile money associated with this wallet. Optional; nullable. Python type: ``FinancialAccountWalletMobileMoney | None``; wire name: ``mobile_money``; JSON type: object"""

from inttegro.wallet.mobile_money import MobileMoney as FinancialAccountWalletMobileMoney
