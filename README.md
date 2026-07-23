# my-shop

A Django ERP framework example project with sales, purchase, expense, and reporting modules.

---

## First-time setup

Follow these steps once when you first get the project.

### 1. Install Python

Download and install **Python 3.11 or newer** from https://www.python.org/downloads/.

**Important:** during installation, check the box **"Add Python to PATH"** at the bottom of the installer. If you miss this, uninstall and reinstall.

Verify it worked:

```powershell
python --version
```

You should see something like `Python 3.11.9`.

If you see `Python was not found`, reinstall Python and check "Add Python to PATH".

### 2. Install Git

Download from https://git-scm.com/downloads and install with default options.

Verify:

```powershell
git --version
```

### 3. Get the project files

Open **PowerShell** (press `Win` key, type `powershell`, press Enter).

```powershell
cd C:\kb\sales
git clone <your-repo-url>
cd my-shop
```

If you already have the folder, skip `git clone` and just:

```powershell
cd C:\kb\sales\my-shop
```

### 4. Create a virtual environment

A virtual environment isolates this project's packages from the rest of your system.

```powershell
python -m venv .venv
```

This creates a folder named `.venv` inside the project. You only need to do this once.

### 5. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

After activation, your prompt changes to show `(.venv)` at the beginning:

```
(.venv) C:\kb\sales\my-shop>
```

**If you get a security error:** PowerShell blocks script execution by default. Run this once:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then run the activation command again.

### 6. Upgrade pip

```powershell
python -m pip install --upgrade pip
```

### 7. Install project dependencies

```powershell
pip install -r requirements.txt
```

This installs all required packages. Two of them (`django-erp-framework` and `django-slick-reporting`) are pulled directly from GitHub as editable installs, so this may take 2–3 minutes.

If the install fails:

- Make sure your virtual environment is activated (you see `(.venv)` in the prompt).
- Make sure Git is installed (`git --version`).
- Check your internet connection.

### 8. Run database migrations

```powershell
python manage.py migrate
```

This creates the SQLite database file (`db.sqlite3`) and sets up all the tables.

Expected output:

```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, expense, ...
Running migrations:
  Applying ... OK
```

If you see `No migrations to apply`, that is also fine — it means the database is already up to date.

### 9. Load sample data (optional but recommended)

```powershell
python manage.py create_entries
python manage.py create_purchase_entries
```

This populates the database with demo products, sales, purchases, and expenses so the dashboard has data to display.

### 10. Create an admin user

```powershell
python manage.py createsuperuser
```

You will be prompted for:

- **Username:** (e.g., `admin`)
- **Email address:** (can be blank, just press Enter)
- **Password:** (characters won't show as you type)

Confirm the password and you should see `Superuser created successfully.`

### 11. Collect static files (required once)

Jazzmin (the admin theme) needs static files collected into one place.

```powershell
python manage.py collectstatic
```

When asked `Are you sure you want to do this?`, type `yes` and press Enter.

### 12. Start the development server

```powershell
python manage.py runserver
```

You should see:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
Django version 4.2.30, using settings 'my_shop.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### 13. Open the app

Open your web browser and go to:

**http://127.0.0.1:8000/**

Log in with the username and password you created in step 10.

---

## Subsequent Runs (Second Time and Beyond)

After completing the initial setup, use the following steps to run the project locally.

### 1. Open PowerShell

Open PowerShell on your computer.

### 2. Navigate to the project folder

```powershell
cd C:\kb\sales\my-shop
```

### 3. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

You should see `(.venv)` at the beginning of the terminal line.

### 4. Start the Django server

```powershell
python manage.py runserver
```

### 5. Open the application

Open your browser and visit:

```
http://127.0.0.1:8000/
```

### 6. Stop the server

To stop the server, press:

```
Ctrl + C
```

in the PowerShell window.

---

## Project structure

```
my-shop/
├── .venv/                  # Virtual environment (do not touch)
├── expense/                # Expenses app
├── general_reports/        # Profitability reports app
├── my_shop/                # Project settings and URLs
│   ├── settings.py
│   ├── urls.py
│   └── middleware.py
├── purchase/               # Purchases app
├── request_analytics/      # Request analytics dashboard
├── sales/                  # Sales app (clients, products, sales)
├── templates/              # Custom templates
│   ├── admin/
│   │   └── custom_index.html
│   ├── request_analytics/
│   └── front_end_dashboard.html
├── manage.py               # Django CLI entry point
├── requirements.txt        # Python dependencies
├── db.sqlite3              # SQLite database (created by migrate)
└── collected_static/       # Collected static files (created by collectstatic)
```

---

## Useful commands

| Action | Command |
|---|---|
| Check for Django system issues | `python manage.py check` |
| Create new migrations | `python manage.py makemigrations` |
| Open Django shell | `python manage.py shell` |
| View all registered URLs | `python manage.py show_urls` |
| List installed packages | `pip list` |
| Deactivate virtual env | `deactivate` |
| Delete database and start fresh | `del db.sqlite3` then `python manage.py migrate` |
