# Financial Accounting Service

A **Django-based financial accounting service** for managing personal finances. This application allows users to track their income and expenses, view reports, and create budgets. The project is structured with a focus on backend architecture, without a frontend.

## Features

- Manage income and expenses.
- Create and manage budgets.
- View financial reports.
- Admin panel for managing users, transactions, and budgets.

## Table of Contents

1. [Installation](#installation)
2. [Project Structure](#project-structure)
3. [Setup](#setup)
4. [Admin Panel](#admin-panel)
5. [Backend-Only Structure](#backend-only-structure)
6. [Models](#models)
7. [License](#license)

## Installation

To set up this project locally, follow these steps:

### 1. Clone the repository:

```bash
git clone https://github.com/Rocowoco/financial-accounting.git

```
### 2. Navigate to the project directory:

```bash
cd financial-accounting
```

### 3. Set up a virtual environment:
For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
For MacOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies:

```bash
pip install -r requirements.txt
```

### 5. Install Pillow (required for handling image fields):

```bash
pip install Pillow
```

## Project Structure

Here is the project structure:

```plaintext
financial-accounting/
│
├── apps/
│   ├── budgets/         # Managing budgets: setting limits by categories and periods
│   ├── categories/      # Managing categories for transactions and budgets
│   ├── reports/         # Managing reports: graphs, charts and statistics on income and expenses
│   ├── transactions/    # Managing income and expenses: adding, editing and deleting transactions
│   ├── users/           # Managing users: registration, authentication, profile editing
│   └── usettings/       # Managing user settings: currency selection, language, date format
│
├── finaccounting/       # Main Django project configuration
├── templates/           # HTML-files for apps
│
├── .gitignore           # List of files and directories ignored by git
├── manage.py            # Django's command-line utility for administrative tasks
├── requirements.txt     # Python dependencies required by the project
├── README.md            # Guide for devs, explaining what the project is and how to set it up
└── venv/                # Virtual environment (not committed to version control)
```
## Setup

### 1. Migrate the database:

```bash
python manage.py makemigrations
python manage.py migrate
```