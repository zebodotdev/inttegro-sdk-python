"""Inline price values embedded in other Inttegro resources."""

from dataclasses import dataclass

from inttegro.money import Amount


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Inline(Amount):
    """A currency amount embedded directly in another API resource.

    This response type has the same ``currency`` and integer minor-unit
    ``value`` semantics as :class:`inttegro.money.Amount`. It is named
    ``Inline`` to distinguish embedded money from the catalog
    :class:`inttegro.price.Price` resource.
    """
