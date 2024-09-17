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

### 2. Create a superuser:
To access the Django admin interface, create a superuser account:

```bash
python manage.py createsuperuser
```
Follow the prompts to set up the superuser credentials.

### 3. Run the development server:
Start the Django development server:

```bash
python manage.py runserver
```
Visit http://127.0.0.1:8000/ to view the app locally and http://127.0.0.1:8000/admin/ to access the admin panel.

## Admin Panel

To manage transactions, budgets, and user settings, log into the admin panel using the superuser account you created.

```plaintext
http://127.0.0.1:8000/admin/
```
Admin Features:
- Manage transactions: Add, edit, or delete income and expense transactions.
- Manage budgets: Create and manage personal budgets.
- Manage users: Edit user details, set permissions, and assign avatars.


## Backend-Only Structure

This project focuses solely on the backend, with the architecture designed to manage personal finance data efficiently. It doesn't include any frontend code, but it’s structured in a way that makes it easy to extend with APIs or a web-based user interface in the future.

Key points about this structure:
- **Backend-focused:** All interactions happen through Django views, models, and the admin panel.
- **Extensible:** You can easily integrate a REST API or a frontend framework like Vue or React if needed.
- **Modular:** Each major feature (transactions, budgets, categories) is its own Django app, making it easier to maintain and expand.


## Models

### 1. Transaction (apps.transactions.models.Transaction):

Represents individual financial transactions (income/expenses).
Fields:
- user: Foreign key to the CustomUser model, linking the transaction to a user.
- category: Foreign key to the Category model. Null if the category is deleted.
- amount: Decimal field for the transaction amount, up to 10 digits with 2 decimal places.
- description: Optional text description of the transaction.
- transaction_type: CharField to specify whether it's an income or expense.
- date: Date when the transaction occurred.

### 2. Budget (apps.budgets.models.Budget):

Used to manage personal budgets.

### 3. Category (apps.categories.models.Category):

Categories for organizing financial transactions.

### 4. CustomUser (apps.users.models.CustomUser):

To manage user-specific data, such as avatars, groups, permissions.

### 5. Report (apps.reports.models.Report):

To manage reports: graphs, charts and statistics on income and expenses.

### 6. UserSettings (apps.usettings.models.UserSettings):

To manage user settings: currency selection, lang, date format.