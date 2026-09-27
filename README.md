# E-commerce Test Suite: automationexercise.com

**Selenium + pytest suite covering login, registration, search, product pages, cart and checkout on a live e-commerce practice site, plus a full manual test cycle. Runs in CI on every push.**

[![Tests](https://github.com/sasa-stokanic/qa-automation-portfolio/actions/workflows/main.yml/badge.svg)](https://github.com/sasa-stokanic/qa-automation-portfolio/actions/workflows/main.yml)

**[Latest CI runs](https://github.com/sasa-stokanic/qa-automation-portfolio/actions) · [Manual test cases & bugs](https://docs.google.com/spreadsheets/d/1Kq1odftNSNppfaeaYLiV9xK3bT_BZYt8/edit?usp=sharing)**

---

## What's here

| Part | Stack | Scope |
|---|---|---|
| [`selenium/`](selenium/) | Python 3.11, Selenium, pytest, Page Object Model | 20 automated tests |
| [`manual-testing/`](manual-testing/) | Black-box test cases, bug reports | 26 test cases, 2 bugs |
| [`.github/workflows/`](.github/workflows/) | GitHub Actions, pytest-html | Headless run + HTML report on every push |

**Automated coverage:**

| Module | Tests | What's checked |
|---|:---:|---|
| Login | 4 | Valid/invalid credentials, error messages |
| Registration | 4 | Full sign-up (account created, then deleted), existing email, empty fields |
| Product page | 3 | Name and price on the details page for several products, add to cart |
| Search | 3 | Valid queries, empty results |
| Cart | 5 | Add/remove, multiple products (JS click and real hover + click), quantity and total price |
| Checkout | 1 | Login → product → cart → checkout, name and price must match between cart and checkout |

Every assertion has a message showing expected vs. actual, so a red run is readable without opening the code.

## Manual testing

Alongside the automated suite, I ran a full manual black-box cycle on the same site: 26 test cases and 2 bug reports, written in a standard test case template.

| Module | Test cases | Includes |
|---|:---:|---|
| Login | 10 | Empty fields, leading whitespace, uppercase email, SQL injection, very long input |
| Registration | 5 | Duplicate email, invalid email format, empty required fields, weak password |
| Search | 3 | Existing product, no results, empty search |
| Cart | 5 | Add/remove, quantity update, price × quantity total, persistence after refresh |
| Checkout | 3 | Full purchase to payment confirmation, login required before checkout |

**Bugs found:**

| ID | Summary | Severity |
|---|---|---|
| BUG-001 | Login email field is case-sensitive (uppercase version of a valid email fails) | Low |
| BUG-002 | Registration accepts extremely weak passwords, no minimum strength enforced | Medium |

Full test cases with steps, expected and actual results: [Google Sheets](https://docs.google.com/spreadsheets/d/1Kq1odftNSNppfaeaYLiV9xK3bT_BZYt8/edit?usp=sharing) or the `.xlsx` in [`manual-testing/`](manual-testing/).

## Problems I ran into

1. **Ad overlay intercepting clicks.** A Google Vignette ad kept covering elements and stealing clicks on almost every module. Most page objects click through JavaScript (`execute_script("arguments[0].click();", element)`), which the overlay can't intercept. Before checkout, `close_add_if_present()` waits up to 5 seconds for the ad's dismiss button and closes it, and moves on if no ad shows up. A JS click skips real user interaction, so the cart module also has a test that adds products with a real hover and click, to prove the actual UI path works too.
2. **pytest module-naming collision in CI.** Old Saucedemo and Demoblaze practice folders had test files with the same names as the new ones, and pytest refused to collect them on the runner. I deleted the old folders, since this project replaced them anyway.
3. **Cart items read from the wrong place.** `get_cart_item_names()` used a global CSS selector, so it picked up product names from outside the cart table. I scoped the search to the cart rows (`tbody tr`).
4. **Flaky tests.** Product titles came back with a different number of spaces between runs, so exact string checks failed at random. I normalize the text with `re.sub(r'\s+', ' ', text).strip()` instead of guessing the exact string. The search tests also raced each other, which I fixed with a `wait_for_url()` step before reading results.
5. **Hover-only buttons.** "Add to cart" only appears on CSS hover, so a plain click didn't work. I use ActionChains `move_to_element` to hover first, then do a real click.

## How it runs

- Every push and pull request to `main` triggers the workflow in `.github/workflows/main.yml`.
- The `selenium/conftest.py` fixture checks the `CI` environment variable: visible Chrome locally, headless in CI, no config changes needed.
- Selenium Manager (built into Selenium 4) finds the right ChromeDriver on its own, so the setup is the same on my machine and on the runner.
- The pytest-html report is uploaded as a downloadable artifact on each run.

## Run locally

```bash
git clone https://github.com/sasa-stokanic/qa-automation-portfolio.git
cd qa-automation-portfolio/selenium
pip install -r requirements.txt
pytest tests/ -v --html=report.html --self-contained-html
```

Requires Chrome. The driver downloads automatically on the first run.

## About

**Saša Stokanić**, self-taught QA automation engineer from Serbia. Python, Selenium, pytest, manual testing, CI/CD. Open to freelance and full-time QA work.