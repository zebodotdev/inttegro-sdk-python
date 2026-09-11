"""Models, requests, and enums for the Inttegro bank account resource.

The primary returned object is ``inttegro.bank_account.BankAccount``. Related request types, nested response shapes, and string-backed enums are exported from this singular namespace. Public members load lazily, so importing one resource does not eagerly import the entire SDK."""

from importlib import import_module
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .bank_account import BankAccount as BankAccount
    from .created_bank_account import CreatedBankAccount as CreatedBankAccount
    from .created_ghana_bank_account import CreatedGhanaBankAccount as CreatedGhanaBankAccount
    from .created_owner import CreatedOwner as CreatedOwner
    from .created_owner_address import CreatedOwnerAddress as CreatedOwnerAddress
    from .ghana_bank_account import GhanaBankAccount as GhanaBankAccount
    from .ghana_bank_account_params import GhanaBankAccountParams as GhanaBankAccountParams
    from .owner import Owner as Owner
    from .owner_address import OwnerAddress as OwnerAddress
    from .owner_address_params import OwnerAddressParams as OwnerAddressParams
    from .owner_address_update_params import OwnerAddressUpdateParams as OwnerAddressUpdateParams
    from .owner_params import OwnerParams as OwnerParams
    from .owner_update_params import OwnerUpdateParams as OwnerUpdateParams
    from .params import Params as Params
    from .type import Type as Type
    from .updated_bank_account import UpdatedBankAccount as UpdatedBankAccount
    from .updated_ghana_bank_account import UpdatedGhanaBankAccount as UpdatedGhanaBankAccount
    from .updated_owner import UpdatedOwner as UpdatedOwner
    from .updated_owner_address import UpdatedOwnerAddress as UpdatedOwnerAddress


_EXPORTS: dict[str, tuple[str, str]] = {
    "BankAccount": ("inttegro.bank_account.bank_account", "BankAccount"),
    "CreatedBankAccount": ("inttegro.bank_account.created_bank_account", "CreatedBankAccount"),
    "CreatedGhanaBankAccount": ("inttegro.bank_account.created_ghana_bank_account", "CreatedGhanaBankAccount"),
    "CreatedOwner": ("inttegro.bank_account.created_owner", "CreatedOwner"),
    "CreatedOwnerAddress": ("inttegro.bank_account.created_owner_address", "CreatedOwnerAddress"),
    "GhanaBankAccount": ("inttegro.bank_account.ghana_bank_account", "GhanaBankAccount"),
    "GhanaBankAccountParams": ("inttegro.bank_account.ghana_bank_account_params", "GhanaBankAccountParams"),
    "Owner": ("inttegro.bank_account.owner", "Owner"),
    "OwnerAddress": ("inttegro.bank_account.owner_address", "OwnerAddress"),
    "OwnerAddressParams": ("inttegro.bank_account.owner_address_params", "OwnerAddressParams"),
    "OwnerAddressUpdateParams": ("inttegro.bank_account.owner_address_update_params", "OwnerAddressUpdateParams"),
    "OwnerParams": ("inttegro.bank_account.owner_params", "OwnerParams"),
    "OwnerUpdateParams": ("inttegro.bank_account.owner_update_params", "OwnerUpdateParams"),
    "Params": ("inttegro.bank_account.params", "Params"),
    "Type": ("inttegro.bank_account.type", "Type"),
    "UpdatedBankAccount": ("inttegro.bank_account.updated_bank_account", "UpdatedBankAccount"),
    "UpdatedGhanaBankAccount": ("inttegro.bank_account.updated_ghana_bank_account", "UpdatedGhanaBankAccount"),
    "UpdatedOwner": ("inttegro.bank_account.updated_owner", "UpdatedOwner"),
    "UpdatedOwnerAddress": ("inttegro.bank_account.updated_owner_address", "UpdatedOwnerAddress"),
}

__all__ = [
    "BankAccount",
    "CreatedBankAccount",
    "CreatedGhanaBankAccount",
    "CreatedOwner",
    "CreatedOwnerAddress",
    "GhanaBankAccount",
    "GhanaBankAccountParams",
    "Owner",
    "OwnerAddress",
    "OwnerAddressParams",
    "OwnerAddressUpdateParams",
    "OwnerParams",
    "OwnerUpdateParams",
    "Params",
    "Type",
    "UpdatedBankAccount",
    "UpdatedGhanaBankAccount",
    "UpdatedOwner",
    "UpdatedOwnerAddress",
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
