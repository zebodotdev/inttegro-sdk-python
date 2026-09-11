"""PageItem in the ``inttegro.price`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from typing import TypeAlias
from inttegro.price.price import Price as CatalogPrice


PageItem: TypeAlias = CatalogPrice
"""One catalog :class:`inttegro.price.Price` returned in a paginated price result."""
