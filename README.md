QA Automation Portfolio
QA portfolio combining UI test automation (Python, Selenium, pytest) and manual black-box testing, as I move from self-taught QA into freelance and full-time work.

The project targets automationexercise.com, a public practice site for e-commerce testing, and covers the core flows a real QA engineer would be responsible for: authentication, product discovery, search, cart, and checkout.

Why this project exists
I wanted a project that actually looks like something a QA team would maintain — not a one-off script that clicks a few buttons and calls it done. That meant:

Structuring the code so pages and tests are separated (POM), so a UI change only breaks one file, not twenty
Writing tests that fail with a useful message, not a silent assertion error
Running the suite automatically on every push instead of only on my own machine
Documenting why things are built a certain way, not just what they do
Along the way I ran into (and fixed) real problems: flaky selectors, a scoping bug that only showed up under specific conditions, an ad overlay blocking clicks in headless mode, and a pytest module-naming collision in CI. Those fixes are part of what makes this a genuine engineering exercise rather than a tutorial copy.

Tech stack
Python 3.11
Selenium WebDriver — browser automation
pytest — test runner
pytest-html — HTML test reports
webdriver-manager — automatic ChromeDriver management (no manual driver downloads, works the same locally and in CI)
GitHub Actions — CI/CD pipeline
Project structure
pages/                     # Page Object classes — one per page/component
├── cart_page.py
├── checkout_page.py
├── login_page.py
├── product_page.py
├── register_page.py
└── search_page.py
tests/                      # Test files — one per feature area
├── test_cart.py
├── test_checkout.py
├── test_login.py
├── test_product_page.py
├── test_register.py
└── test_search.py
manual-testing/             # Manual black-box test cases & bug reports
├── QA_Test_Report_Template.xlsx
└── README.md
conftest.py                 # Shared pytest fixtures (WebDriver setup, headless mode for CI)
requirements.txt
.github/workflows/          # CI/CD pipeline definition
└── tests.yml
What's covered
20 automated tests across the core user journey:

Login (4 tests) — valid/invalid credentials, error handling
Registration (4 tests) — including validation on empty required fields
Product page (3 tests) — product details, search-to-detail flow
Search (3 tests) — valid queries, empty results handling
Cart (5 tests) — add/remove items, quantity updates, cart persistence
Checkout (1 capstone test) — full end-to-end flow from cart to order confirmation, tying the other modules together
Every test uses descriptive docstrings and f-string assertion messages, so a failure tells you what was expected vs. what actually happened — not just AssertionError.

Manual testing
Alongside the automated suite, this repo includes a full manual testing cycle on the same site — 26 test cases across 5 modules (login, registration, search, cart, checkout) plus 2 documented bugs, following a standard black-box test case and bug tracking format.

📊 View test cases & bug reports (Google Sheets):(https://docs.google.com/spreadsheets/d/1Kq1odftNSNppfaeaYLiV9xK3bT_BZYt8/edit?gid=678596651#gid=678596651)

See the manual-testing/ folder for full details.

CI/CD
Every push to main triggers a GitHub Actions workflow that:

Sets up Python 3.11 and installs dependencies from requirements.txt
Installs Chrome on the runner
Runs the full test suite in headless mode (the conftest.py fixture detects the CI environment variable and switches from a visible browser locally to headless in CI automatically)
Generates a self-contained HTML report via pytest-html
Uploads that report as a downloadable artifact on the workflow run
You can check the latest run status under the Actions tab of this repo.

Running it locally
git clone https://github.com/sasa-stokanic/qa-automation-portfolio.git
cd qa-automation-portfolio
pip install -r requirements.txt
pytest tests/ --html=report.html --self-contained-html
Chrome and a matching driver are required locally — webdriver-manager handles the driver download automatically the first time you run the suite.

About me
I'm a self-taught QA automation engineer based in Serbia, building toward freelance and full-time QA/automation work. This project is a working example of how I approach testing: structured, documented, and built to survive contact with a real CI pipeline — not just to run once on my laptop.

Feel free to look through the commit history — it reflects the actual process of building this, bugs and fixes included
