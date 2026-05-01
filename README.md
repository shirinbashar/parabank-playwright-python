# ParaBank Playwright Python

End-to-end test automation framework for [ParaBank](https://para.testar.org/parabank/index.htm) — a demo banking application — built with **Playwright**, **pytest**, and the **Page Object Model** pattern.

---

## Project Structure

```
parabank-playwright-python/
├── pages/                        # Page Object Model classes
│   ├── __init__.py
│   ├── base_page.py              # Shared base with common helpers
│   ├── login_page.py             # Login page
│   ├── home_page.py              # Post-login home / navigation
│   ├── register_page.py          # Registration page
│   └── account_overview_page.py  # Accounts Overview page
├── tests/                        # pytest test suites
│   ├── __init__.py
│   ├── test_login.py             # Valid & invalid login scenarios
│   ├── test_register.py          # New user registration scenarios
│   └── test_account_overview.py  # Account Overview page tests
├── .github/
│   └── workflows/
│       └── ci.yml                # GitHub Actions CI/CD pipeline
├── conftest.py                   # Shared pytest fixtures
├── pytest.ini                    # pytest configuration
├── requirements.txt
└── README.md
```

---

## Prerequisites

- Python 3.10 or higher
- pip

---

## Installation

```bash
# 1. Clone the repository
git clone <repo-url>
cd parabank-playwright-python

# 2. (Optional) Create and activate a virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install Playwright browsers
playwright install chromium
```

---

## Running Tests

### Run all tests

```bash
pytest
```

### Run a specific test file

```bash
pytest tests/test_login.py
```

### Run by marker

```bash
pytest -m smoke       # Smoke tests only
pytest -m negative    # Negative / error-path tests only
pytest -m regression  # Regression tests only
```

### Run headed (visible browser)

```bash
pytest --headed
```

### Run with a specific browser

```bash
pytest --browser firefox
pytest --browser webkit
```

### Run tests in parallel (requires pytest-xdist)

```bash
pip install pytest-xdist
pytest -n auto
```

---

## HTML Report

An HTML report is generated automatically at `reports/report.html` after every run.  
Open it with any browser:

```bash
start reports/report.html        # Windows
open reports/report.html         # macOS
xdg-open reports/report.html     # Linux
```

---

## Test Coverage

| File | Tests | Markers |
|------|-------|---------|
| `test_login.py` | Valid login (logout link visible, URL change), invalid credentials, empty credentials, wrong password | `smoke`, `negative` |
| `test_register.py` | New user registration, duplicate username error, mismatched passwords error | `smoke`, `negative` |
| `test_account_overview.py` | Page loads after login, at least one account visible, accessible via nav, total balance shown | `smoke`, `regression` |

---

## Fixtures (`conftest.py`)

| Fixture | Scope | Description |
|---------|-------|-------------|
| `page` | function | Auto-provided by pytest-playwright — fresh browser page per test |
| `login_page` | function | Navigates to the login page and returns a `LoginPage` instance |
| `authenticated_page` | function | Logs in as `john / demo` and returns the authenticated page |

---

## Page Objects

| Class | URL | Key Methods |
|-------|-----|-------------|
| `BasePage` | — | `get_title()`, `get_current_url()`, `wait_for_load()` |
| `LoginPage` | `/parabank/index.htm` | `navigate()`, `login(user, pwd)`, `get_error_message()`, `is_error_displayed()` |
| `HomePage` | (post-login) | `is_logged_in()`, `get_welcome_text()`, `go_to_account_overview()`, `logout()` |
| `RegisterPage` | `/parabank/register.htm` | `navigate()`, `register(data)`, `is_registered_successfully()`, `get_error_messages()` |
| `AccountOverviewPage` | `/parabank/overview.htm` | `navigate()`, `is_loaded()`, `get_account_count()`, `get_total_balance_text()` |

---

## CI/CD

The GitHub Actions workflow (`.github/workflows/ci.yml`) runs on every push and pull request to `main`:

1. Sets up Python 3.12
2. Installs dependencies and Playwright's Chromium browser
3. Runs the full test suite
4. Uploads the HTML report as a downloadable artifact (retained 14 days)

---

## Credentials

| Use | Username | Password |
|-----|----------|----------|
| Valid login | `john` | `demo` |
| Invalid login | `invalid_user` | `wrong_pass` |
