"""Typed request objects for customer operations."""

from .request_types import (
    CreateCustomerRequest as CreateRequest,
    CustomerAddressInput as Address,
    PageCustomersRequest as PageRequest,
    UpdateCustomerRequest as UpdateRequest,
)

__all__ = ["Address", "CreateRequest", "PageRequest", "UpdateRequest"]
