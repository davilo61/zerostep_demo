# SauceDemo Playwright Test

An automated test suite that uses the ZeroStep AI agent on the SauceDemo sample e-commerce website using Playwright.

## Features

- End-to-end testing of the SauceDemo website
- Credentials management using environment variables
- Complete user journey testing:
  - Login
  - Product selection
  - Cart management
  - Checkout process
  - Order completion verification
  - Return to home page

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. Clone this repository:
   ```
   git clone [your-repository-url]
   cd saucedemo-tests
   ```

2. Install required dependencies:
   ```
   pip install playwright python-dotenv
   playwright install
   ```

3. Create a `.env` file in the project root:
   ```
   # SauceDemo Credentials
   SAUCE_USERNAME=standard_user
   SAUCE_PASSWORD=secret_sauce
   
   # Optional test configuration
   HEADLESS=false
   SLOW_MO=0
   ```

## Usage

Run the test script:
```
python saucedemo_test.py
```

For debugging with more verbose output:
```
# Windows
set PWDEBUG=1
python saucedemo_test.py

# macOS/Linux
PWDEBUG=1 python saucedemo_test.py
```

## Test Steps

The automated test performs the following actions:

1. Navigates to saucedemo.com
2. Logs in with credentials from .env file
3. Verifies successful login
4. Adds "Sauce Labs Backpack" to the cart
5. Verifies the item is in the cart
6. Proceeds to checkout
7. Completes checkout form with test data
8. Verifies order completion and confirmation messages
9. Returns to home page
10. Verifies successful return to product listing

## Project Structure

```
saucedemo-tests/
├── .env                  # Environment variables (not in version control)
├── .gitignore            # Git ignore file
├── README.md             # This file
└── saucedemo_test.py     # Main test script
```

## Git Setup

To initialize this as a new Git repository while excluding sensitive files:

1. Initialize a new Git repository:
   ```
   git init
   ```

2. Create a `.gitignore` file:
   ```
   echo ".env" > .gitignore
   ```

3. Stage and commit your files:
   ```
   git add .
   git commit -m "Initial commit: Add SauceDemo test with Playwright"
   ```

4. Connect to your remote repository (optional):
   ```
   git remote add origin [your-repository-url]
   git push -u origin main
   ```

## License

[Your chosen license]

## Author

[Your Name]
