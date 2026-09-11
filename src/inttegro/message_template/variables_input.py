"""VariablesInput in the ``inttegro.message_template`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from typing import Any, TypeAlias


VariablesInput: TypeAlias = dict[str, Any]
"""Template-variable values keyed by declared variable name. Values must match the corresponding variable definition and are serialized as JSON-compatible data."""
