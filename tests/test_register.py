import uuid

import pytest
from playwright.sync_api import Page

from pages.register_page import RegisterPage


def _make_user(username: str) -> dict:
    return {
        "first_name": "Test",
        "last_name": "User",
        "address": "123 Main Street",
        "city": "Springfield",
        "state": "IL",
        "zip_code": "62701",
        "phone": "2175550100",
        "ssn": "987-65-4321",
        "username": username,
        "password": "P@ssw0rd1",
        "confirm_password": "P@ssw0rd1",
    }


_REGISTRATION_DISABLED = pytest.mark.skip(
    reason="Registration form is disabled on this test instance "
    "('Dear client, you can not register in the system')"
)


class TestRegister:
    @pytest.mark.smoke
    @_REGISTRATION_DISABLED
    def test_new_user_registration_succeeds(self, page: Page):
        unique_username = f"user_{uuid.uuid4().hex[:8]}"
        register = RegisterPage(page)
        register.navigate()
        register.register(_make_user(unique_username))
        assert register.is_registered_successfully(), (
            f"Expected welcome heading after registering '{unique_username}', "
            f"got: {register.get_heading_text()!r}"
        )

    @pytest.mark.negative
    @_REGISTRATION_DISABLED
    def test_duplicate_username_shows_error(self, page: Page):
        # "john" is a pre-existing account, so re-registering should fail
        register = RegisterPage(page)
        register.navigate()
        register.register(_make_user("john"))
        errors = register.get_error_messages()
        assert errors, "At least one validation error must appear for a duplicate username"
        assert any("already" in e.lower() for e in errors), (
            f"Expected 'already exists' error, got: {errors}"
        )

    @pytest.mark.negative
    @_REGISTRATION_DISABLED
    def test_mismatched_passwords_show_error(self, page: Page):
        user_data = _make_user(f"user_{uuid.uuid4().hex[:8]}")
        user_data["confirm_password"] = "DifferentPassword!"
        register = RegisterPage(page)
        register.navigate()
        register.register(user_data)
        errors = register.get_error_messages()
        assert errors, "A validation error must appear for mismatched passwords"
