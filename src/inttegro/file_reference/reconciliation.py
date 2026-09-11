"""Reconciliation in the ``inttegro.file_reference`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Reconciliation(ApiModel):
    """Typed reconciliation data in the file reference resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``FileReferenceReconciliation``.
    """
    reconciled: Literal[True] = field(init=False)
    """The reconciled associated with this reconciliation. Required. Python type: ``Literal[True]``; wire name: ``reconciled``; JSON type: boolean. Constraints: allowed values ``True``"""
