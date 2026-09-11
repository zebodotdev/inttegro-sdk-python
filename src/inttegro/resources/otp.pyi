"""Generated public typing surface. Do not edit by hand."""

from typing import Any

from ..http_client import HttpClient
from inttegro.otp.transaction import Transaction
from inttegro.otp.verification import Verification
from inttegro.otp.initiate_request import InitiateRequest
from inttegro.otp.verify_request import VerifyRequest
from inttegro.otp.lookup_request import LookupRequest

class Otp:
    def __init__(self, http: HttpClient) -> None: ...
    def initiate(self, payload: InitiateRequest) -> Transaction: ...
    def verify(self, payload: VerifyRequest) -> Verification: ...
    def lookup(self, payload: LookupRequest) -> Transaction: ...
    def cancel(self, payload: LookupRequest) -> Transaction: ...
