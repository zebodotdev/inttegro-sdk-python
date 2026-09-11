"""ReferenceInput in the ``inttegro.message_template`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._request_base import ApiRequest, UNSET, UnsetType


@dataclass(frozen=True, slots=True, kw_only=True)
class ReferenceInput(ApiRequest):
    """Parameters accepted by the reference input operation.

    This is an immutable, keyword-only request object. ``to_dict()`` uses
    the documented wire names, omits fields left as ``UNSET``, serializes
    string-backed enums by value, and requires timezone-aware datetimes.

    API contract schema: ``MessageTemplateReferenceInput``.
    """
    variables: MessageTemplateVariablesInput | UnsetType = field(default=UNSET)
    """Variable values used when rendering a template. Optional. Python type: ``MessageTemplateVariablesInput``; wire name: ``variables``; JSON type: object (MessageTemplateVariables)"""
    template_id: str
    """API-generated message template id. Required. Python type: ``str``; wire name: ``template_id``; JSON type: string"""

from inttegro.message_template.variables_input import VariablesInput as MessageTemplateVariablesInput
