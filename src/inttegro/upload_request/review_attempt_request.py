"""ReviewAttemptRequest in the ``inttegro.upload_request`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from typing import TypeAlias
from inttegro.upload_request.review_attempt_by_id_request import ReviewAttemptByIDRequest as ReviewUploadRequestAttemptByIDRequest
from inttegro.upload_request.review_attempt_by_ordinal_request import ReviewAttemptByOrdinalRequest as ReviewUploadRequestAttemptByOrdinalRequest


ReviewAttemptRequest: TypeAlias = ReviewUploadRequestAttemptByIDRequest | ReviewUploadRequestAttemptByOrdinalRequest
"""A review decision targeting one upload attempt. Identify the attempt with its stable ``attempt_id`` or with its integer ``attempt_ordinal`` within the upload request."""
