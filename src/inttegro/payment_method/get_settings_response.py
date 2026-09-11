"""GetSettingsResponse in the ``inttegro.payment_method`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class GetSettingsResponse(ApiModel):
    """Typed response returned by the get settings operation.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``GetPaymentMethodSettingsResponse``.
    """
    settings: PaymentMethodSettings = field(init=False)
    """The settings associated with this get settings response. Required. Python type: ``PaymentMethodSettings``; wire name: ``settings``; JSON type: object"""

from inttegro.payment_method.settings import Settings as PaymentMethodSettings
