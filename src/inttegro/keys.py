"""Typed request objects for secret-key operations."""

from ._enums import SecretKeyAuthResult, SecretKeyStatus, SecretKeyTokenType
from .request_types import (
    GenerateSecretKeyRequest as GenerateRequest,
    PageSecretKeysRequest as PageRequest,
    SecretKeyUsageRequest as UsageRequest,
    UpdateSecretKeyRequest as UpdateRequest,
)

__all__ = [
    "GenerateRequest",
    "PageRequest",
    "SecretKeyAuthResult",
    "SecretKeyStatus",
    "SecretKeyTokenType",
    "UpdateRequest",
    "UsageRequest",
]
