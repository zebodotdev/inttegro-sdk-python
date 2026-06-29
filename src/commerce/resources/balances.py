from __future__ import annotations

from ..http_client import HttpClient


class Balances:
    def __init__(self, http: HttpClient):
        self.http = http

    def get(self):
        return self.http.post("/balances", {})
