"""Models, requests, and enums for the Inttegro upload request resource.

The primary returned object is ``inttegro.upload_request.UploadRequest``. Related request types, nested response shapes, and string-backed enums are exported from this singular namespace. Public members load lazily, so importing one resource does not eagerly import the entire SDK."""

from importlib import import_module
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .actor import Actor as Actor
    from .attempt import Attempt as Attempt
    from .attempts import Attempts as Attempts
    from .attempts_request import AttemptsRequest as AttemptsRequest
    from .cancel_request import CancelRequest as CancelRequest
    from .constraints import Constraints as Constraints
    from .constraints_input import ConstraintsInput as ConstraintsInput
    from .create_request import CreateRequest as CreateRequest
    from .display import Display as Display
    from .display_input import DisplayInput as DisplayInput
    from .latest_error import LatestError as LatestError
    from .lookup_request import LookupRequest as LookupRequest
    from .page import Page as Page
    from .page_request import PageRequest as PageRequest
    from .page_response import PageResponse as PageResponse
    from .response import Response as Response
    from .review import Review as Review
    from .review_attempt_by_id_request import ReviewAttemptByIDRequest as ReviewAttemptByIDRequest
    from .review_attempt_by_ordinal_request import ReviewAttemptByOrdinalRequest as ReviewAttemptByOrdinalRequest
    from .review_attempt_request import ReviewAttemptRequest as ReviewAttemptRequest
    from .review_decision import ReviewDecision as ReviewDecision
    from .review_reason import ReviewReason as ReviewReason
    from .review_reason_input import ReviewReasonInput as ReviewReasonInput
    from .review_type import ReviewType as ReviewType
    from .status import Status as Status
    from .upload_request import UploadRequest as UploadRequest
    from .with_attempt_object import WithAttemptObject as WithAttemptObject
    from .with_attempt_response import WithAttemptResponse as WithAttemptResponse


_EXPORTS: dict[str, tuple[str, str]] = {
    "Actor": ("inttegro.upload_request.actor", "Actor"),
    "Attempt": ("inttegro.upload_request.attempt", "Attempt"),
    "Attempts": ("inttegro.upload_request.attempts", "Attempts"),
    "AttemptsRequest": ("inttegro.upload_request.attempts_request", "AttemptsRequest"),
    "CancelRequest": ("inttegro.upload_request.cancel_request", "CancelRequest"),
    "Constraints": ("inttegro.upload_request.constraints", "Constraints"),
    "ConstraintsInput": ("inttegro.upload_request.constraints_input", "ConstraintsInput"),
    "CreateRequest": ("inttegro.upload_request.create_request", "CreateRequest"),
    "Display": ("inttegro.upload_request.display", "Display"),
    "DisplayInput": ("inttegro.upload_request.display_input", "DisplayInput"),
    "LatestError": ("inttegro.upload_request.latest_error", "LatestError"),
    "LookupRequest": ("inttegro.upload_request.lookup_request", "LookupRequest"),
    "Page": ("inttegro.upload_request.page", "Page"),
    "PageRequest": ("inttegro.upload_request.page_request", "PageRequest"),
    "PageResponse": ("inttegro.upload_request.page_response", "PageResponse"),
    "Response": ("inttegro.upload_request.response", "Response"),
    "Review": ("inttegro.upload_request.review", "Review"),
    "ReviewAttemptByIDRequest": ("inttegro.upload_request.review_attempt_by_id_request", "ReviewAttemptByIDRequest"),
    "ReviewAttemptByOrdinalRequest": ("inttegro.upload_request.review_attempt_by_ordinal_request", "ReviewAttemptByOrdinalRequest"),
    "ReviewAttemptRequest": ("inttegro.upload_request.review_attempt_request", "ReviewAttemptRequest"),
    "ReviewDecision": ("inttegro.upload_request.review_decision", "ReviewDecision"),
    "ReviewReason": ("inttegro.upload_request.review_reason", "ReviewReason"),
    "ReviewReasonInput": ("inttegro.upload_request.review_reason_input", "ReviewReasonInput"),
    "ReviewType": ("inttegro.upload_request.review_type", "ReviewType"),
    "Status": ("inttegro.upload_request.status", "Status"),
    "UploadRequest": ("inttegro.upload_request.upload_request", "UploadRequest"),
    "WithAttemptObject": ("inttegro.upload_request.with_attempt_object", "WithAttemptObject"),
    "WithAttemptResponse": ("inttegro.upload_request.with_attempt_response", "WithAttemptResponse"),
}

__all__ = [
    "Actor",
    "Attempt",
    "Attempts",
    "AttemptsRequest",
    "CancelRequest",
    "Constraints",
    "ConstraintsInput",
    "CreateRequest",
    "Display",
    "DisplayInput",
    "LatestError",
    "LookupRequest",
    "Page",
    "PageRequest",
    "PageResponse",
    "Response",
    "Review",
    "ReviewAttemptByIDRequest",
    "ReviewAttemptByOrdinalRequest",
    "ReviewAttemptRequest",
    "ReviewDecision",
    "ReviewReason",
    "ReviewReasonInput",
    "ReviewType",
    "Status",
    "UploadRequest",
    "WithAttemptObject",
    "WithAttemptResponse",
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
