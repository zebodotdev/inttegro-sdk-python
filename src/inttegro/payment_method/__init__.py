"""Models, requests, and enums for the Inttegro payment method resource.

The primary returned object is ``inttegro.payment_method.PaymentMethod``. Related request types, nested response shapes, and string-backed enums are exported from this singular namespace. Public members load lazily, so importing one resource does not eagerly import the entire SDK."""

from importlib import import_module
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .activate_request import ActivateRequest as ActivateRequest
    from .activate_response import ActivateResponse as ActivateResponse
    from .archive_request import ArchiveRequest as ArchiveRequest
    from .archive_response import ArchiveResponse as ArchiveResponse
    from .bank_account import BankAccount as BankAccount
    from .bank_account_ghana_bank_account import BankAccountGhanaBankAccount as BankAccountGhanaBankAccount
    from .card import Card as Card
    from .data_input import DataInput as DataInput
    from .data_input_mobile_money import DataInputMobileMoney as DataInputMobileMoney
    from .deletion import Deletion as Deletion
    from .disactivate_request import DisactivateRequest as DisactivateRequest
    from .disactivate_response import DisactivateResponse as DisactivateResponse
    from .get_settings_request import GetSettingsRequest as GetSettingsRequest
    from .get_settings_response import GetSettingsResponse as GetSettingsResponse
    from .lookup_request import LookupRequest as LookupRequest
    from .lookup_response import LookupResponse as LookupResponse
    from .mobile_money import MobileMoney as MobileMoney
    from .mobile_money_network import MobileMoneyNetwork as MobileMoneyNetwork
    from .owner import Owner as Owner
    from .owner_address import OwnerAddress as OwnerAddress
    from .owner_input import OwnerInput as OwnerInput
    from .owner_input_address import OwnerInputAddress as OwnerInputAddress
    from .page import Page as Page
    from .page_request import PageRequest as PageRequest
    from .page_response import PageResponse as PageResponse
    from .payment_method import PaymentMethod as PaymentMethod
    from .settings import Settings as Settings
    from .supplied import Supplied as Supplied
    from .tokenize_mobile_money_request import TokenizeMobileMoneyRequest as TokenizeMobileMoneyRequest
    from .tokenize_mobile_money_request_mobile_money import TokenizeMobileMoneyRequestMobileMoney as TokenizeMobileMoneyRequestMobileMoney
    from .tokenize_response import TokenizeResponse as TokenizeResponse
    from .type import Type as Type
    from .type_setting import TypeSetting as TypeSetting
    from .unarchive_request import UnarchiveRequest as UnarchiveRequest
    from .unarchive_response import UnarchiveResponse as UnarchiveResponse
    from .update_request import UpdateRequest as UpdateRequest
    from .update_request_owner import UpdateRequestOwner as UpdateRequestOwner
    from .update_request_owner_address import UpdateRequestOwnerAddress as UpdateRequestOwnerAddress
    from .update_response import UpdateResponse as UpdateResponse
    from .verification import Verification as Verification
    from .verification_delivery import VerificationDelivery as VerificationDelivery
    from .verification_session import VerificationSession as VerificationSession


_EXPORTS: dict[str, tuple[str, str]] = {
    "ActivateRequest": ("inttegro.payment_method.activate_request", "ActivateRequest"),
    "ActivateResponse": ("inttegro.payment_method.activate_response", "ActivateResponse"),
    "ArchiveRequest": ("inttegro.payment_method.archive_request", "ArchiveRequest"),
    "ArchiveResponse": ("inttegro.payment_method.archive_response", "ArchiveResponse"),
    "BankAccount": ("inttegro.payment_method.bank_account", "BankAccount"),
    "BankAccountGhanaBankAccount": ("inttegro.payment_method.bank_account_ghana_bank_account", "BankAccountGhanaBankAccount"),
    "Card": ("inttegro.payment_method.card", "Card"),
    "DataInput": ("inttegro.payment_method.data_input", "DataInput"),
    "DataInputMobileMoney": ("inttegro.payment_method.data_input_mobile_money", "DataInputMobileMoney"),
    "Deletion": ("inttegro.payment_method.deletion", "Deletion"),
    "DisactivateRequest": ("inttegro.payment_method.disactivate_request", "DisactivateRequest"),
    "DisactivateResponse": ("inttegro.payment_method.disactivate_response", "DisactivateResponse"),
    "GetSettingsRequest": ("inttegro.payment_method.get_settings_request", "GetSettingsRequest"),
    "GetSettingsResponse": ("inttegro.payment_method.get_settings_response", "GetSettingsResponse"),
    "LookupRequest": ("inttegro.payment_method.lookup_request", "LookupRequest"),
    "LookupResponse": ("inttegro.payment_method.lookup_response", "LookupResponse"),
    "MobileMoney": ("inttegro.payment_method.mobile_money", "MobileMoney"),
    "MobileMoneyNetwork": ("inttegro.payment_method.mobile_money_network", "MobileMoneyNetwork"),
    "Owner": ("inttegro.payment_method.owner", "Owner"),
    "OwnerAddress": ("inttegro.payment_method.owner_address", "OwnerAddress"),
    "OwnerInput": ("inttegro.payment_method.owner_input", "OwnerInput"),
    "OwnerInputAddress": ("inttegro.payment_method.owner_input_address", "OwnerInputAddress"),
    "Page": ("inttegro.payment_method.page", "Page"),
    "PageRequest": ("inttegro.payment_method.page_request", "PageRequest"),
    "PageResponse": ("inttegro.payment_method.page_response", "PageResponse"),
    "PaymentMethod": ("inttegro.payment_method.payment_method", "PaymentMethod"),
    "Settings": ("inttegro.payment_method.settings", "Settings"),
    "Supplied": ("inttegro.payment_method.supplied", "Supplied"),
    "TokenizeMobileMoneyRequest": ("inttegro.payment_method.tokenize_mobile_money_request", "TokenizeMobileMoneyRequest"),
    "TokenizeMobileMoneyRequestMobileMoney": ("inttegro.payment_method.tokenize_mobile_money_request_mobile_money", "TokenizeMobileMoneyRequestMobileMoney"),
    "TokenizeResponse": ("inttegro.payment_method.tokenize_response", "TokenizeResponse"),
    "Type": ("inttegro.payment_method.type", "Type"),
    "TypeSetting": ("inttegro.payment_method.type_setting", "TypeSetting"),
    "UnarchiveRequest": ("inttegro.payment_method.unarchive_request", "UnarchiveRequest"),
    "UnarchiveResponse": ("inttegro.payment_method.unarchive_response", "UnarchiveResponse"),
    "UpdateRequest": ("inttegro.payment_method.update_request", "UpdateRequest"),
    "UpdateRequestOwner": ("inttegro.payment_method.update_request_owner", "UpdateRequestOwner"),
    "UpdateRequestOwnerAddress": ("inttegro.payment_method.update_request_owner_address", "UpdateRequestOwnerAddress"),
    "UpdateResponse": ("inttegro.payment_method.update_response", "UpdateResponse"),
    "Verification": ("inttegro.payment_method.verification", "Verification"),
    "VerificationDelivery": ("inttegro.payment_method.verification_delivery", "VerificationDelivery"),
    "VerificationSession": ("inttegro.payment_method.verification_session", "VerificationSession"),
}

__all__ = [
    "ActivateRequest",
    "ActivateResponse",
    "ArchiveRequest",
    "ArchiveResponse",
    "BankAccount",
    "BankAccountGhanaBankAccount",
    "Card",
    "DataInput",
    "DataInputMobileMoney",
    "Deletion",
    "DisactivateRequest",
    "DisactivateResponse",
    "GetSettingsRequest",
    "GetSettingsResponse",
    "LookupRequest",
    "LookupResponse",
    "MobileMoney",
    "MobileMoneyNetwork",
    "Owner",
    "OwnerAddress",
    "OwnerInput",
    "OwnerInputAddress",
    "Page",
    "PageRequest",
    "PageResponse",
    "PaymentMethod",
    "Settings",
    "Supplied",
    "TokenizeMobileMoneyRequest",
    "TokenizeMobileMoneyRequestMobileMoney",
    "TokenizeResponse",
    "Type",
    "TypeSetting",
    "UnarchiveRequest",
    "UnarchiveResponse",
    "UpdateRequest",
    "UpdateRequestOwner",
    "UpdateRequestOwnerAddress",
    "UpdateResponse",
    "Verification",
    "VerificationDelivery",
    "VerificationSession",
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
