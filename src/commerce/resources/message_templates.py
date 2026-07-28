"""Message templates resource for reusable SMS and email content."""

from __future__ import annotations

from ..http_client import HttpClient


class MessageTemplates:
    """Create, publish, archive, look up, page, and preview message templates."""

    def __init__(self, http: HttpClient):
        self.http = http

    def create(self, payload: dict, idempotency_key: str | None = None):
        """Create a reusable message template."""
        return self.http.post_with_headers(
            "/message_templates/create",
            payload,
            self._idempotency_headers(idempotency_key),
        )

    def update(self, payload: dict, idempotency_key: str | None = None):
        """Update a message template draft."""
        return self.http.post_with_headers(
            "/message_templates/update",
            payload,
            self._idempotency_headers(idempotency_key),
        )

    def publish(self, template_id: str, idempotency_key: str | None = None):
        """Publish the current draft version of a template."""
        return self.http.post_with_headers(
            "/message_templates/publish",
            {"id": template_id},
            self._idempotency_headers(idempotency_key),
        )

    def archive(self, template_id: str, idempotency_key: str | None = None):
        """Archive a template."""
        return self.http.post_with_headers(
            "/message_templates/archive",
            {"id": template_id},
            self._idempotency_headers(idempotency_key),
        )

    def lookup(self, template_id: str):
        """Look up one template by ID."""
        return self.http.post("/message_templates/lookup", {"id": template_id})

    def page(self, payload: dict | None = None):
        """Page through message templates."""
        return self.http.post("/message_templates/page", payload or {})

    def render_preview(self, payload: dict):
        """Render a draft-aware template preview."""
        return self.http.post("/message_templates/render_preview", payload)

    def _idempotency_headers(self, idempotency_key: str | None) -> dict[str, str]:
        return {"Idempotency-Key": idempotency_key} if idempotency_key else {}
