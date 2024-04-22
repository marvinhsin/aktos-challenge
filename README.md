# Aktos Full Stack Django App Challenge

## Demo
https://www.loom.com/share/79805951d2a14b089fbec08471d1fae9?sid=ac483088-34b9-48fa-96b8-ccced47f29bb

## Background

This Django application is designed to facilitate a collection agency's workflow by allowing them to ingest data files provided by their clients. The data files are in CSV format and contain account information regarding consumers and the debts they owe to a single client.

**Client**: An organization that hires a collection agency to collect debt on their behalf. A collection agency can work with multiple clients to collect debts.

**Consumers**: Individuals or entities that owe debt.

**Debt**: The amount owed by one or more consumers.

Assuming all consumers belong to the same collection agency and client, this system handles the ingestion and retrieval of data efficiently.

## Design

The application features a simple UI on the homepage with a button for uploading CSV files. Upon clicking the button, the system invokes an API (`load_csv`) to read through the rows of the CSV file, performing input sanitization, and storing the data in the database. 

After ingestion, the system provides APIs for querying account information from the database. Examples include:

1. `GET /accounts?min_balance=100&max_balance=1000&status=in_collection`
2. `GET /accounts?min_balance=100.23&status=collected&consumer_name=john`

Upon querying the database, the system renders a view containing the queried objects, which are paginated for easy navigation. Each model in the application is thoroughly tested to ensure reliability and accuracy.

## Potential Improvement

1. UI design can be improved with React for better experience.
2. Columns can be indexed for faster lookup performance.

## Usage

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Configure the database settings in `settings.py`.
4. Run migrations using `python manage.py migrate`.
5. Start the server with `python manage.py runserver`.
6. Access the application in your web browser at `http://localhost:8000`.

## Technologies Used

- Django
- Django REST Framework
- HTML/CSS (for UI)
- SQLite (for database)
