"""Models, requests, and enums for the Inttegro payment resource.

The primary returned object is ``inttegro.payment.Payment``. Related request types, nested response shapes, and string-backed enums are exported from this singular namespace. Public members load lazily, so importing one resource does not eagerly import the entire SDK."""

from importlib import import_module
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .attempt import Attempt as Attempt
    from .attempt_error import AttemptError as AttemptError
    from .attempt_status import AttemptStatus as AttemptStatus
    from .billing_details import BillingDetails as BillingDetails
    from .confirm_request import ConfirmRequest as ConfirmRequest
    from .confirmation_channel import ConfirmationChannel as ConfirmationChannel
    from .error import Error as Error
    from .next_action import NextAction as NextAction
    from .next_action_authorize import NextActionAuthorize as NextActionAuthorize
    from .next_action_confirm_payment import NextActionConfirmPayment as NextActionConfirmPayment
    from .next_action_confirm_payment_attempt import NextActionConfirmPaymentAttempt as NextActionConfirmPaymentAttempt
    from .next_action_confirm_payment_request import NextActionConfirmPaymentRequest as NextActionConfirmPaymentRequest
    from .next_action_redirect import NextActionRedirect as NextActionRedirect
    from .next_action_redirect_latest_visit import NextActionRedirectLatestVisit as NextActionRedirectLatestVisit
    from .next_action_request_confirmation import NextActionRequestConfirmation as NextActionRequestConfirmation
    from .next_action_type import NextActionType as NextActionType
    from .payment import Payment as Payment
    from .payment_method import PaymentMethod as PaymentMethod
    from .payment_method_bank_account import PaymentMethodBankAccount as PaymentMethodBankAccount
    from .payment_method_ghana_bank_account import PaymentMethodGhanaBankAccount as PaymentMethodGhanaBankAccount
    from .payment_method_mobile_money import PaymentMethodMobileMoney as PaymentMethodMobileMoney
    from .payment_method_owner import PaymentMethodOwner as PaymentMethodOwner
    from .payout_configuration import PayoutConfiguration as PayoutConfiguration
    from .payout_configuration_destination import PayoutConfigurationDestination as PayoutConfigurationDestination
    from .result_status import ResultStatus as ResultStatus
    from .status import Status as Status


_EXPORTS: dict[str, tuple[str, str]] = {
    "Attempt": ("inttegro.payment.attempt", "Attempt"),
    "AttemptError": ("inttegro.payment.attempt_error", "AttemptError"),
    "AttemptStatus": ("inttegro.payment.attempt_status", "AttemptStatus"),
    "BillingDetails": ("inttegro.payment.billing_details", "BillingDetails"),
    "ConfirmRequest": ("inttegro.payment.confirm_request", "ConfirmRequest"),
    "ConfirmationChannel": ("inttegro.payment.confirmation_channel", "ConfirmationChannel"),
    "Error": ("inttegro.payment.error", "Error"),
    "NextAction": ("inttegro.payment.next_action", "NextAction"),
    "NextActionAuthorize": ("inttegro.payment.next_action_authorize", "NextActionAuthorize"),
    "NextActionConfirmPayment": ("inttegro.payment.next_action_confirm_payment", "NextActionConfirmPayment"),
    "NextActionConfirmPaymentAttempt": ("inttegro.payment.next_action_confirm_payment_attempt", "NextActionConfirmPaymentAttempt"),
    "NextActionConfirmPaymentRequest": ("inttegro.payment.next_action_confirm_payment_request", "NextActionConfirmPaymentRequest"),
    "NextActionRedirect": ("inttegro.payment.next_action_redirect", "NextActionRedirect"),
    "NextActionRedirectLatestVisit": ("inttegro.payment.next_action_redirect_latest_visit", "NextActionRedirectLatestVisit"),
    "NextActionRequestConfirmation": ("inttegro.payment.next_action_request_confirmation", "NextActionRequestConfirmation"),
    "NextActionType": ("inttegro.payment.next_action_type", "NextActionType"),
    "Payment": ("inttegro.payment.payment", "Payment"),
    "PaymentMethod": ("inttegro.payment.payment_method", "PaymentMethod"),
    "PaymentMethodBankAccount": ("inttegro.payment.payment_method_bank_account", "PaymentMethodBankAccount"),
    "PaymentMethodGhanaBankAccount": ("inttegro.payment.payment_method_ghana_bank_account", "PaymentMethodGhanaBankAccount"),
    "PaymentMethodMobileMoney": ("inttegro.payment.payment_method_mobile_money", "PaymentMethodMobileMoney"),
    "PaymentMethodOwner": ("inttegro.payment.payment_method_owner", "PaymentMethodOwner"),
    "PayoutConfiguration": ("inttegro.payment.payout_configuration", "PayoutConfiguration"),
    "PayoutConfigurationDestination": ("inttegro.payment.payout_configuration_destination", "PayoutConfigurationDestination"),
    "ResultStatus": ("inttegro.payment.result_status", "ResultStatus"),
    "Status": ("inttegro.payment.status", "Status"),
}

__all__ = [
    "Attempt",
    "AttemptError",
    "AttemptStatus",
    "BillingDetails",
    "ConfirmRequest",
    "ConfirmationChannel",
    "Error",
    "NextAction",
    "NextActionAuthorize",
    "NextActionConfirmPayment",
    "NextActionConfirmPaymentAttempt",
    "NextActionConfirmPaymentRequest",
    "NextActionRedirect",
    "NextActionRedirectLatestVisit",
    "NextActionRequestConfirmation",
    "NextActionType",
    "Payment",
    "PaymentMethod",
    "PaymentMethodBankAccount",
    "PaymentMethodGhanaBankAccount",
    "PaymentMethodMobileMoney",
    "PaymentMethodOwner",
    "PayoutConfiguration",
    "PayoutConfigurationDestination",
    "ResultStatus",
    "Status",
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
