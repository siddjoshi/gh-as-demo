# Expense Tracker

This is a simple web application for tracking expenses. It allows users to add and delete expenses, and view a list of all expenses. This application is a demo app to showcase GitHub Advanced Security capabilities such as Dependabot alerts, CodeQL scanning, and auto-fix.

## Features

- Add new expenses with an amount and description.
- Delete expenses by index.
- View a list of all expenses.

## Requirements

- Python 3.x
- Flask

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/expense-tracker.git
    cd expense-tracker
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    venv\Scripts\activate  # On Windows
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```sh
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/`.

## Routes

- `/` - Home page, displays the list of expenses.
- `/add` - Add a new expense (POST method).
- `/delete/<int:index>` - Delete an expense by its index.

## Example

To add an expense, fill out the form on the home page with the amount and description, then click "Add Expense". To delete an expense, click the "Delete" button next to the expense you want to remove.

## GitHub Advanced Security

This project demonstrates the following GitHub Advanced Security features:

### Dependabot

Dependabot alerts and updates are configured to automatically check for vulnerabilities in dependencies.

- Configuration file: `.github/dependabot.yml`

### CodeQL Analysis

CodeQL scanning is set up to analyze the code for security vulnerabilities.

- Workflow file: `.github/workflows/codeql-analysis.yml`

### Security Policy

A security policy is provided to guide users on how to report vulnerabilities.

- Security policy file: `SECURITY.md`

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgements

- Flask documentation: https://flask.palletsprojects.com/
- Bootstrap for styling: https://getbootstrap.com/# Expense Tracker

This is a simple web application for tracking expenses. It allows users to add and delete expenses, and view a list of all expenses. This application is a demo app to showcase GitHub Advanced Security capabilities such as Dependabot alerts, CodeQL scanning, and auto-fix.

## Features

- Add new expenses with an amount and description.
- Delete expenses by index.
- View a list of all expenses.

## Requirements

- Python 3.x
- Flask

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/expense-tracker.git
    cd expense-tracker
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    venv\Scripts\activate  # On Windows
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```sh
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/`.

## Routes

- `/` - Home page, displays the list of expenses.
- `/add` - Add a new expense (POST method).
- `/delete/<int:index>` - Delete an expense by its index.

## Example

To add an expense, fill out the form on the home page with the amount and description, then click "Add Expense". To delete an expense, click the "Delete" button next to the expense you want to remove.

## GitHub Advanced Security

This project demonstrates the following GitHub Advanced Security features:

### Dependabot

Dependabot alerts and updates are configured to automatically check for vulnerabilities in dependencies.

- Configuration file: `.github/dependabot.yml`

### CodeQL Analysis

CodeQL scanning is set up to analyze the code for security vulnerabilities.

- Workflow file: `.github/workflows/codeql-analysis.yml`

### Security Policy

A security policy is provided to guide users on how to report vulnerabilities.

- Security policy file: `SECURITY.md`

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgements

- Flask documentation: https://flask.palletsprojects.com/
- Bootstrap for styling: https://getbootstrap.com/