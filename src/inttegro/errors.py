class InttegroError(Exception):
    """Base error for the Inttegro SDK."""


class NetworkError(InttegroError):
    """Raised for network connectivity errors."""

    def __init__(self, message: str, original: Exception | None = None):
        super().__init__(message)
        self.original = original


class TimeoutError(NetworkError):
    """Raised when a request times out."""


class APIError(InttegroError):
    """Raised for API errors (HTTP >= 400)."""

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
        body=None,
        data=None,
    ):
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


class AuthenticationError(APIError):
    """Raised on 401 responses."""


class RateLimitError(APIError):
    """Raised on 429 responses."""

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
        body=None,
        data=None,
        retry_after: int | None = None,
    ):
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
        )
        self.retry_after = retry_after
