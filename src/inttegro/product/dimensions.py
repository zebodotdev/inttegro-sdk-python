"""Dimensions in the ``inttegro.product`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Dimensions(ApiModel):
    """At most one of `physical`, `digital`, or `custom`.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``ProductDimensions``.
    """
    physical: ProductDimensionsPhysical | None = field(init=False)
    """The physical associated with this dimension. Optional; nullable. Python type: ``ProductDimensionsPhysical | None``; wire name: ``physical``; JSON type: object"""
    digital: ProductDimensionsDigital | None = field(init=False)
    """The digital associated with this dimension. Optional; nullable. Python type: ``ProductDimensionsDigital | None``; wire name: ``digital``; JSON type: object"""
    custom: ProductDimensionsCustom | None = field(init=False)
    """The custom associated with this dimension. Optional; nullable. Python type: ``ProductDimensionsCustom | None``; wire name: ``custom``; JSON type: object"""

from inttegro.product.dimensions_custom import DimensionsCustom as ProductDimensionsCustom
from inttegro.product.dimensions_digital import DimensionsDigital as ProductDimensionsDigital
from inttegro.product.dimensions_physical import DimensionsPhysical as ProductDimensionsPhysical
