"""CreateRequest in the ``inttegro.order`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from typing import TypeAlias
from inttegro.order.create_existing_customer_input import CreateExistingCustomerInput as CreateOrderExistingCustomerInput
from inttegro.order.create_new_customer_input import CreateNewCustomerInput as CreateOrderNewCustomerInput


CreateRequest: TypeAlias = CreateOrderNewCustomerInput | CreateOrderExistingCustomerInput
"""Parameters for creating an order. Supply ``CreateNewCustomerInput`` with ``customer_data`` for a new customer, or ``CreateExistingCustomerInput`` with ``customer_id`` for an existing customer."""
