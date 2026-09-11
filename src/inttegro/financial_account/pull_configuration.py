"""PullConfiguration in the ``inttegro.financial_account`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class PullConfiguration(ApiModel):
    """Typed pull configuration data in the financial account resource namespace.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``FinancialAccountPullConfiguration``.
    """
    enabled_at: datetime = field(init=False)
    """Timestamp for enabled at. Required. Python type: ``datetime``; wire name: ``enabled_at``; JSON type: string (date-time)"""
    mandate: FinancialAccountPullConfigurationMandate = field(init=False)
    """The mandate associated with this pull configuration. Required. Python type: ``FinancialAccountPullConfigurationMandate``; wire name: ``mandate``; JSON type: object (FinancialAccountMandate)"""

from inttegro.financial_account.pull_configuration_mandate import PullConfigurationMandate as FinancialAccountPullConfigurationMandate
