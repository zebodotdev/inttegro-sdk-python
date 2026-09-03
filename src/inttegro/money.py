"""Currency and amount primitives for the Inttegro API."""

from dataclasses import dataclass, field

from ._model_base import ApiModel
from ._request_base import ApiRequest
from .enums import WireEnum


class Currency(WireEnum):
    """Currency identifiers with lowercase API wire values."""

    GHS = "ghs"
    USD = "usd"
    GBP = "gbp"
    EUR = "eur"
    CNY = "cny"


@dataclass(frozen=True, slots=True, kw_only=True)
class AmountParams(ApiRequest):
    """An amount supplied in a request, in the currency's smallest unit."""

    currency: Currency
    value: int


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Amount(ApiModel):
    """An amount returned by the API, in the currency's smallest unit."""

    currency: Currency = field(init=False)
    value: int = field(init=False)


__all__ = ["Amount", "AmountParams", "Currency"]
