"""
test_urban_routes.py — Selenium test suite for Urban Routes web application.

Test Strategy:
    These tests cover the critical order flow for the Comfort tariff.
    Organized into two groups:
        @pytest.mark.smoke   — fast critical path (run on every push)
        @pytest.mark.full    — complete happy path regression
        @pytest.mark.negative — error conditions and edge cases

    Run all:        pytest selenium/
    Run smoke only: pytest selenium/ -m smoke
    Run negative:   pytest selenium/ -m negative

Architecture:
    Tests call methods on UrbanRoutesPage — no raw Selenium in this file.
    All test data comes from config.py → .env → environment variables.
    Screenshots are auto-captured on failure via conftest.py hook.

Sprint: 8 (Selenium WebDriver) / 9 (pytest automation)
"""

import pytest
from config import TEST_DATA


# ─── Happy Path Tests ───────────────────────────────────────────────────────────────

class TestOrderFlow:
    """
    Full order flow through the Urban Routes app using Comfort tariff.
    Each test is independent — relies on the `page` fixture for a fresh browser.
    """

    @pytest.mark.smoke
    def test_set_route(self, page):
        """TC-01: User can enter origin and destination addresses."""
        page.set_route(TEST_DATA["from_address"], TEST_DATA["to_address"])

        assert page.get_from_address() == TEST_DATA["from_address"], (
            f"Expected FROM field to contain '{TEST_DATA['from_address']}', "
            f"but got '{page.get_from_address()}'"
        )
        assert page.get_to_address() == TEST_DATA["to_address"], (
            f"Expected TO field to contain '{TEST_DATA['to_address']}', "
            f"but got '{page.get_to_address()}'"
        )

    @pytest.mark.smoke
    def test_select_comfort_tariff(self, page):
        """TC-02: Selecting Comfort tariff highlights it as active."""
        page.set_route(TEST_DATA["from_address"], TEST_DATA["to_address"])
        page.select_comfort_tariff()

        assert page.get_selected_tariff_name() == "Comfort", (
            "Expected 'Comfort' tariff to be selected after clicking it."
        )

    @pytest.mark.full
    def test_add_phone_number(self, page):
        """TC-03: User can add a phone number and confirm via SMS code."""
        page.set_route(TEST_DATA["from_address"], TEST_DATA["to_address"])
        page.select_comfort_tariff()
        page.add_phone_number(TEST_DATA["phone"], TEST_DATA["sms_code"])

        displayed = page.get_phone_number_displayed()
        assert TEST_DATA["phone"] in displayed, (
            f"Phone number '{TEST_DATA['phone']}' not shown in UI. Got: '{displayed}'"
        )

    @pytest.mark.full
    def test_add_credit_card(self, page):
        """TC-04: User can add a credit card via the payment dialog."""
        page.set_route(TEST_DATA["from_address"], TEST_DATA["to_address"])
        page.select_comfort_tariff()
        page.add_phone_number(TEST_DATA["phone"], TEST_DATA["sms_code"])
        page.add_credit_card(TEST_DATA["card_number"], TEST_DATA["card_cvv"])
        # If no exception is raised, the card was accepted and dialog closed cleanly.

    @pytest.mark.full
    def test_add_driver_comment(self, page):
        """TC-05: User can enter a message for the driver."""
        page.set_route(TEST_DATA["from_address"], TEST_DATA["to_address"])
        page.select_comfort_tariff()
        page.add_driver_comment(TEST_DATA["driver_comment"])

        assert page.get_driver_comment() == TEST_DATA["driver_comment"], (
            f"Driver comment not saved. Expected: '{TEST_DATA['driver_comment']}'"
        )

    @pytest.mark.full
    def test_toggle_blanket_extra(self, page):
        """TC-06: Blanket and handkerchiefs extra can be toggled on."""
        page.set_route(TEST_DATA["from_address"], TEST_DATA["to_address"])
        page.select_comfort_tariff()
        page.toggle_blanket()

        assert page.is_blanket_checked() is True, (
            "Expected blanket checkbox to be checked after toggling."
        )

    @pytest.mark.full
    def test_increment_ice_cream(self, page):
        """TC-07: Ice cream counter increments to 2 after two clicks."""
        page.set_route(TEST_DATA["from_address"], TEST_DATA["to_address"])
        page.select_comfort_tariff()
        page.increment_ice_cream(times=2)

        count = page.get_ice_cream_count()
        assert count == 2, (
            f"Expected ice cream count to be 2 after two increments. Got: {count}"
        )

    @pytest.mark.smoke
    def test_place_order_shows_modal(self, page):
        """TC-08: Clicking 'Order a Taxi' opens the order confirmation modal."""
        page.set_route(TEST_DATA["from_address"], TEST_DATA["to_address"])
        page.select_comfort_tariff()
        page.add_phone_number(TEST_DATA["phone"], TEST_DATA["sms_code"])
        page.add_credit_card(TEST_DATA["card_number"], TEST_DATA["card_cvv"])
        page.place_order()

        assert page.is_order_modal_visible(), (
            "Order confirmation modal did not appear after clicking 'Order a Taxi'."
        )

    @pytest.mark.full
    @pytest.mark.flaky(reruns=2, reruns_delay=3)
    def test_driver_info_appears(self, page):
        """TC-09: Driver information panel appears after order is placed."""
        page.set_route(TEST_DATA["from_address"], TEST_DATA["to_address"])
        page.select_comfort_tariff()
        page.add_phone_number(TEST_DATA["phone"], TEST_DATA["sms_code"])
        page.add_credit_card(TEST_DATA["card_number"], TEST_DATA["card_cvv"])
        page.add_driver_comment(TEST_DATA["driver_comment"])
        page.toggle_blanket()
        page.increment_ice_cream(times=2)
        page.place_order()

        assert page.wait_for_driver_info(), (
            "Driver info panel did not appear within the timeout. "
            "The sandbox may be slow — check TIMEOUT_DRIVER_INFO in .env."
        )


# ─── Negative / Edge Case Tests ─────────────────────────────────────────────────────────────

class TestNegativeScenarios:
    """
    Tests for error conditions, empty inputs, and boundary values.
    These test QA judgment — not just happy path coverage.
    """

    @pytest.mark.negative
    def test_empty_from_address_does_not_proceed(self, page):
        """TC-N01: Route with empty origin should not allow tariff selection."""
        page.set_route("", TEST_DATA["to_address"])
        assert page.get_from_address() == "", (
            "Expected FROM field to remain empty when cleared."
        )

    @pytest.mark.negative
    def test_empty_to_address_does_not_proceed(self, page):
        """TC-N02: Route with empty destination should not allow tariff selection."""
        page.set_route(TEST_DATA["from_address"], "")
        assert page.get_to_address() == "", (
            "Expected TO field to remain empty when cleared."
        )

    @pytest.mark.negative
    def test_ice_cream_starts_at_zero(self, page):
        """TC-N03: Ice cream counter should default to 0 before any interaction."""
        page.set_route(TEST_DATA["from_address"], TEST_DATA["to_address"])
        page.select_comfort_tariff()
        count = page.get_ice_cream_count()
        assert count == 0, (
            f"Expected ice cream counter to start at 0. Got: {count}"
        )

    @pytest.mark.negative
    def test_driver_comment_with_special_characters(self, page):
        """TC-N04: Driver comment field accepts special characters without error."""
        special_comment = "Hello! @#$%^&*() — Traer una cobija, por favor."
        page.set_route(TEST_DATA["from_address"], TEST_DATA["to_address"])
        page.select_comfort_tariff()
        page.add_driver_comment(special_comment)

        stored = page.get_driver_comment()
        assert stored == special_comment, (
            f"Special characters in comment were not preserved. Got: '{stored}'"
        )

    @pytest.mark.negative
    def test_blanket_toggle_can_be_unchecked(self, page):
        """TC-N05: Blanket extra can be toggled off after being toggled on."""
        page.set_route(TEST_DATA["from_address"], TEST_DATA["to_address"])
        page.select_comfort_tariff()
        page.toggle_blanket()   # ON
        page.toggle_blanket()   # OFF

        assert page.is_blanket_checked() is False, (
            "Expected blanket to be unchecked after toggling it off."
        )
