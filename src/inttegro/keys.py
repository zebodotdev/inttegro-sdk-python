"""Typed request objects for secret-key operations."""

from .request_types import (
    GenerateSecretKeyRequest as GenerateRequest,
    PageSecretKeysRequest as PageRequest,
    SecretKeyUsageRequest as UsageRequest,
    UpdateSecretKeyRequest as UpdateRequest,
)

__all__ = ["GenerateRequest", "PageRequest", "UpdateRequest", "UsageRequest"]
