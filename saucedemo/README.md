# SauceDemo Automation Project

This project contains automated UI test scenarios for the SauceDemo web application using Python, Selenium, and PyTest.

The main focus of this project is validating core e-commerce functionality including authentication, cart management, checkout flow, sorting functionality, and UI data validation.

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
- Invalid password validation

---

## Cart Tests

- Cart badge matches added products
- Cart item data matches inventory item
- Remove specific item from cart
- Remove all items from cart and validate badge removal

---

## Checkout Tests

- Checkout validation for required fields
- Checkout overview subtotal validation
- Complete order flow validation

---

## Sorting Tests

- Products are sorted correctly from low to high price

---

# Features Covered

- Positive and negative test scenarios
- End-to-end checkout testing
- Cart item validation
- Cart badge validation
- Product price and subtotal verification
- Sorting validation
- Dynamic waits using WebDriverWait
- Explicit waits for synchronization and stability
- Stable element locators using ID, CSS Selectors, and data-test attributes

---

# Run Tests

Run all SauceDemo tests:

```bash
py -m pytest -v saucedemo/tests
```

Run single test file:

```bash
py -m pytest -v saucedemo/tests/test_checkout.py
```

Run single test:

```bash
py -m pytest -v saucedemo/tests/test_cart.py::test_remove_item_from_cart_page
```

---

# Notes

- Tests use explicit waits instead of time.sleep() for better stability.
- The project focuses on realistic UI automation scenarios commonly used in e-commerce testing.
- The automation suite is designed as part of a freelance QA automation portfolio.