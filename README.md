# UI Test Automation Portfolio

This repository contains my UI automation testing portfolio built with Python, Selenium, and PyTest.

The portfolio includes automated end-to-end test scenarios for two different web applications with focus on:

- UI automation
- Functional testing
- Cart and checkout validation
- Login scenarios
- Dynamic waits and synchronization
- Data validation
- Sorting functionality
- Alert handling

---

# Technologies Used

- Python
- Selenium WebDriver
- PyTest
- ChromeDriver

---

# Projects

## SauceDemo Automation

Automation test suite for SauceDemo covering:

- Login functionality
- Cart functionality
- Checkout process
- Product sorting
- Item data validation
- Subtotal calculation validation

Project Folder: `saucedemo/`

---

## Demoblaze Automation

Automation test suite for Demoblaze covering:

- Positive login scenario
- Negative login scenario
- Add to cart functionality
- Remove from cart functionality
- Cart persistence after refresh
- Browser alert handling

Project Folder: `demoblaze/`

---

# Features Covered

- Positive and negative test scenarios
- End-to-end checkout testing
- Cart item validation
- Dynamic waits using WebDriverWait
- UI data verification
- Sorting validation
- Alert handling
- Stable element locators using ID, CSS Selectors, and XPath strategies

---

# How To Run Tests

Run all tests:

```bash
py -m pytest -v
```

Run SauceDemo tests:

```bash
py -m pytest -v saucedemo
```

Run Demoblaze tests:

```bash
py -m pytest -v demoblaze
```

Run single test file:

```bash
py -m pytest -v saucedemo/tests/test_checkout.py
```

## Demo Videos

### SauceDemo Automation Run
[Watch Video](https://www.youtube.com/watch?v=Oy0J243p7yw)

### Demoblaze Automation Run
[Watch Video](https://www.youtube.com/watch?v=KQ_Odnk9aYY)