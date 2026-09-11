"""Models, requests, and enums for the Inttegro wallet resource.

The primary returned object is ``inttegro.wallet.Wallet``. Related request types, nested response shapes, and string-backed enums are exported from this singular namespace. Public members load lazily, so importing one resource does not eagerly import the entire SDK."""

from importlib import import_module
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .mobile_money import MobileMoney as MobileMoney
    from .mobile_money_params import MobileMoneyParams as MobileMoneyParams
    from .params import Params as Params
    from .type import Type as Type
    from .updated_mobile_money import UpdatedMobileMoney as UpdatedMobileMoney
    from .updated_wallet import UpdatedWallet as UpdatedWallet
    from .wallet import Wallet as Wallet


_EXPORTS: dict[str, tuple[str, str]] = {
    "MobileMoney": ("inttegro.wallet.mobile_money", "MobileMoney"),
    "MobileMoneyParams": ("inttegro.wallet.mobile_money_params", "MobileMoneyParams"),
    "Params": ("inttegro.wallet.params", "Params"),
    "Type": ("inttegro.wallet.type", "Type"),
    "UpdatedMobileMoney": ("inttegro.wallet.updated_mobile_money", "UpdatedMobileMoney"),
    "UpdatedWallet": ("inttegro.wallet.updated_wallet", "UpdatedWallet"),
    "Wallet": ("inttegro.wallet.wallet", "Wallet"),
}

__all__ = [
    "MobileMoney",
    "MobileMoneyParams",
    "Params",
    "Type",
    "UpdatedMobileMoney",
    "UpdatedWallet",
    "Wallet",
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
