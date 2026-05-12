# AdNabu QA Automation Assignment

## Overview

This project is part of the QA Engineer assignment for AdNabu.

The automation covers the following user flow:

- Search for a product
- Add the product to the cart successfully

The project is implemented using:

- Python
- Selenium WebDriver
- Pytest
- Explicit Waits
- Lightweight Page Object Model (POM)

---

# Assignment Scope

## Task 1 — Manual Testing

Manual test cases were created for:

- Product Search
- Add to Cart

The test cases include:

- Positive scenarios
- Negative scenarios
- Edge cases

---

## Task 2 — Test Automation

Automated scenario:

- Search for a product and add it to the cart successfully

Automation requirements covered:

- Python + Selenium implementation
- Explicit waits used (No hardcoded sleeps)
- Readable and modular code structure

---

# Project Structure

```bash
adnabu-qa-assignment/
│
├── pages/
│   ├── home_page.py
│   └── product_page.py
│
├── tests/
│   └── test_add_to_cart.py
│
├── utils/
│   └── driver_setup.py
│
├── reports/
│   └── report.html
│
├── TEST_CASES.md
├── requirements.txt
├── README.md
└── pytest.ini
```

### Folder Details

- `pages/` → Contains Page Object Model (POM) classes
- `tests/` → Contains automated test scripts
- `utils/` → Contains driver setup and reusable utilities
- `reports/` → Contains generated HTML test reports
- `TEST_CASES.md` → Contains manual test cases for Task 1

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# How to Run the Tests

## Run Test Suite

```bash
pytest -v
```

## Generate HTML Report

```bash
pytest --html=reports/report.html
```

---

# Design Decisions

The following design decisions were implemented to keep the framework clean, maintainable, and stable:

- Explicit waits used instead of hardcoded sleeps
- Lightweight Page Object Model implemented for modularity
- webdriver-manager used for automatic driver management
- Modular and readable code structure maintained
- Assertions added for validation of key user actions

---

# Deliverables Included

- Manual test cases
- Selenium automation script
- HTML execution report
- README with setup and execution instructions
