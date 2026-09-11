"""Shared request and response shapes used by multiple Inttegro resources.

Import these cross-resource building blocks from ``inttegro.shared``. Resource-specific models, requests, and enums remain in their singular resource namespace."""

from .address_input import AddressInput as AddressInput
from .billing_details_input import BillingDetailsInput as BillingDetailsInput
from .content_safety_status import ContentSafetyStatus as ContentSafetyStatus
from .country_bank import CountryBank as CountryBank
from .country_bank_branch import CountryBankBranch as CountryBankBranch
from .country_bank_directory import CountryBankDirectory as CountryBankDirectory
from .country_specification import CountrySpecification as CountrySpecification
from .error import Error as Error
from .fee_details_input import FeeDetailsInput as FeeDetailsInput
from .fee_line_item_input import FeeLineItemInput as FeeLineItemInput
from .line_item_input import LineItemInput as LineItemInput
from .list_country_specs_request import ListCountrySpecsRequest as ListCountrySpecsRequest
from .list_country_specs_response import ListCountrySpecsResponse as ListCountrySpecsResponse
from .request_confirmation_request import RequestConfirmationRequest as RequestConfirmationRequest
from .resource_supply import ResourceSupply as ResourceSupply
from .shipping_details_input import ShippingDetailsInput as ShippingDetailsInput
from .shipping_input import ShippingInput as ShippingInput
from .shipping_line_item_input import ShippingLineItemInput as ShippingLineItemInput
from .upload_fulfillment import UploadFulfillment as UploadFulfillment
