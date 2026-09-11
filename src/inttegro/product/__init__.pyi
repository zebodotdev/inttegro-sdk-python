"""Models, requests, and enums for the Inttegro product resource.

The primary returned object is ``inttegro.product.Product``. Related request types, nested response shapes, and string-backed enums are exported from this singular namespace. Public members load lazily, so importing one resource does not eagerly import the entire SDK."""

from .action_request import ActionRequest as ActionRequest
from .add_price_request import AddPriceRequest as AddPriceRequest
from .add_price_response import AddPriceResponse as AddPriceResponse
from .attribute import Attribute as Attribute
from .attribute_input import AttributeInput as AttributeInput
from .catalog_with_price_data_input import CatalogWithPriceDataInput as CatalogWithPriceDataInput
from .catalog_with_price_reference_input import CatalogWithPriceReferenceInput as CatalogWithPriceReferenceInput
from .create_request import CreateRequest as CreateRequest
from .delivery import Delivery as Delivery
from .details_input import DetailsInput as DetailsInput
from .dimensions import Dimensions as Dimensions
from .dimensions_custom import DimensionsCustom as DimensionsCustom
from .dimensions_digital import DimensionsDigital as DimensionsDigital
from .dimensions_input import DimensionsInput as DimensionsInput
from .dimensions_input_custom import DimensionsInputCustom as DimensionsInputCustom
from .dimensions_input_digital import DimensionsInputDigital as DimensionsInputDigital
from .dimensions_input_physical import DimensionsInputPhysical as DimensionsInputPhysical
from .dimensions_physical import DimensionsPhysical as DimensionsPhysical
from .download import Download as Download
from .inline_details_input import InlineDetailsInput as InlineDetailsInput
from .line_item_input import LineItemInput as LineItemInput
from .lookup_request import LookupRequest as LookupRequest
from .media import Media as Media
from .media_input import MediaInput as MediaInput
from .page import Page as Page
from .page_request import PageRequest as PageRequest
from .page_response import PageResponse as PageResponse
from .price_summary import PriceSummary as PriceSummary
from .product import Product as Product
from .render import Render as Render
from .response import Response as Response
from .service import Service as Service
from .shipment import Shipment as Shipment
from .shipment_input import ShipmentInput as ShipmentInput
from .shipment_input_type import ShipmentInputType as ShipmentInputType
from .shipment_type import ShipmentType as ShipmentType
from .stream import Stream as Stream
from .type import Type as Type
from .update_request import UpdateRequest as UpdateRequest
from .update_response import UpdateResponse as UpdateResponse
from .updated import Updated as Updated
