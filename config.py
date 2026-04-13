"""
config.py — Centralized test configuration for Urban Routes QA suite.

All test data and environment-specific values live here.
Tests import from this module — never hardcode values directly in test files.

Usage:
    from config import BASE_URL, TEST_DATA, TIMEOUTS

Setup:
    Copy .env.example to .env and fill in your values.
    python-dotenv will load them automatically via conftest.py.
"""

import os
from dotenv import load_dotenv

# Load .env file if present (local dev). CI injects vars directly.
load_dotenv()

# ─── URLs ────────────────────────────────────────────────────────────────────

BASE_URL: str = os.getenv(
    "URBAN_ROUTES_URL",
    "https://cnt-placeholder.containerhub.tripleten-services.com"
)

# ─── Test Data ────────────────────────────────────────────────────────────────

TEST_DATA: dict = {
    "from_address": os.getenv("TEST_FROM_ADDRESS", "East 2nd Street, 601"),
    "to_address":   os.getenv("TEST_TO_ADDRESS",   "1300 1st St"),
    "phone":        os.getenv("TEST_PHONE",         "+12025550199"),
    "card_number":  os.getenv("TEST_CARD_NUMBER",   "1234 0000 5678"),
    "card_cvv":     os.getenv("TEST_CARD_CVV",      "111"),
    "driver_comment": os.getenv("TEST_DRIVER_COMMENT", "Bring a blanket"),
    "sms_code":     os.getenv("TEST_SMS_CODE",      "000000"),  # Sandbox default
}

# ─── Timeouts (seconds) ───────────────────────────────────────────────────────

TIMEOUTS: dict = {
    "implicit":    int(os.getenv("TIMEOUT_IMPLICIT", "0")),   # Keep at 0 — use explicit waits
    "explicit":    int(os.getenv("TIMEOUT_EXPLICIT", "10")),
    "driver_info": int(os.getenv("TIMEOUT_DRIVER_INFO", "60")),  # Longer wait for driver modal
}

# ─── Screenshot Settings ──────────────────────────────────────────────────────

SCREENSHOTS_DIR: str = os.getenv("SCREENSHOTS_DIR", "screenshots")
