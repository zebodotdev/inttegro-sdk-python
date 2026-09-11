"""LineItem in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from typing import TypeAlias
from inttegro.order.discount_line_item import DiscountLineItem as OrderDiscountLineItem
from inttegro.order.fee_line_item import FeeLineItem as OrderFeeLineItem
from inttegro.order.product_line_item import ProductLineItem as OrderProductLineItem
from inttegro.order.shipping_line_item import ShippingLineItem as OrderShippingLineItem


LineItem: TypeAlias = OrderProductLineItem | OrderFeeLineItem | OrderShippingLineItem | OrderDiscountLineItem
"""A returned order line item. The ``type`` discriminator identifies product, fee, shipping, and discount snapshots with their corresponding typed detail object."""
