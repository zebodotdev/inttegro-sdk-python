"""SavedCustomerRecipientInput in the ``inttegro.chime`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Literal
from inttegro._request_base import ApiRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class SavedCustomerRecipientInput(ApiRequest):
    """Parameters accepted by the saved customer recipient input operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``ChimeSavedCustomerRecipientInput``.
    """
    customer_id: str
    """Identifier of the related customer. Required. Python type: ``str``; wire name: ``customer_id``; JSON type: string"""
    transport: Literal['sms', 'email', ChimeTransport.SMS, ChimeTransport.EMAIL]
    """The transport associated with this saved customer recipient input. Required. Python type: ``Literal['sms', 'email', ChimeTransport.SMS, ChimeTransport.EMAIL]``; wire name: ``transport``; JSON type: string. Constraints: allowed values ``sms``, ``email``"""

from inttegro.chime.transport import Transport as ChimeTransport
