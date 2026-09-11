"""LineItemInput in the ``inttegro.shared`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from typing import TypeAlias
from inttegro.shared.fee_line_item_input import FeeLineItemInput
from inttegro.product.line_item_input import LineItemInput as ProductLineItemInput
from inttegro.shared.shipping_line_item_input import ShippingLineItemInput


LineItemInput: TypeAlias = ProductLineItemInput | FeeLineItemInput | ShippingLineItemInput
"""A line item supplied when creating or updating an order. The required ``type`` discriminator selects product, fee, or shipping input and its corresponding detail object."""
