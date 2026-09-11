"""Generated public typing surface. Do not edit by hand."""

from typing import Any

from ..http_client import HttpClient
from inttegro.file_link.file_link import FileLink
from inttegro.file_link.creation import Creation
from inttegro.file_link.page import Page
from inttegro.file_link.create_request import CreateRequest
from inttegro.file_link.page_request import PageRequest
from inttegro.file_link.revoke_request import RevokeRequest
from .files import FileDownload

class FileLinks:
    def __init__(self, http: HttpClient) -> None: ...
    def create(self, payload: CreateRequest, idempotency_key: str | None = None) -> Creation: ...
    def lookup(self, id: str) -> FileLink: ...
    def page(self, payload: PageRequest | None = None) -> Page: ...
    def revoke(self, payload: RevokeRequest, idempotency_key: str | None = None) -> FileLink: ...
    def open(self, url: str, save_to: str | None = None) -> FileDownload: ...
