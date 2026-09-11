"""CountrySpecification in the ``inttegro.shared`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inttegro._model_base import ApiModel


@dataclass(frozen=True, slots=True, init=False, repr=False, eq=False)
class CountrySpecification(ApiModel):
    """Complete specification for a country including supported features and requirements.

    Instances are immutable API responses. ``from_dict()`` decodes nested
    objects, string-backed enums, and timezone-aware ISO-8601 timestamps;
    ``to_dict()`` returns the corresponding JSON-compatible wire shape.
    Fields not returned by the API remain absent and can still be queried
    through mapping-style access.
    """
    country_code: str = field(init=False)
    """ISO 3166-1 alpha-2 country code. Required. Python type: ``str``; wire name: ``country_code``; JSON type: string"""
    country_name: str = field(init=False)
    """Full country name. Required. Python type: ``str``; wire name: ``country_name``; JSON type: string"""
    currencies: list[str] = field(init=False)
    """Supported currencies in this country. Required. Python type: ``list[str]``; wire name: ``currencies``; JSON type: array of string values"""
    payment_methods: list[str] = field(init=False)
    """Supported payment methods in this country. Required. Python type: ``list[str]``; wire name: ``payment_methods``; JSON type: array of string values"""
    payout_schedules: list[str] = field(init=False)
    """Available payout schedules for this country. Required. Python type: ``list[str]``; wire name: ``payout_schedules``; JSON type: array of string values"""
    bt_aging_specs: list[str] = field(init=False)
    """Balance transaction aging specifications available. Required. Python type: ``list[str]``; wire name: ``bt_aging_specs``; JSON type: array of string values"""
    legal_entity_types: list[str] = field(init=False)
    """Legal entity types that can operate in this country. Required. Python type: ``list[str]``; wire name: ``legal_entity_types``; JSON type: array of string values"""
    financial_account_types: list[str] = field(init=False)
    """Financial account types available in this country. Required. Python type: ``list[str]``; wire name: ``financial_account_types``; JSON type: array of string values"""
    id_document_types: list[str] = field(init=False)
    """Identification document types accepted in this country. Required. Python type: ``list[str]``; wire name: ``id_document_types``; JSON type: array of string values"""
    banks: CountryBankDirectory | None = field(init=False)
    """Bank reference data available for country-specific bank accounts. Optional; nullable. Python type: ``CountryBankDirectory | None``; wire name: ``banks``; JSON type: object (CountryBankDirectory)"""

from inttegro.shared.country_bank_directory import CountryBankDirectory
