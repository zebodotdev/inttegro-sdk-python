"""Shared request and response shapes used by multiple Inttegro resources.

Import these cross-resource building blocks from ``inttegro.shared``. Resource-specific models, requests, and enums remain in their singular resource namespace."""

from importlib import import_module
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
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


_EXPORTS: dict[str, tuple[str, str]] = {
    "AddressInput": ("inttegro.shared.address_input", "AddressInput"),
    "BillingDetailsInput": ("inttegro.shared.billing_details_input", "BillingDetailsInput"),
    "ContentSafetyStatus": ("inttegro.shared.content_safety_status", "ContentSafetyStatus"),
    "CountryBank": ("inttegro.shared.country_bank", "CountryBank"),
    "CountryBankBranch": ("inttegro.shared.country_bank_branch", "CountryBankBranch"),
    "CountryBankDirectory": ("inttegro.shared.country_bank_directory", "CountryBankDirectory"),
    "CountrySpecification": ("inttegro.shared.country_specification", "CountrySpecification"),
    "Error": ("inttegro.shared.error", "Error"),
    "FeeDetailsInput": ("inttegro.shared.fee_details_input", "FeeDetailsInput"),
    "FeeLineItemInput": ("inttegro.shared.fee_line_item_input", "FeeLineItemInput"),
    "LineItemInput": ("inttegro.shared.line_item_input", "LineItemInput"),
    "ListCountrySpecsRequest": ("inttegro.shared.list_country_specs_request", "ListCountrySpecsRequest"),
    "ListCountrySpecsResponse": ("inttegro.shared.list_country_specs_response", "ListCountrySpecsResponse"),
    "RequestConfirmationRequest": ("inttegro.shared.request_confirmation_request", "RequestConfirmationRequest"),
    "ResourceSupply": ("inttegro.shared.resource_supply", "ResourceSupply"),
    "ShippingDetailsInput": ("inttegro.shared.shipping_details_input", "ShippingDetailsInput"),
    "ShippingInput": ("inttegro.shared.shipping_input", "ShippingInput"),
    "ShippingLineItemInput": ("inttegro.shared.shipping_line_item_input", "ShippingLineItemInput"),
    "UploadFulfillment": ("inttegro.shared.upload_fulfillment", "UploadFulfillment"),
}

__all__ = [
    "AddressInput",
    "BillingDetailsInput",
    "ContentSafetyStatus",
    "CountryBank",
    "CountryBankBranch",
    "CountryBankDirectory",
    "CountrySpecification",
    "Error",
    "FeeDetailsInput",
    "FeeLineItemInput",
    "LineItemInput",
    "ListCountrySpecsRequest",
    "ListCountrySpecsResponse",
    "RequestConfirmationRequest",
    "ResourceSupply",
    "ShippingDetailsInput",
    "ShippingInput",
    "ShippingLineItemInput",
    "UploadFulfillment",
]


def __getattr__(name: str) -> Any:
    """Load a public resource type on first access."""
    try:
        module_name, attribute_name = _EXPORTS[name]
    except KeyError:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}") from None
    value = getattr(import_module(module_name), attribute_name)
    globals()[name] = value
    return value
