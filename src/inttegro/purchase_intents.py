"""Typed request objects for purchase-intent operations."""

from ._enums import PurchaseIntentActivityType, PurchaseIntentStatus
from .request_types import (
    CancelPurchaseIntentRequest as CancelRequest,
    CreatePurchaseIntentRequest as CreateRequest,
    CreatePurchaseIntentRequestPrice as Price,
    CreatePurchaseIntentRequestPriceOriginal as OriginalPrice,
    CreatePurchaseIntentRequestProduct as Product,
    CreatePurchaseIntentRequestQuantity as Quantity,
    CreatePurchaseIntentRequestUsage as Usage,
    PagePurchaseIntentsRequest as PageRequest,
    UpdatePurchaseIntentRequest as UpdateRequest,
    UpdatePurchaseIntentRequestQuantity as UpdateQuantity,
)
from .price_types import PriceParams as NominalPrice

OriginalNominalPrice = NominalPrice

__all__ = [
    "CancelRequest",
    "CreateRequest",
    "NominalPrice",
    "OriginalNominalPrice",
    "OriginalPrice",
    "PageRequest",
    "Price",
    "Product",
    "PurchaseIntentActivityType",
    "PurchaseIntentStatus",
    "Quantity",
    "UpdateQuantity",
    "UpdateRequest",
    "Usage",
]
