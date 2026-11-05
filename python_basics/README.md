# QA Automation Practice: Sauce Demo & Restful Booker

Test automation project created while learning QA Automation with Python.

## What is tested
- **UI tests** for [Sauce Demo](https://www.saucedemo.com): login (positive and negative cases), adding products to the cart
- **API tests** for [Restful Booker](https://restful-booker.herokuapp.com): getting, creating and checking bookings, negative case (404)

## Tech stack
- Python
- pytest
- Playwright
- requests
- Page Object Model
- GitHub Actions (CI)

## Project structure
- `../pages` – Page Objects (locators and actions for each page)
- `tests` – UI and API tests
- `../.github/workflows` – CI configuration

## How to run
1. Install dependencies:
   `pip install pytest pytest-playwright requests pytest-html`
2. Install the browser:
   `python -m playwright install chromium`
3. Run the tests:
   `pytest tests -v`
4. Run with an HTML report:
   `pytest tests --html=report.html --self-contained-html`