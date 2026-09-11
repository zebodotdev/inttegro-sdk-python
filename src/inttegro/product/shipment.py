"""Shipment in the ``inttegro.product`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Shipment(ApiModel):
    """Typed shipment data in the product resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``ProductShipment``.
    """
    type: Literal['delivery', 'download', 'render', 'service', 'stream'] = field(init=False)
    """Discriminator identifying the shipment type. Required. Python type: ``Literal['delivery', 'download', 'render', 'service', 'stream']``; wire name: ``type``; JSON type: string. Constraints: allowed values ``delivery``, ``download``, ``render``, ``service``, ``stream``"""
    delivery: ProductDelivery | None = field(init=False)
    """Delivery fulfillment marker. Optional; nullable. Python type: ``ProductDelivery | None``; wire name: ``delivery``; JSON type: object (ProductDelivery)"""
    download: ProductDownload | None = field(init=False)
    """Download fulfillment marker. Optional; nullable. Python type: ``ProductDownload | None``; wire name: ``download``; JSON type: object (ProductDownload)"""
    render: ProductRender | None = field(init=False)
    """Rendered fulfillment marker. Optional; nullable. Python type: ``ProductRender | None``; wire name: ``render``; JSON type: object (ProductRender)"""
    service: ProductService | None = field(init=False)
    """Service fulfillment marker. Optional; nullable. Python type: ``ProductService | None``; wire name: ``service``; JSON type: object (ProductService)"""
    stream: ProductStream | None = field(init=False)
    """Streaming fulfillment marker. Optional; nullable. Python type: ``ProductStream | None``; wire name: ``stream``; JSON type: object (ProductStream)"""

from inttegro.product.delivery import Delivery as ProductDelivery
from inttegro.product.download import Download as ProductDownload
from inttegro.product.render import Render as ProductRender
from inttegro.product.service import Service as ProductService
from inttegro.product.stream import Stream as ProductStream
