"""RecipientInput in the ``inttegro.chime`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from typing import TypeAlias
from inttegro.chime.inline_recipient_input import InlineRecipientInput as ChimeInlineRecipientInput
from inttegro.chime.saved_customer_recipient_input import SavedCustomerRecipientInput as ChimeSavedCustomerRecipientInput


RecipientInput: TypeAlias = ChimeInlineRecipientInput | ChimeSavedCustomerRecipientInput
"""A Chime recipient supplied inline by phone or email, or referenced by an existing ``customer_id`` together with the desired transport."""
