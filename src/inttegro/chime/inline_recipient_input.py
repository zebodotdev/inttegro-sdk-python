"""InlineRecipientInput in the ``inttegro.chime`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from typing import TypeAlias
from inttegro.chime.inline_recipient_input_variant1 import InlineRecipientInputVariant1 as ChimeInlineRecipientInputVariant1
from inttegro.chime.inline_recipient_input_variant2 import InlineRecipientInputVariant2 as ChimeInlineRecipientInputVariant2


InlineRecipientInput: TypeAlias = ChimeInlineRecipientInputVariant1 | ChimeInlineRecipientInputVariant2
"""An inline Chime recipient supplied as either a phone or email recipient. The required ``type`` discriminator is ``phone`` when ``phone`` details are present and ``email`` when ``email`` details are present."""
