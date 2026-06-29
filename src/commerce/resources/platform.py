"""Platform resource for application and API key management."""

from __future__ import annotations

from ..http_client import HttpClient


class Platform:
    """
    Platform resource for managing applications, API keys, and sessions.

    The Platform resource provides administrative functionality for managing your Commerce
    account, applications, API keys, and active sessions. Most applications don't need
    these endpoints as they're primarily used by the Commerce dashboard.

    See https://commerce.zebo.dev/api/platform for detailed documentation.
    """

    def __init__(self, http: HttpClient):
        """Initialize Platform resource with HTTP client."""
        self.http = http

    def create_app(self, payload: dict):
        """
        Create a new application.

        Creates a new Commerce application under your account. Applications represent
        separate projects or environments and have their own API keys and settings.

        Args:
            payload: Application creation parameters including name and configuration

        Returns:
            ResponseObject containing the created application with id and API keys

        Example:
            ```python
            result = client.platform.create_app({
                "name": "My New App",
                "description": "Production environment"
            })
            ```
        """
        return self.http.post("/apps/create", payload)

    def generate_key(self, payload: dict):
        """
        Generate a new API key for an application.

        Creates a new API key (secret or publishable) for the specified application.
        Use this to rotate keys or create additional keys for different environments.

        Args:
            payload: Key generation parameters including app_id and key type

        Returns:
            ResponseObject containing the generated API key

        Example:
            ```python
            result = client.platform.generate_key({
                "app_id": "app_abc123",
                "type": "secret"
            })
            ```

        Security Note:
            Store API keys securely. Never expose secret keys in client-side code.
        """
        return self.http.post("/keys/generate", payload)

    def new_session(self, payload: dict):
        """
        Create a new authenticated session.

        Creates a new session for API authentication. This is primarily used by the
        Commerce dashboard and administrative tools.

        Args:
            payload: Session creation parameters

        Returns:
            ResponseObject containing the session token and details

        Example:
            ```python
            result = client.platform.new_session({
                "email": "admin@example.com",
                "password": "secure_password"
            })
            ```
        """
        return self.http.post("/sessions/new", payload)
