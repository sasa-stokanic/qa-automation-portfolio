# Demoblaze Automation Project

This project contains automated UI test scenarios for the Demoblaze web application using Python, Selenium, and PyTest.

The main focus of this project is validating core e-commerce functionality including authentication, cart management, product validation, and cart persistence behavior.

---

# Technologies Used

- Python
- Selenium WebDriver
- PyTest
- ChromeDriver

---

# Test Scenarios Covered

## Login Tests

- Successful login validation
- Invalid username validation

---

## Cart Tests

- Add product to cart
- Remove product from cart
- Cart item matches selected product
- Cart persistence after page refresh

---

# Features Covered

- Positive and negative test scenarios
- Dynamic waits using WebDriverWait
- Browser alert handling
- Cart state validation
- Product data validation
- Cart persistence validation
- Explicit waits for synchronization and stability
- Stable element locators using ID, CSS Selectors, and XPath

---

# Run Tests

Run all Demoblaze tests:

```bash
py -m pytest -v demoblaze/tests
```

Run single test file:

```bash
py -m pytest -v demoblaze/tests/test_cart.py
```

Run single test:

```bash
py -m pytest -v demoblaze/tests/test_login.py::test_login_invalid_username
```

---

# Notes

- Tests use explicit waits instead of time.sleep() for better stability.
- The project focuses on realistic UI automation scenarios commonly used in e-commerce testing.
- The automation suite is designed as part of a freelance QA automation portfolio.