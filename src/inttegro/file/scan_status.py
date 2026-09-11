"""ScanStatus in the ``inttegro.file`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from inttegro._enum_base import WireEnum


class ScanStatus(WireEnum):
    """Typed scan status data in the file resource namespace.

    Members are strings as well as enum values, so they compare naturally
    with API payloads and serialize to the lowercase wire value shown below.

    API contract schema: ``FileScanStatus``.
    """
    PENDING = "pending"
    """Wire value ``pending`` (pending)"""
    PASSED = "passed"
    """Wire value ``passed`` (passed)"""
    FAILED = "failed"
    """Wire value ``failed`` (failed)"""
    SKIPPED = "skipped"
    """Wire value ``skipped`` (skipped)"""
