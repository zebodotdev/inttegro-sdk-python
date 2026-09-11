"""AttachmentIDsInput in the ``inttegro.message_template`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from typing import TypeAlias


AttachmentIDsInput: TypeAlias = list[str]
"""File IDs to attach when creating or updating an email message template. Each string is an Inttegro managed-file identifier; ordering is preserved on serialization."""
