"""Variant in the ``inttegro.purchase_intent`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Variant(ApiModel):
    """Typed variant data in the purchase intent resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PurchaseIntentVariant``.
    """
    active: bool = field(init=False)
    """Whether the variant is active. Required. Python type: ``bool``; wire name: ``active``; JSON type: boolean"""
    position: int | None = field(init=False)
    """The position associated with this variant. Optional; nullable. Python type: ``int | None``; wire name: ``position``; JSON type: integer"""
    price: PurchaseIntentPrice | None = field(init=False)
    """The price associated with this variant. Optional; nullable. Python type: ``PurchaseIntentPrice | None``; wire name: ``price``; JSON type: object (PurchaseIntentPrice)"""
    product: PurchaseIntentProduct | None = field(init=False)
    """The product associated with this variant. Optional; nullable. Python type: ``PurchaseIntentProduct | None``; wire name: ``product``; JSON type: object (PurchaseIntentProduct)"""
    product_id: str = field(init=False)
    """Identifier of the related product. Required. Python type: ``str``; wire name: ``product_id``; JSON type: string"""
    variant_values: dict[str, str] = field(init=False)
    """Product variant attribute selections keyed by attribute name. Required. Python type: ``dict[str, str]``; wire name: ``variant_values``; JSON type: object (VariantValues)"""

from inttegro.purchase_intent.price import Price as PurchaseIntentPrice
from inttegro.purchase_intent.product import Product as PurchaseIntentProduct
