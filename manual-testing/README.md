# Manual Testing — Automation Exercise

Manual QA testing project performed on [automationexercise.com](https://automationexercise.com), a public demo e-commerce site built for practicing manual and automated testing.

## Overview

This project documents a full manual test cycle across the core user flows of an e-commerce site — login, registration, search, cart, and checkout — using a standard test case and bug tracking format.

**26 test cases** across **5 modules**, plus **2 documented bugs** found during testing.

| Module | Test Cases | Coverage |
|---|---|---|
| Login | 10 | Happy path, invalid credentials, empty fields, whitespace handling, case sensitivity, SQL injection, oversized input |
| Registration | 5 | Happy path, duplicate email, invalid email format, empty fields, weak password |
| Search | 3 | Existing product, no results, empty search field |
| Cart | 5 | Add, remove, update quantity, total price calculation, persistence after refresh |
| Checkout | 3 | Full checkout and payment flow, login requirement |

## Approach

Test cases follow a black-box testing convention: **Expected Result** describes the general/functional outcome a tester would reasonably expect *before* running the test, while **Actual Result** captures the exact behavior and messages observed *during* testing. This mirrors how a tester without access to the system's source code would realistically document a test — expectations set in advance, results confirmed afterward.

Beyond standard happy-path and validation checks, the login module includes a couple of edge cases often overlooked in junior-level testing:

- Leading whitespace in the email field
- Case sensitivity of the email field
- Basic SQL injection resistance check
- Handling of an extremely long input string

## Bugs Found

| ID | Related Test | Description | Severity |
|---|---|---|---|
| BUG-001 | TC-008 | Login is case-sensitive on the email field, deviating from standard practice (emails should be case-insensitive) | Low |
| BUG-002 | TC-015 | Registration accepts extremely weak/short passwords with no minimum strength requirement enforced | Medium |

Full details, steps to reproduce, and expected/actual behavior are documented in the Bug Reports sheet.

## Files

- `QA_Test_Report_Template.xlsx` — full test case suite and bug reports (3 sheets: Test Cases, Bug Reports, Summary)

## Tools

Google Sheets / Excel, manual black-box testing, no automation involved in this project.
