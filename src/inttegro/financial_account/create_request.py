"""CreateRequest in the ``inttegro.financial_account`` resource namespace.

Generated from the Inttegro API contract; do not edit by hand.
"""

from __future__ import annotations
from typing import TypeAlias
from inttegro.financial_account.bank_request import BankRequest as FinancialAccountBankRequest
from inttegro.financial_account.dosh_request import DoshRequest as FinancialAccountDoshRequest
from inttegro.financial_account.wallet_request import WalletRequest as FinancialAccountWalletRequest


CreateRequest: TypeAlias = FinancialAccountWalletRequest | FinancialAccountBankRequest | FinancialAccountDoshRequest
"""Parameters for creating a financial account. The required ``type`` discriminator selects wallet, bank-account, or Dosh-account details and the corresponding typed configuration."""
