"""VariantSet in the ``inttegro.purchase_intent`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class VariantSet(ApiModel):
    """Typed variant set data in the purchase intent resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PurchaseIntentVariantSet``.
    """
    active: bool = field(init=False)
    """Whether the variant set is active. Required. Python type: ``bool``; wire name: ``active``; JSON type: boolean"""
    default_product_id: str | None = field(init=False)
    """Identifier of the related default product. Optional; nullable. Python type: ``str | None``; wire name: ``default_product_id``; JSON type: string"""
    description: str | None = field(init=False)
    """Human-readable description of the variant set. Optional; nullable. Python type: ``str | None``; wire name: ``description``; JSON type: string"""
    id: str = field(init=False)
    """Unique identifier for this variant set. Required. Python type: ``str``; wire name: ``id``; JSON type: string"""
    name: str = field(init=False)
    """Human-readable name of the variant set. Required. Python type: ``str``; wire name: ``name``; JSON type: string"""
    reference: str | None = field(init=False)
    """Merchant-defined external reference for the variant set. Optional; nullable. Python type: ``str | None``; wire name: ``reference``; JSON type: string"""
    variant_axes: list[PurchaseIntentVariantAxis] = field(init=False)
    """The variant axes associated with this variant set. Required. Python type: ``list[PurchaseIntentVariantAxis]``; wire name: ``variant_axes``; JSON type: array of object (PurchaseIntentVariantAxis) values"""
    variants: list[PurchaseIntentVariant] = field(init=False)
    """The variants associated with this variant set. Required. Python type: ``list[PurchaseIntentVariant]``; wire name: ``variants``; JSON type: array of object (PurchaseIntentVariant) values"""

from inttegro.purchase_intent.variant import Variant as PurchaseIntentVariant
from inttegro.purchase_intent.variant_axis import VariantAxis as PurchaseIntentVariantAxis
