"""Inline price primitives for request and response bodies."""

from dataclasses import dataclass

from .money import Amount, AmountParams


@dataclass(frozen=True, slots=True, kw_only=True)
class PriceParams(AmountParams):
    """An inline price supplied in a request."""


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Price(Amount):
    """An inline price returned by the API."""


__all__ = ["Price", "PriceParams"]
