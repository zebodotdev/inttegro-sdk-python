"""Currency and amount primitives for the Inttegro API."""

from dataclasses import dataclass, field

from ._model_base import ApiModel
from ._request_base import ApiRequest
from ._enum_base import WireEnum


class Currency(WireEnum):
    """ISO-style currency identifiers accepted by Inttegro.

    Currency members are strings and serialize to lowercase API wire values.
    Input is case-insensitive, so ``Currency("GHS")`` resolves to
    :attr:`Currency.GHS`, while serialized requests always contain ``"ghs"``.
    """

    GHS = "ghs"
    """Ghanaian cedi. Wire value: ``ghs``."""
    USD = "usd"
    """United States dollar. Wire value: ``usd``."""
    GBP = "gbp"
    """British pound sterling. Wire value: ``gbp``."""
    EUR = "eur"
    """Euro. Wire value: ``eur``."""
    CNY = "cny"
    """Chinese yuan renminbi. Wire value: ``cny``."""

    @classmethod
    def _missing_(cls, value: object) -> "Currency | None":
        if isinstance(value, str):
            normalized = value.strip().lower()
            for currency in cls:
                if currency.value == normalized:
                    return currency
        return None


@dataclass(frozen=True, slots=True, kw_only=True)
class AmountParams(ApiRequest):
    """A monetary amount supplied in an API request.

    ``value`` is always an integer in the currency's minor unit. For example,
    ``AmountParams(currency=Currency.GHS, value=5000)`` represents GHS 50.00.
    ``to_dict()`` serializes this value as
    ``{"currency": "ghs", "value": 5000}``.
    """

    currency: Currency
    """Required currency. Python type: :class:`Currency`; wire name: ``currency``; JSON type: string."""
    value: int
    """Required integer minor-unit amount. Python type: ``int``; wire name: ``value``; JSON type: integer."""


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Amount(ApiModel):
    """A monetary amount returned by the API.

    ``from_dict()`` converts the lowercase wire currency to :class:`Currency`.
    ``value`` remains an integer in that currency's minor unit, which avoids
    binary floating-point rounding in financial calculations.
    """

    currency: Currency = field(init=False)
    """Required currency. Python type: :class:`Currency`; wire name: ``currency``; JSON type: string."""
    value: int = field(init=False)
    """Required integer minor-unit amount. Python type: ``int``; wire name: ``value``; JSON type: integer."""


__all__ = ["Amount", "AmountParams", "Currency"]
