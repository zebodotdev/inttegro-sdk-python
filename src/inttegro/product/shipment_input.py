"""ShipmentInput in the ``inttegro.product`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Literal
from inttegro._request_base import ApiRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class ShipmentInput(ApiRequest):
    """Parameters accepted by the shipment input operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``ProductShipmentInput``.
    """
    type: Literal['delivery', 'download', 'render', 'stream', ProductShipmentInputType.DELIVERY, ProductShipmentInputType.DOWNLOAD, ProductShipmentInputType.RENDER, ProductShipmentInputType.STREAM]
    """Discriminator identifying the shipment input type. Required. Python type: ``Literal['delivery', 'download', 'render', 'stream', ProductShipmentInputType.DELIVERY, ProductShipmentInputType.DOWNLOAD, ProductShipmentInputType.RENDER, ProductShipmentInputType.STREAM]``; wire name: ``type``; JSON type: string. Constraints: allowed values ``delivery``, ``download``, ``render``, ``stream``"""

from inttegro.product.shipment_input_type import ShipmentInputType as ProductShipmentInputType
