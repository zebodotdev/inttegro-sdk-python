"""VerificationSession in the ``inttegro.payment_method`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class VerificationSession(ApiModel):
    """Public file link metadata. Token hashes and provider URLs are not exposed.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PaymentMethodVerificationSession``.
    """
    payment_method_id: str = field(init=False)
    """Identifier of the related payment method. Optional. Python type: ``str``; wire name: ``payment_method_id``; JSON type: string"""
    status: str = field(init=False)
    """Current lifecycle status of the verification session. Required. Python type: ``str``; wire name: ``status``; JSON type: string. Constraints: allowed values ``active``, ``revoked``, ``expired``, ``disabled``"""
    token_sent_at: datetime | None = field(init=False)
    """Timestamp for token sent at. Optional; nullable. Python type: ``datetime | None``; wire name: ``token_sent_at``; JSON type: string (date-time)"""
    expires_at: datetime | None = field(init=False)
    """Timestamp for expires at. Required; nullable. Python type: ``datetime | None``; wire name: ``expires_at``; JSON type: string (date-time)"""
    delivery: PaymentMethodVerificationDelivery | None = field(init=False)
    """The delivery associated with this verification session. Required; nullable. Python type: ``PaymentMethodVerificationDelivery | None``; wire name: ``delivery``; JSON type: object (FileLinkDelivery)"""

from inttegro.payment_method.verification_delivery import VerificationDelivery as PaymentMethodVerificationDelivery
