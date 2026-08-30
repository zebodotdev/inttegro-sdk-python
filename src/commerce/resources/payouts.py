"""Payouts resource for managing fund transfers to financial accounts."""

from __future__ import annotations

from ..http_client import HttpClient


class Payouts:
    """
    Payouts resource for configuring and managing transfers of funds from your balance.

    Payouts move money from your Commerce balance to your financial accounts (bank accounts,
    mobile money wallets, or Dosh). You can configure automatic weekly payouts or trigger
    manual payouts on demand. Set different destinations for different currencies to route
    funds appropriately.

    The typical setup is:
    1. Connect financial accounts via the FinancialAccounts resource
    2. Set payout destinations (which financial account receives which currency)
    3. Configure automatic or manual payout schedule
    4. Monitor payouts via the page() method

    See https://studio.inttegro.com/payouts for detailed guides.
    """

    def __init__(self, http: HttpClient):
        """Initialize Payouts resource with HTTP client."""
        self.http = http

    def set_destinations(self, destinations: dict):
        """
        Configure where funds should be sent for each currency.

        Maps currencies to financial accounts so Commerce knows where to send payouts.
        Each currency can have one destination. When a payout is created, funds in each
        currency are sent to their configured financial account.

        You must set destinations before payouts can be processed. If you accept multiple
        currencies, configure a destination for each.

        Args:
            destinations: Currency-to-financial-account mapping where keys are currency
                codes (e.g., "ghs", "usd") and values are financial account IDs
                (e.g., "fa_abc123"). Example:
                    {
                        "ghs": "fa_mtn_wallet",
                        "usd": "fa_bank_account"
                    }

        Returns:
            ResponseObject containing:
                - settings: Updated payout settings with new destinations

        Raises:
            ApiError: If financial account doesn't exist or isn't verified

        Example:
            ```python
            # Set single currency destination
            result = client.payouts.set_destinations({
                "ghs": "fa_abc123"
            })

            # Set multi-currency destinations
            result = client.payouts.set_destinations({
                "ghs": "fa_mtn_wallet",
                "usd": "fa_bank_usd",
                "eur": "fa_bank_eur"
            })

            settings = result.data["settings"]
            print(f"Destinations configured: {settings['destinations']}")

            # Complete setup flow
            # Step 1: Connect financial account
            fa_result = client.financial_accounts.connect({
                "type": "wallet",
                "wallet": {
                    "type": "mobile_money",
                    "mobile_money": {
                        "network": "mtn",
                        "account_number": "0241234567"
                    }
                }
            })

            fa_id = fa_result.data["financial_account"]["id"]

            # Step 2: Verify financial account
            client.financial_accounts.verify(fa_id)
            # ... complete verification with OTP ...

            # Step 3: Set as payout destination
            client.payouts.set_destinations({
                "ghs": fa_id
            })

            print("Payout setup complete!")
            ```

        Note:
            - Financial accounts must be verified before use as payout destinations
            - Changing destinations affects future payouts only (not pending ones)
            - You can update destinations at any time

        See Also:
            - FinancialAccounts.connect(): Add new financial accounts
            - settings(): View current payout configuration
            - https://studio.inttegro.com/set-up-financial-account
        """
        return self.http.post("/payouts/set_destinations", {"destinations": destinations})

    def settings(self):
        """
        Retrieve current payout configuration.

        Gets your payout settings including schedule (automatic or manual), destinations
        (currency-to-financial-account mappings), and FX conversion preferences. Use this
        to display current configuration or verify setup completion.

        Returns:
            ResponseObject containing:
                - settings: Payout configuration including:
                    - schedule: Payout schedule object:
                        - type: "automatic" or "manual"
                        - interval: "weekly" for automatic
                        - schedule_on: Day of week for automatic (e.g., "monday")
                    - destinations: Currency-to-financial-account map
                    - fx_enabled: Whether currency conversion is enabled
                    - created_at: When settings were first created
                    - updated_at: When settings were last modified

        Example:
            ```python
            # Get current settings
            result = client.payouts.settings()
            settings = result.data["settings"]

            print(f"Schedule: {settings['schedule']['type']}")
            print(f"Destinations: {settings['destinations']}")
            print(f"FX enabled: {settings.get('fx_enabled', False)}")

            # Check if setup is complete
            def is_payout_configured():
                result = client.payouts.settings()
                settings = result.data["settings"]

                has_destinations = bool(settings.get("destinations"))
                has_schedule = settings.get("schedule", {}).get("type") is not None

                return has_destinations and has_schedule

            if is_payout_configured():
                print("Payouts are configured and ready")
            else:
                print("Complete payout setup in dashboard")

            # Display settings to user
            def show_payout_settings():
                result = client.payouts.settings()
                settings = result.data["settings"]

                schedule = settings["schedule"]
                if schedule["type"] == "automatic":
                    print(f"Automatic payouts every {schedule['interval']}")
                    print(f"Scheduled on: {schedule['schedule_on']}")
                else:
                    print("Manual payouts (trigger on demand)")

                print(f"\\nPayout destinations:")
                for currency, fa_id in settings["destinations"].items():
                    print(f"  {currency.upper()}: {fa_id}")
            ```

        See Also:
            - set_destinations(): Configure payout destinations
            - disable_automatic(): Switch to manual payouts
            - https://studio.inttegro.com/api/payouts/settings
        """
        return self.http.post("/payouts/settings", {})

    def schedule(self, payload: dict):
        """
        Schedule a payout to a connected financial account.

        Args:
            payload: Schedule parameters including destination_id, max_amount, reference,
                and optionally execute_after.

        Returns:
            ResponseObject containing the scheduled payout.
        """
        return self.http.post("/payouts/schedule", payload)

    def lookup(self, payout_id: str):
        """
        Retrieve a payout by ID.

        Args:
            payout_id: Payout identifier.

        Returns:
            ResponseObject containing the payout.
        """
        return self.http.post("/payouts/lookup", {"payout_id": payout_id})

    def disable_automatic(self):
        """
        Switch payout schedule to manual mode.

        Disables automatic weekly payouts, giving you full control over when payouts occur.
        In manual mode, payouts only happen when you explicitly trigger them through the
        dashboard or API. Use this for marketplaces, escrow scenarios, or when you need
        approval workflows before funds transfer.

        Once disabled, payouts won't occur automatically. You must manually trigger each
        payout when you're ready to receive funds.

        Returns:
            ResponseObject containing:
                - settings: Updated payout settings with manual schedule

        Example:
            ```python
            # Disable automatic payouts
            result = client.payouts.disable_automatic()
            settings = result.data["settings"]

            schedule = settings["schedule"]
            print(f"Schedule type: {schedule['type']}")  # "manual"
            print("Automatic payouts disabled. Trigger manually when needed.")

            # Marketplace scenario
            def setup_marketplace_payouts():
                # Disable automatic payouts
                client.payouts.disable_automatic()
                print("Manual payout mode enabled")

                # In your approval flow
                def approve_vendor_payout(vendor_id):
                    # Your approval logic
                    approved = check_vendor_approval(vendor_id)

                    if approved:
                        # Trigger manual payout via dashboard
                        print(f"Approved payout for vendor {vendor_id}")
                        print("Trigger payout in Commerce dashboard")

            # Re-enable automatic if needed
            # (Use dashboard: Commerce > Settings > Payouts > Schedule)
            ```

        Note:
            - Existing pending payouts are not affected
            - You can re-enable automatic payouts through the dashboard
            - Balance continues to accumulate until you trigger payouts

        See Also:
            - settings(): View current schedule configuration
            - page(): Monitor executed payouts
            - https://studio.inttegro.com/api/payouts/disable
        """
        return self.http.post("/payouts/disable", {})

    def enable_automatic(self):
        """
        Re-enable automatic payouts for your application.

        Returns:
            ResponseObject containing the updated payout settings.
        """
        return self.http.post("/payouts/enable", {})

    def enable_fx(self):
        """
        Enable foreign exchange conversion for payouts.

        Allows Commerce to automatically convert currencies during payouts when needed.
        When enabled and you have a destination configured for a base currency (e.g., GHS),
        funds in other currencies can be converted and included in that payout rather than
        waiting for a matching destination.

        FX conversion uses mid-market rates with transparent fees. Enable this if you want
        all funds consolidated into one currency, or disable to keep currencies separate.

        Returns:
            ResponseObject containing:
                - settings: Updated payout settings with FX enabled

        Example:
            ```python
            # Enable FX conversion
            result = client.payouts.enable_fx()
            settings = result.data["settings"]

            print(f"FX enabled: {settings.get('fx_enabled', False)}")

            # Consolidate multi-currency balance
            def setup_consolidated_payouts():
                # Set GHS as primary destination
                client.payouts.set_destinations({
                    "ghs": "fa_mtn_wallet"
                })

                # Enable FX to convert USD/EUR/etc to GHS
                client.payouts.enable_fx()

                print("All currencies will convert to GHS on payout")

            # Check FX status
            result = client.payouts.settings()
            if result.data["settings"].get("fx_enabled"):
                print("FX conversion is active")
            else:
                print("Currencies paid out separately")
            ```

        Note:
            - FX rates are determined at payout execution time
            - Check Commerce dashboard for current FX fees
            - Disable FX to keep currencies separate

        See Also:
            - disable_fx(): Turn off currency conversion
            - set_destinations(): Configure currency routing
            - https://studio.inttegro.com/api/payouts/enable-fx
        """
        return self.http.post("/payouts/enable_fx", {})

    def disable_fx(self):
        """
        Disable foreign exchange conversion for payouts.

        Prevents automatic currency conversion during payouts. With FX disabled, each
        currency requires its own destination financial account. Payouts occur per currency—
        GHS goes to GHS account, USD to USD account, etc. Currencies without configured
        destinations accumulate in your balance until you set up their destinations.

        Disable FX if you want to maintain separate currency balances or avoid conversion fees.

        Returns:
            ResponseObject containing:
                - settings: Updated payout settings with FX disabled

        Example:
            ```python
            # Disable FX conversion
            result = client.payouts.disable_fx()
            settings = result.data["settings"]

            print(f"FX enabled: {settings.get('fx_enabled', False)}")  # False

            # Multi-currency separate payouts
            def setup_separate_currency_payouts():
                # Disable FX
                client.payouts.disable_fx()

                # Set up separate destinations
                client.payouts.set_destinations({
                    "ghs": "fa_mtn_wallet",
                    "usd": "fa_bank_usd",
                    "eur": "fa_bank_eur"
                })

                print("Each currency pays out to its own account")

            # Check what happens to unmapped currencies
            result = client.payouts.settings()
            settings = result.data["settings"]

            destinations = settings.get("destinations", {})
            print(f"Configured destinations: {list(destinations.keys())}")
            print("Currencies without destinations will accumulate in balance")
            ```

        Note:
            - You need a financial account for each currency you accept
            - Currencies without destinations won't pay out automatically
            - Enable FX to consolidate into one currency

        See Also:
            - enable_fx(): Turn on currency conversion
            - set_destinations(): Configure per-currency accounts
            - https://studio.inttegro.com/api/payouts/disable-fx
        """
        return self.http.post("/payouts/disable_fx", {})

    def page(self, payload: dict | None = None):
        """
        List executed payouts with page-based pagination.

        Retrieves a paginated history of payouts that have been created. Use this to build
        payout history views, reconcile bank deposits, or export financial reports. Results
        include successful, failed, and pending payouts sorted by creation date (most recent
        first).

        Args:
            payload: Pagination parameters including:
                - page_number: Page index to fetch (1-10 inclusive, default: 1)
                - page_size: Number of payouts per page (1-256, default: 20)

        Returns:
            ResponseObject containing:
                - page: Object with:
                    - number: The page number returned
                    - size: Number of payouts in this page
                    - payouts: Array of payout objects with:
                        - id: Payout ID
                        - amount: Amount and currency
                        - status: Current status
                        - destination_id: Financial account that received funds
                        - initiated_by: How payout was initiated (automatic or manual)
                        - latest_attempt_id: Most recent execution attempt
                        - latest_error: Error details if payout failed

        Example:
            ```python
            # Get recent payouts
            result = client.payouts.page({"page_number": 1, "page_size": 20})
            page = result.data["page"]
            
            for payout in page["payouts"]:
                amount = payout["amount"]
                print(f"{payout['id']}: {amount['value']} {amount['currency']} - {payout['status']}")
            
            # Paginate through all payouts
            for page_num in range(1, 11):
                result = client.payouts.page({
                    "page_number": page_num,
                    "page_size": 50
                })
                
                page = result.data["page"]
                if page["size"] == 0:
                    break
                
                payouts = page["payouts"]
                print(f"Page {page_num}: {len(payouts)} payouts")
            
            # Get large page of payouts
            result = client.payouts.page({
                "page_number": 1,
                "page_size": 100
            })
            
            # Build reconciliation report
            def reconcile_payouts():
                result = client.payouts.page({
                    "page_number": 1,
                    "page_size": 256  # Maximum page size
                })
                
                total_paid = {}
                for payout in result.data["page"]["payouts"]:
                    if payout["status"] != "paid":
                        continue
                    
                    amount = payout["amount"]
                    currency = amount["currency"]
                    value = amount["value"]
                    
                    if currency not in total_paid:
                        total_paid[currency] = 0
                    
                    total_paid[currency] += value
                
                print("Total payouts by currency:")
                for currency, total in total_paid.items():
                    print(f"  {currency.upper()}: {total}")
            ```

        See Also:
            - settings(): View payout configuration
            - https://studio.inttegro.com/api/payouts/page
        """
        return self.http.post("/payouts/page", payload or {})

    def cancel(self, payout_id: str):
        """
        Cancel a scheduled payout before it executes.

        Only payouts in `scheduled` status with a future `execute_after` timestamp
        can be canceled. On success, returns the canceled payout payload.

        Args:
            payout_id: ID of the scheduled payout to cancel.

        Returns:
            ResponseObject containing:
                - payout: Updated payout object with `status` set to `canceled`
        """
        return self.http.post("/payouts/cancel", {"payout_id": payout_id})
