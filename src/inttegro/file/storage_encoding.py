"""StorageEncoding in the ``inttegro.file`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class StorageEncoding(WireEnum):
    """Encoding of the stored representation.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``FileStorageEncoding``.
    """
    IDENTITY = "identity"
    """Wire value ``identity`` (identity) for encoding of the stored representation"""
    BROTLI = "br"
    """Wire value ``br`` (brotli) for encoding of the stored representation"""
