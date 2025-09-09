# Selenium Pytest POM Framework
# Features

- Page Object Model (POM) implemented for maintainable tests
- JSON-driven locators and test data
- Centralized configuration using `config.ini` and `config_reader.py`
- Timestamped logs and HTML reports per test run
- Supports multiple browsers via CLI (`--browser_name Chrome|Edge|Firefox`)
- Pytest fixtures for setup, logger, and WebDriver
- Fully automated end-to-end test flows for:
  - Login / Forgot Password
  - Product Search / Checkout / Orders
  - Practice Page interactions
  - Mobile shop checkout

## Usage

1. Install dependencies
pip install -r requirements.txt

2. Run tests with default Chrome
pytest

3. Run tests on a specific browser
pytest --browser_name Firefox

4. Logs and HTML reports
   Logs and reports are stored in Reports/<timestamp>/
   HTML report file: report.html
   Logger file: logs/test.log inside timestamped folder
   
5. Configurable URLs and credentials
   Update config/config.ini to add URLs, timeouts, or credentials
   Use ConfigReader in tests or POM classes

6. Add more URLs, credentials, or timeouts in config.ini as needed
