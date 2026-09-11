"""CreateRequestRelationshipPolicy in the ``inttegro.app`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class CreateRequestRelationshipPolicy(ApiRequest):
    """Parameters accepted by the create request relationship policy operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``CreateApplicationRequestRelationshipPolicy``.
    """
    child_standing: str | UnsetType = field(default=UNSET)
    """The child standing associated with this create request relationship policy. Optional. Python type: ``str``; wire name: ``child_standing``; JSON type: string"""
    management: Literal['parent', 'child', AppManagementRole.PARENT, AppManagementRole.CHILD] | UnsetType = field(default=UNSET)
    """The management associated with this create request relationship policy. Optional. Python type: ``Literal['parent', 'child', AppManagementRole.PARENT, AppManagementRole.CHILD]``; wire name: ``management``; JSON type: string"""
    credentials: Literal['child', 'parent', AppCredentialOwner.CHILD, AppCredentialOwner.PARENT] | UnsetType = field(default=UNSET)
    """The credentials associated with this create request relationship policy. Optional. Python type: ``Literal['child', 'parent', AppCredentialOwner.CHILD, AppCredentialOwner.PARENT]``; wire name: ``credentials``; JSON type: string"""

from inttegro.app.credential_owner import CredentialOwner as AppCredentialOwner
from inttegro.app.management_role import ManagementRole as AppManagementRole
