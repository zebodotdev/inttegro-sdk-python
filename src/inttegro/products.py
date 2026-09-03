"""Typed request objects for product operations."""

from .request_types import (
    AddProductPriceRequest as AddPriceRequest,
    CreateProductRequest as CreateRequest,
    ProductAttributeInput as Attribute,
    ProductDimensionsInput as Dimensions,
    ProductDimensionsInputCustom as CustomDimensions,
    ProductDimensionsInputDigital as DigitalDimensions,
    ProductDimensionsInputPhysical as PhysicalDimensions,
    ProductMediaInput as Media,
    ProductShipmentInput as Shipment,
    PageProductsRequest as PageRequest,
    UpdateProductRequest as UpdateRequest,
)
from .money import AmountParams

__all__ = [
    "AddPriceRequest",
    "Attribute",
    "CreateRequest",
    "CustomDimensions",
    "DigitalDimensions",
    "Dimensions",
    "Media",
    "PageRequest",
    "PhysicalDimensions",
    "AmountParams",
    "Shipment",
    "UpdateRequest",
]
