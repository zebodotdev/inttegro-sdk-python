"""Typed request objects for one-time-password operations."""

from .request_types import (
    InitiateOTPRequest as InitiateRequest,
    LookupOTPRequest as LookupRequest,
    VerifyOTPRequest as VerifyRequest,
)

__all__ = ["InitiateRequest", "LookupRequest", "VerifyRequest"]
