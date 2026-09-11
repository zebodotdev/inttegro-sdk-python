"""Request parameters for inline price values."""

from dataclasses import dataclass

from inttegro.money import AmountParams


@dataclass(frozen=True, slots=True, kw_only=True)
class InlineParams(AmountParams):
    """A currency amount supplied inline in another request.

    Use this type where an operation accepts price data directly rather than a
    ``price_id`` referencing :class:`inttegro.price.Price`. ``value`` is an
    integer minor-unit amount, such as ``5000`` for GHS 50.00.
    """
