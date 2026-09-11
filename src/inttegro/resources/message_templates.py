"""Message templates resource for reusable SMS and email content."""

from __future__ import annotations

from ..http_client import HttpClient


class MessageTemplates:
    """Create, publish, archive, look up, page, and preview message templates.

    Access this service as ``InttegroClient.message_templates``. Methods use the client's shared transport and return the typed resource shapes documented below.
    """

    def __init__(self, http: HttpClient):
        self.http = http

    def create(self, payload: dict, idempotency_key: str | None = None):
        """Create a reusable message template.

        API endpoint: ``/message_templates/create``.

        Args:
            payload (dict): Typed request object or equivalent request mapping for this operation.
            idempotency_key (str | None): Optional stable key to reuse when retrying the same logical write.

        Returns:
            ``MessageTemplate`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post_with_headers(
            "/message_templates/create",
            payload,
            self._idempotency_headers(idempotency_key),
        )

    def update(self, payload: dict, idempotency_key: str | None = None):
        """Update a message template draft.

        API endpoint: ``/message_templates/update``.

        Args:
            payload (dict): Typed request object or equivalent request mapping for this operation.
            idempotency_key (str | None): Optional stable key to reuse when retrying the same logical write.

        Returns:
            ``MessageTemplate`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post_with_headers(
            "/message_templates/update",
            payload,
            self._idempotency_headers(idempotency_key),
        )

    def publish(self, template_id: str, idempotency_key: str | None = None):
        """Publish the current draft version of a template.

        API endpoint: ``/message_templates/publish``.

        Args:
            template_id (str): Unique identifier of the template.
            idempotency_key (str | None): Optional stable key to reuse when retrying the same logical write.

        Returns:
            ``MessageTemplate`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post_with_headers(
            "/message_templates/publish",
            {"id": template_id},
            self._idempotency_headers(idempotency_key),
        )

    def archive(self, template_id: str, idempotency_key: str | None = None):
        """Archive a template.

        API endpoint: ``/message_templates/archive``.

        Args:
            template_id (str): Unique identifier of the template.
            idempotency_key (str | None): Optional stable key to reuse when retrying the same logical write.

        Returns:
            ``MessageTemplate`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post_with_headers(
            "/message_templates/archive",
            {"id": template_id},
            self._idempotency_headers(idempotency_key),
        )

    def lookup(self, template_id: str):
        """Look up one template by ID.

        API endpoint: ``/message_templates/lookup``.

        Args:
            template_id (str): Unique identifier of the template.

        Returns:
            ``MessageTemplate`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/message_templates/lookup", {"id": template_id})

    def page(self, payload: dict | None = None):
        """Page through message templates.

        API endpoint: ``/message_templates/page``.

        Args:
            payload (dict | None): Typed request object or equivalent request mapping for this operation.

        Returns:
            ``Page`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/message_templates/page", payload or {})

    def render_preview(self, payload: dict):
        """Render a draft-aware template preview.

        API endpoint: ``/message_templates/render_preview``.

        Args:
            payload (dict): Typed request object or equivalent request mapping for this operation.

        Returns:
            ``Preview`` decoded from the documented response shape.

        Raises:
            APIError: The API rejected the request or could not complete it.
            NetworkError: The request could not reach the Inttegro API.
            TimeoutError: The configured request deadline elapsed.
        """
        return self.http.post("/message_templates/render_preview", payload)

    def _idempotency_headers(self, idempotency_key: str | None) -> dict[str, str]:
        return {"Idempotency-Key": idempotency_key} if idempotency_key else {}
