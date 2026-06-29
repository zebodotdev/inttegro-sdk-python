"""OTP resource for one-time password verification."""

from __future__ import annotations

from ..http_client import HttpClient


class Otp:
    """
    OTP resource for generating and verifying one-time passwords.

    The OTP resource provides standalone one-time password functionality for verifying
    phone numbers, confirming sensitive actions, or adding two-factor authentication.
    This is separate from payment and payment method verification OTPs.

    See https://commerce.zebo.dev/api/otp for detailed documentation.
    """

    def __init__(self, http: HttpClient):
        """Initialize OTP resource with HTTP client."""
        self.http = http

    def initiate(self, payload: dict):
        """
        Initiate an OTP verification flow.

        Generates and sends a one-time password to the specified recipient. The customer
        receives the OTP via SMS and must submit it via verify() to complete verification.

        Args:
            payload: Initiation parameters including recipient, sender, and service_name

        Returns:
            ResponseObject containing the OTP transaction with id and expiry information

        Example:
            ```python
            result = client.otp.initiate({
                "recipient": "+233241234567",
                "sender": "Acme",
                "service_name": "Acme Bank",
                "request_meta": {"idempotency_key": "otp_login_1700000000"}
            })
            txn_id = result.data["transaction"]["id"]
            ```

        See Also:
            - verify(): Submit OTP code to complete verification
        """
        return self.http.post("/otp/initiate", payload)

    def verify(self, payload: dict):
        """
        Verify an OTP code submitted by the user.

        Validates the OTP code entered by the customer against the active OTP transaction.
        If the code is correct and not expired, verification succeeds.

        Args:
            payload: Verification parameters including transaction_id, recipient, and token

        Returns:
            ResponseObject containing the OTP session with updated status and verified flag

        Example:
            ```python
            result = client.otp.verify({
                "transaction_id": "ot_abc123",
                "recipient": "+233241234567",
                "token": "123456"
            })
            if result.data.get("transaction", {}).get("status") == "verified":
                print("OTP verified!")
            ```

        See Also:
            - initiate(): Start OTP verification flow
        """
        return self.http.post("/otp/verify", payload)

    def lookup(self, payload: dict):
        """
        Retrieve details of an OTP transaction.

        Fetches information about an OTP verification transaction including its status
        and expiration. Use debug_mode=1 to include verification attempts.

        Args:
            payload: Lookup parameters including transaction_id

        Returns:
            ResponseObject containing the OTP session details

        Example:
            ```python
            result = client.otp.lookup({"transaction_id": "ot_abc123"})
            print(f"Status: {result.data['transaction']['status']}")
            ```

        See Also:
            - initiate(): Create OTP sessions
        """
        return self.http.post("/otp/lookup", payload)

    def cancel(self, payload: dict):
        """
        Cancel an active OTP transaction.

        Invalidates an OTP transaction before it expires naturally. Use this when the user
        abandons the verification flow or requests a new OTP.

        Args:
            payload: Cancellation parameters including transaction_id and reason

        Returns:
            ResponseObject containing the cancelled OTP session

        Example:
            ```python
            result = client.otp.cancel({
                "transaction_id": "ot_abc123",
                "reason": "user_requested_new_code"
            })
            ```

        See Also:
            - initiate(): Create new OTP after cancellation
        """
        return self.http.post("/otp/cancel", payload)
