"""Spec resource for retrieving API specifications and supported values."""

from __future__ import annotations

from ..http_client import HttpClient


class Spec:
    """
    Spec resource for retrieving supported countries, currencies, and API specifications.

    The Spec resource provides reference data about what Inttegro supports including
    available countries, currencies, payment methods per country, and mobile money
    issuers. Use this to build dynamic forms, validate user input, or display
    available options.

    See https://studio.inttegro.com/api/spec for detailed documentation.
    """

    def __init__(self, http: HttpClient):
        """Initialize Spec resource with HTTP client."""
        self.http = http

    def countries(self):
        """
        Retrieve the list of supported countries and their specifications.

        Returns detailed information about each country Inttegro supports including
        available currencies, payment methods, mobile money issuers, and other
        country-specific configuration.

        Returns:
            ResponseObject containing:
                - countries: List of country objects with:
                    - code: ISO 3166-1 alpha-2 country code (e.g., "GH")
                    - name: Country name
                    - currencies: Supported currency codes
                    - payment_methods: Available payment types
                    - mobile_money: Mobile money issuer details (if available)
                    - banks: Bank information (if available)

        Example:
            ```python
            # Get all supported countries
            result = client.spec.countries()
            countries = result.data["countries"]

            for country in countries:
                print(f"{country['name']} ({country['code']})")
                print(f"  Currencies: {', '.join(country['currencies'])}")
                print(f"  Payment methods: {', '.join(country['payment_methods'])}")

            # Build country selector
            def get_country_options():
                result = client.spec.countries()
                return [
                    {"code": c["code"], "name": c["name"]}
                    for c in result.data["countries"]
                ]

            # Get mobile money issuers for Ghana
            result = client.spec.countries()
            ghana = next(c for c in result.data["countries"] if c["code"] == "GH")
            issuers = ghana.get("mobile_money", {}).get("issuers", [])
            print(f"Ghana mobile money: {issuers}")
            ```

        Use Cases:
            - Building country/currency selectors in forms
            - Validating user-selected payment methods
            - Displaying available options based on customer location
            - Dynamic form generation

        See Also:
            - https://studio.inttegro.com/api/spec/countries
        """
        return self.http.post("/spec/countries", {})
