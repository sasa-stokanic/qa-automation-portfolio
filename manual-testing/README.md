# Manual Testing: automationexercise.com

**Full manual black-box test cycle on [automationexercise.com](https://automationexercise.com), a public demo e-commerce site: 26 test cases across 5 modules and 2 documented bugs.**

**[Test cases & bug reports (Google Sheets)](https://docs.google.com/spreadsheets/d/1Kq1odftNSNppfaeaYLiV9xK3bT_BZYt8/edit?usp=sharing) · [Automated Selenium suite](../selenium/) · [Back to main README](../README.md)**

---

## Coverage

| Module | Test cases | What's covered |
|---|:---:|---|
| Login | 10 | Happy path, invalid credentials, empty fields, leading whitespace, uppercase email, SQL injection, very long input |
| Registration | 5 | Happy path, duplicate email, invalid email format, empty fields, weak password |
| Search | 3 | Existing product, no results, empty search |
| Cart | 5 | Add, remove, update quantity, total price, persistence after refresh |
| Checkout | 3 | Full checkout and payment, login required before checkout |

## Bugs found

| ID | Related test | Description | Severity |
|---|---|---|---|
| BUG-001 | TC-008 | Login email field is case-sensitive. A valid email typed in uppercase is rejected, while email addresses are normally case-insensitive. | Low |
| BUG-002 | TC-015 | Registration accepts extremely weak passwords (e.g. `1`). No minimum length or strength is enforced. | Medium |

Steps to reproduce and expected vs. actual behavior for each bug are in the **Bug Reports** sheet.

## How I wrote the test cases

I used a black-box approach: I wrote the **Expected Result** before running each test, based on what a user would reasonably expect, and filled in the **Actual Result** afterward with the exact behavior and messages I saw. That's how a tester without access to the source code would work.

Besides the usual happy paths and validation checks, I added a few edge cases to the login form: leading whitespace, an uppercase email, a basic SQL injection string, and a 500+ character input. The uppercase check is where BUG-001 turned up.

## Files

- `QA_Test_Report_Template.xlsx`: the full suite in 3 sheets (Test Cases, Bug Reports, Summary). Same content as the Google Sheets link above.

## Tools

Google Sheets / Excel, manual black-box testing.