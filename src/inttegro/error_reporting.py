from __future__ import annotations

import time
import uuid
from datetime import datetime, timezone
from typing import TYPE_CHECKING

from ._error_report_types import (
    APIErrorReportContext as APIErrorReportContext,
    ErrorReport as ErrorReport,
    ErrorReporter as _ErrorReporter,
    ErrorReportingPolicy as ErrorReportingPolicy,
    HTTPReportContext as HTTPReportContext,
    SDKReportContext as SDKReportContext,
    TraceReportContext as TraceReportContext,
)
from .errors import APIError

if TYPE_CHECKING:
    from opentelemetry.trace import Span


ErrorReporter = _ErrorReporter


def should_report(error: Exception, category: str, policy: ErrorReportingPolicy) -> bool:
    if category == "canceled":
        return False
    if policy == "all":
        return True
    if isinstance(error, APIError):
        return error.status >= 500 or error.type == "unknown_error"
    return True


def create_error_report(
    *,
    error: Exception,
    category: str,
    operation: str,
    method: str,
    route: str | None,
    server_address: str,
    version: str,
    started_at: float,
    span: Span | None,
) -> ErrorReport:
    api_error = error if isinstance(error, APIError) else None
    trace_context = None
    if span is not None:
        context = span.get_span_context()
        if context.is_valid:
            trace_context = TraceReportContext(
                trace_id=f"{context.trace_id:032x}",
                span_id=f"{context.span_id:016x}",
            )
    status_code = api_error.status if api_error is not None else None
    api_context = None
    if api_error is not None and (api_error.type or api_error.code or api_error.fix_code):
        api_context = APIErrorReportContext(
            type=api_error.type,
            code=api_error.code,
            fix_code=api_error.fix_code,
        )
    return ErrorReport(
        schema_version=1,
        event_id=str(uuid.uuid4()),
        occurred_at=datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        severity="error",
        category=category,
        operation=operation,
        sdk=SDKReportContext(language="python", version=version),
        http=HTTPReportContext(
            method=method.upper(),
            route=route,
            server_address=server_address,
            status_code=status_code,
            request_id=api_error.request_id if api_error is not None else None,
            duration_ms=max(0, round((time.monotonic() - started_at) * 1000)),
        ),
        api_error=api_context,
        trace=trace_context,
        exception_type=type(error).__name__,
        fingerprint=":".join(
            (
                "inttegro",
                "python",
                operation,
                category,
                str(status_code) if status_code is not None else "none",
            )
        ),
    )
