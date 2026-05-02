import pytest
from playwright.sync_api import APIRequestContext

API_BASE = "/parabank/services/bank"


class TestCustomerAPI:
    @pytest.mark.api
    def test_get_valid_customer_returns_200(self, api_context: APIRequestContext):
        response = api_context.get(f"{API_BASE}/customers/12212")
        assert response.status == 200, f"Expected 200, got {response.status}"
        body = response.text()
        assert body, "Response body must not be empty"
        assert "12212" in body, f"Customer ID 12212 not found in response: {body[:200]}"

    @pytest.mark.api
    def test_get_valid_account_returns_200(self, api_context: APIRequestContext):
        response = api_context.get(f"{API_BASE}/accounts/12345")
        assert response.status == 200, f"Expected 200, got {response.status}"
        body = response.text()
        assert body, "Response body must not be empty"
        assert "12345" in body, f"Account ID 12345 not found in response: {body[:200]}"

    @pytest.mark.api
    def test_get_invalid_customer_returns_error(self, api_context: APIRequestContext):
        response = api_context.get(f"{API_BASE}/customers/99999")
        assert response.status >= 400, (
            f"Expected an error status code for non-existent customer, got {response.status}"
        )
