# Servers.com Test Automation

Frontend test automation for **servers.com** built with **Playwright +
pytest**.

------------------------------------------------------------------------

## Project Structure

    servers/
    ├── pages/              # Page Object classes
    │   ├── base_page.py
    │   ├── main_page.py
    │   ├── login_page.py
    │   ├── dashboard_page.py
    │   ├── account_page.py
    │   ├── contact_page.py
    │   ├── contact_page_edit.py
    │   ├── new_contact_page.py
    │   └── ...
    ├── components/         # Reusable UI components
    │   └── side_menu.py
    ├── tests/              # Tests (one test = one file)
    │   ├── login/
    │   ├── logout/
    │   ├── account/
    │   ├── side_bar/       # Side bar sections (cloud servers, reports, etc.)
    │   └── ...
    ├── utils/
    │   ├── webdriver.py    # Playwright wrapper
    │   └── custom_expect.py # Custom expect assertions
    ├── storage/            # Auto-generated storage (gitignored)
    ├── conftest.py
    ├── pyproject.toml
    ├── .python-version     # Python 3.12
    └── uv.lock

------------------------------------------------------------------------

## Local Setup (macOS only)

Follow these steps to install all required tools and run the tests
locally. This guide is for macOS only.

### 1. Install Homebrew (if not installed)

Open Terminal and run:

``` bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Verify:

``` bash
brew --version
```

------------------------------------------------------------------------

### 2. Install Python

``` bash
brew install python
```

Verify:

``` bash
python3 --version
```

Python 3.12 is required.

------------------------------------------------------------------------

### 3. Install uv

``` bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Reload shell:

``` bash
source ~/.zshrc
```

Verify:

``` bash
uv --version
```

------------------------------------------------------------------------

### 4. Clone repository

``` bash
git clone <repository_url>
cd servers
```

Make sure you are in the **project root directory**.

------------------------------------------------------------------------

### 5. Install dependencies

``` bash
uv sync
```

------------------------------------------------------------------------

### 6. Install Playwright browsers

``` bash
uv run playwright install chromium
```

------------------------------------------------------------------------

## Base URL

    https://portal.servers.com

------------------------------------------------------------------------

## Running Tests

Parallel execution (e.g. pytest-xdist) is not supported.

### Run all tests (visible mode)

From the project root directory:

``` bash
uv run pytest --base-url https://portal.servers.com --browser chromium --no-headless
```

------------------------------------------------------------------------

### Run all tests (headless mode)

``` bash
uv run pytest --base-url https://portal.servers.com --browser chromium
```

------------------------------------------------------------------------

### Run a specific test

``` bash
uv run pytest tests/login/test_successful_login_with_valid_credentials.py --base-url https://portal.servers.com --browser chromium
```

------------------------------------------------------------------------

## Project Rules

-   One test = one file
-   Page Object Pattern
-   Locators via @property
-   Automatic storage handling

------------------------------------------------------------------------

## Storage Reset

``` bash
rm -rf storage/
uv run pytest --base-url https://portal.servers.com --browser chromium
```
