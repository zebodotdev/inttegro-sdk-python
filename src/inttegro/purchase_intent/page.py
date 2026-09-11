"""Page in the ``inttegro.purchase_intent`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class Page(ApiModel):
    """One page of page resources.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.

    API contract schema: ``PurchaseIntentPage``.
    """
    number: int = field(init=False)
    """One-based page number returned. Required. Python type: ``int``; wire name: ``number``; JSON type: integer"""
    purchase_intents: list[PurchaseIntent] = field(init=False)
    """The purchase intents associated with this page. Required. Python type: ``list[PurchaseIntent]``; wire name: ``purchase_intents``; JSON type: array of object (PurchaseIntent) values"""
    size: int = field(init=False)
    """Number of purchase intents actually returned. Required. Python type: ``int``; wire name: ``size``; JSON type: integer"""

from inttegro.purchase_intent.purchase_intent import PurchaseIntent
