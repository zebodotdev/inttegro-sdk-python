"""CreateRequest in the ``inttegro.message_template`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from typing import TypeAlias
from inttegro.message_template.create_email_request import CreateEmailRequest as CreateEmailMessageTemplateRequest
from inttegro.message_template.create_sms_request import CreateSMSRequest as CreateSMSMessageTemplateRequest


CreateRequest: TypeAlias = CreateSMSMessageTemplateRequest | CreateEmailMessageTemplateRequest
"""Parameters for creating a message template. The required ``channel`` discriminator selects the SMS shape with SMS content or the email shape with email content and optional attachment IDs."""
