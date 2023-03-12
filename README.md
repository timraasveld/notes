# Development environment setup

First, make sure you meet the requirements:
- Python 3 installed and configured as the default `python` command

Then, clone the repo, install dependencies, migrate the database and set up two admin accounts:

```bash
git clone https://github.com/timraasveld/notes.git
cd notes
pip install -r requirements.txt
python3 manage.py migrate --run-syncdb
# Use the insecure password "admin" for both accounts to be able to use the Postman collection as-is
python manage.py createsuperuser --email admin@example.com --username admin
python manage.py createsuperuser --email admin@example.com --username admin2
```

# Run server
```bash
python manage.py runserver
```

# Postman
To use the postman collection provided in `notes.postman_collection.json`, click "import" and point it to the JSON file.

To test the endpoints, first run the task `Log in as admin` (or admin2)

In subsequent requests, a JWT token of the last used user will be automatically added to the Authorization header.

# TODO before going to production

- Use a proper DB, i.e. MySQL or Postgres
- Replace hardcoded SECRET_KEY and DEBUG in settings.py with environment variables (or another secure secret mechanism)