# 🚀 URL Shortener API

This is a fast and simple URL Shortener API built with FastAPI and SQLAlchemy. It uses Base62 encoding to generate short, unique codes for long URLs and includes automatic cleanup for expired links.

📋 Prerequisites

To run this project, you need:

Python 3.9+

A PostgreSQL, SQLite, or other SQLAlchemy-compatible database.

⚙️ Setup and Installation

Follow these steps to get your development environment set up.

1. Clone the Repository (Assuming this is a project)

Bash

git clone <repository_url>
cd url-shortener-api
2. Create and Activate a Virtual Environment

Bash

python -m venv venv
source venv/bin/activate  # On Linux/macOS
# .\venv\Scripts\activate  # On Windows
3. Install Dependencies

You will need to install fastapi, uvicorn, sqlalchemy, alembic, python-dotenv, and validators.

Bash

pip install fastapi uvicorn sqlalchemy alembic python-dotenv pydantic validators psycopg2-binary # Use a database driver appropriate for your DB
4. Configure Environment Variables

Create a file named .env in the root directory of the project. This is used by config.py to load configuration values.

# .env file content
DATABASE_URL="sqlite:///./shortener.db"
# Example for PostgreSQL: postgresql+psycopg2://user:password@host:port/dbname

# Time-To-Live for URLs in minutes (1440 minutes = 24 hours)
APP_TTL_MINUTES=1440
5. Run Database Migrations (Alembic)

The project uses Alembic for database migrations.

Make sure your DATABASE_URL is set correctly in .env.

Initialize the database schema:

Bash

alembic upgrade head
This will create the urls table in your database, which includes columns for id, original_url, short_code, and created_at.

6. Run the Application

Start the FastAPI application using Uvicorn:

Bash

uvicorn main:app --reload
The API will now be running, typically at http://127.0.0.1:8000.

💻 API Endpoints

The API is structured around two main functionalities: creating new short links and redirecting from a short link to the original URL.

Method	Endpoint	Description	Status Code	Dependencies
POST	/urls	Creates a new short URL.	201 Created	URLService.create_short_url
GET	/u/{short_code}	Redirects to the original URL.	302 Found	URLService.get_original_url
GET	/urls	Retrieves a list of all existing URLs.	200 OK	URLService.get_all_urls
DELETE	/urls/{short_code}	Deletes a specific URL by its short code.	204 No Content	URLService.delete_url
💡 Core Functionality Highlights

1. Short Code Generation

The system uses the database primary key (id) and encodes it into a shorter Base62 string using the alphabet: 0-9a-zA-Z.

Process:

A new URL record is created with a temporary short_code.

The auto-generated id is retrieved.

The id is encoded into the final short_code using encode_base62.

The record is updated and committed.

2. URL Validation

All incoming URLs are validated using the validators.url function before creation. If the URL is invalid, an HTTPException with status code 400 is raised.

3. Automatic Expiration (Cleanup Command)

The URLRepository includes a method, delete_expired, which calculates the expiration time based on APP_TTL_MINUTES from the configuration and deletes records where created_at is older than this time. This is typically run via a scheduled task (e.g., a background job or cron job, as suggested by the import in main.py: from commands.cleanup import scheduler).

$$\text{Expiration Time} = \text{Current Time} - \text{timedelta}(\text{minutes}=\text{APP\_TTL\_MINUTES})$$
📚 Project Structure (Conceptual)

The project follows a Service/Repository pattern to separate business logic from data access.

main.py: The entry point for the FastAPI application.

config.py: Loads environment variables from .env.

url_router.py: Defines API endpoints and dependency injection for the database session and service.

services/url_service.py: Contains the core business logic (create, get original, delete).

repositories/url_repository.py: Handles direct database operations (CRUD, deletion of expired URLs).

models/url.py: SQLAlchemy declarative base model for the URL table.

utils.py: Contains the Base62 encoding and URL validation utility functions.

schemas/url_schema.py: Pydantic models for request/response validation and structure.


