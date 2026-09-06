from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Callable, Literal, cast


ErrorReportingPolicy = Literal["unexpected", "all"]


@dataclass(frozen=True)
class SDKReportContext:
    language: Literal["python"]
    version: str


@dataclass(frozen=True)
class HTTPReportContext:
    method: str
    server_address: str
    duration_ms: int
    route: str | None = None
    status_code: int | None = None
    request_id: str | None = None


@dataclass(frozen=True)
class APIErrorReportContext:
    type: str | None = None
    code: str | None = None
    fix_code: str | None = None


@dataclass(frozen=True)
class TraceReportContext:
    trace_id: str
    span_id: str


@dataclass(frozen=True)
class ErrorReport:
    """A privacy-safe description of a failed Inttegro SDK operation."""

    schema_version: Literal[1]
    event_id: str
    occurred_at: str
    severity: Literal["error"]
    category: str
    operation: str
    sdk: SDKReportContext
    http: HTTPReportContext
    exception_type: str
    fingerprint: str
    api_error: APIErrorReportContext | None = None
    trace: TraceReportContext | None = None

    def to_dict(self) -> dict[str, object]:
        """Return a JSON-serializable payload for a collector."""
        return cast(dict[str, object], asdict(self))


ErrorReporter = Callable[[ErrorReport], None]
