"""DetailsInput in the ``inttegro.product`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from typing import TypeAlias
from inttegro.product.catalog_with_price_data_input import CatalogWithPriceDataInput as CatalogProductWithPriceDataInput
from inttegro.product.catalog_with_price_reference_input import CatalogWithPriceReferenceInput as CatalogProductWithPriceReferenceInput
from inttegro.product.inline_details_input import InlineDetailsInput as InlineProductDetailsInput


DetailsInput: TypeAlias = InlineProductDetailsInput | CatalogProductWithPriceDataInput | CatalogProductWithPriceReferenceInput
"""Product details for an order line item. Provide inline product data, a catalog ``product_id`` with an explicit inline price, or a catalog ``product_id`` with a ``price_id`` reference."""
