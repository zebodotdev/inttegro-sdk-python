"""Generated public typing surface. Do not edit by hand."""

from typing import Any

from ..http_client import HttpClient
from inttegro.shared.country_specification import CountrySpecification

class Spec:
    def __init__(self, http: HttpClient) -> None: ...
    def countries(self) -> dict[str, CountrySpecification]: ...
