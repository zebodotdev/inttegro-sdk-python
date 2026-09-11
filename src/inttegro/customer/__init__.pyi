"""Models, requests, and enums for the Inttegro customer resource.

The primary returned object is ``inttegro.customer.Customer``. Related request types, nested response shapes, and string-backed enums are exported from this singular namespace. Public members load lazily, so importing one resource does not eagerly import the entire SDK."""

from .address import Address as Address
from .address_input import AddressInput as AddressInput
from .balance_value import BalanceValue as BalanceValue
from .create_request import CreateRequest as CreateRequest
from .customer import Customer as Customer
from .data_input import DataInput as DataInput
from .lookup_request import LookupRequest as LookupRequest
from .page import Page as Page
from .page_request import PageRequest as PageRequest
from .page_response import PageResponse as PageResponse
from .response import Response as Response
from .update_request import UpdateRequest as UpdateRequest
