from __future__ import annotations

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    from ._error_report_types import ErrorReport


JSONValue: TypeAlias = str | int | float | bool | None | list["JSONValue"] | dict[str, "JSONValue"]


class InttegroError(Exception):
    """Base error for the Inttegro SDK."""

    report: "ErrorReport | None"

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.report = None


class NetworkError(InttegroError):
    """Raised for network connectivity errors."""

    original: Exception | None

    def __init__(self, message: str, original: Exception | None = None) -> None:
        super().__init__(message)
        self.original = original


class TimeoutError(NetworkError):
    """Raised when a request times out."""


class APIError(InttegroError):
    """Raised for API errors (HTTP >= 400)."""

    status: int
    code: str | None
    type: str | None
    url: str | None
    detail: str | None
    fix_code: str | None
    cause: str | None
    body: str | None
    data: JSONValue
    request_id: str | None

    def __init__(
        self,
        message: str,
        status: int,
        code: str | None = None,
        error_type: str | None = None,
        url: str | None = None,
        detail: str | None = None,
        fix_code: str | None = None,
        cause: str | None = None,
        body: str | None = None,
        data: JSONValue = None,
        request_id: str | None = None,
    ) -> None:
        super().__init__(message)
        self.status = status
        self.code = code
        self.type = error_type
        self.url = url
        self.detail = detail
        self.fix_code = fix_code
        self.cause = cause
        self.body = body
        self.data = data
        self.request_id = request_id


class AuthenticationError(APIError):
    """Raised on 401 responses."""


class RateLimitError(APIError):
    """Raised on 429 responses."""

    retry_after: int | None

    def __init__(
        self,
        message: str,
        status: int,
        code: str | None = None,
        error_type: str | None = None,
        url: str | None = None,
        detail: str | None = None,
        fix_code: str | None = None,
        cause: str | None = None,
        body: str | None = None,
        data: JSONValue = None,
        retry_after: int | None = None,
        request_id: str | None = None,
    ) -> None:
        super().__init__(
            message,
            status=status,
            code=code,
            error_type=error_type,
            url=url,
            detail=detail,
            fix_code=fix_code,
            cause=cause,
            body=body,
            data=data,
            request_id=request_id,
        )
        self.retry_after = retry_after
