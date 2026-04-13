# Contributing & Local Setup

This guide gets the Urban Routes Selenium suite running on your machine in under 5 minutes.

---

## Prerequisites

| Tool | Version | Check |
|------|---------|-------|
| Python | 3.10+ | `python3 --version` |
| Google Chrome | latest stable | `google-chrome --version` |
| ChromeDriver | must match Chrome | auto-managed by Selenium 4 |
| Git | any | `git --version` |

> **Note:** Selenium 4.6+ manages ChromeDriver automatically. No manual download needed.

---

## 1. Clone the Repository

```bash
git clone https://github.com/efrain-solivan/TripleTen-QA-projects-ES.git
cd TripleTen-QA-projects-ES
```

---

## 2. Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate        # macOS / Linux
# .venv\Scripts\activate         # Windows
```

You should see `(.venv)` in your terminal prompt.

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

```bash
cp .env.example .env
```

Open `.env` and set your TripleTen sandbox URL:

```
URBAN_ROUTES_URL=https://cnt-YOUR-SANDBOX-ID.containerhub.tripleten-services.com
```

> The sandbox URL changes every sprint. Get the current one from your TripleTen workspace.
> All other values in `.env.example` are pre-filled with sandbox defaults and can be left as-is.

---

## 5. Run the Tests

**Smoke tests only (fast — ~2 min):**
```bash
pytest selenium/ -m smoke
```

**Full test suite:**
```bash
pytest selenium/
```

**Negative / edge case tests only:**
```bash
pytest selenium/ -m negative
```

**Watch tests run in a real browser (disable headless):**
```bash
HEADLESS=false pytest selenium/ -m smoke
```

---

## 6. View the HTML Report

After any test run, open the auto-generated report:

```bash
open reports/test_report.html      # macOS
xdg-open reports/test_report.html  # Linux
start reports/test_report.html     # Windows
```

---

## 7. View Failure Screenshots

If a test fails, a screenshot is saved automatically:

```
screenshots/FAIL_<test_name>_<timestamp>.png
```

---

## Repository Structure

```
TripleTen-QA-projects-ES/
├── config.py                    # All test data and env var loading
├── .env.example                 # Environment variable template — copy to .env
├── pytest.ini                   # pytest configuration and markers
├── requirements.txt             # Python dependencies
├── reports/                     # Auto-generated HTML test reports
├── screenshots/                 # Auto-captured failure screenshots
├── selenium/
│   ├── conftest.py              # Shared fixtures (driver, page, screenshot hook)
│   ├── test_urban_routes.py     # Test cases (happy path + negative)
│   └── pages/
│       └── urban_routes_page.py # Page Object Model — all locators and actions
├── postman/                     # Sprint 4: API test collection
├── sql/                         # Sprint 5: Data integrity queries
├── test-cases/                  # Manual test case documentation
└── .github/
    └── workflows/
        └── tests.yml            # GitHub Actions CI/CD pipeline
```

---

## CI/CD

Every push to `main` triggers the GitHub Actions workflow which:
1. Spins up a headless Chrome on Ubuntu
2. Runs the `smoke` test suite
3. Uploads the HTML report as a downloadable artifact
4. Uploads any failure screenshots if tests fail

To enable CI, add your sandbox credentials as GitHub Secrets:
`Repo → Settings → Secrets and variables → Actions → New repository secret`

| Secret Name | Value |
|-------------|-------|
| `URBAN_ROUTES_URL` | Your sandbox URL |
| `TEST_FROM_ADDRESS` | `East 2nd Street, 601` |
| `TEST_TO_ADDRESS` | `1300 1st St` |
| `TEST_PHONE` | `+12025550199` |
| `TEST_CARD_NUMBER` | `1234 0000 5678` |
| `TEST_CARD_CVV` | `111` |
| `TEST_SMS_CODE` | `000000` |
| `TEST_DRIVER_COMMENT` | `Bring a blanket` |
