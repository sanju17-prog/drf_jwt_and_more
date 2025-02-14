# Student Management System with Django and JWT Authentication

This project is a simple Student Management System built using Django and Django REST Framework. It includes JWT (JSON Web Token) authentication for securing the API endpoints, along with features like CRUD operations, request throttling, filtering, database seeding, and pagination.

## Features

- **JWT Authentication:** Secure user authentication using JSON Web Tokens.
- **CRUD Operations:** Implement Create, Read, Update, and Delete operations for managing students.
- **Request Throttling:** Prevent abuse by limiting the rate of API requests.
- **Filtering:** Use django-filter, search-filter, and order-filter to filter, search and order querysets based on specified criteria.
- **Database Seeding:** Populate the database with fake data using Faker.
- **Pagination:** Efficiently manage large datasets by implementing pagination in API responses.

## Installation

Follow these steps to set up the project on your local machine.

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Steps

1. **Clone the repository**

```bash
git clone https://github.com/your-username/student-management-system.git
cd student-management-system
```

2. **Create a virutal environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Apply migrations**

```bash
python manage.py migrate
```

5. **Create a superuser**

```bash
python manage.py createsuperuser
```

6. **Run the development server**

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`.

## Usage

## Accessing APIs using HTTPie

HTTPie is a command-line HTTP client that makes it easy to interact with APIs. Below are some examples of how to use HTTPie to access the APIs in this project.

## JWT Authentication

The project uses JSON Web Tokens (JWT) for authentication. Here's how it works:
- **Access Token:** Used to authenticate requests to the API. It has a short lifespan for security reasons.
- **Refresh Token:** Used to obtain a new access token once it expires. It has a longer lifespan.

### Obtain JWT Token

First, you need to obtain a JWT token by logging in with your superuser credentials.

```bash
http POST http://127.0.0.1:8000/token/ username=your-username password=your-password
```

You will receive a response with an access token and a refresh token.

## Accessing Student API

Use the access token to authenticate your requests to the Student API.

#### List all students

```bash
http GET http://127.0.0.1:8000/student/ "Authorization: Bearer your-access-token"
```

#### Create a new student

```bash
http POST http://127.0.0.1:8000/student/ name=JohnDoe age=20 roll=101 city=NewYork "Authorization: Bearer your-access-token"
```

#### Retrieve a student

```bash
http GET http://127.0.0.1:8000/student/1/ "Authorization: Bearer your-access-token"
```

#### Update a student

```bash
http PUT http://127.0.0.1:8000/student/1/ name=JaneDoe age=21 roll=102 city=LosAngeles "Authorization: Bearer your-access-token"
```

#### Delete a student

```bash
http DELETE http://127.0.0.1:8000/student/1/ "Authorization: Bearer your-access-token"
```

## Project Structure

```bash
project_root/
├── db.sqlite3                       # SQLite database file.
├── manage.py                        # Entry point for managing the Django project.
├── README.md                        # Project documentation and instructions.
├── requirements.txt                # List of project dependencies.
├── jwt_and_more/
│   ├── __pycache__/                 # Compiled Python files (cache).
│   ├── __init__.py                  # Initialization file for the package.
│   ├── asgi.py                      # ASGI configuration for asynchronous applications.
│   ├── settings.py                  # Project settings and configurations.
│   ├── urls.py                      # URL routing for the project.
│   └── wsgi.py                      # WSGI configuration for web server integration.
├── jwt_auth/
│   ├── __pycache__/                 # Compiled Python files (cache).
│   ├── migrations/                  # Database migration scripts for schema changes.
│   ├── __init__.py                  # Initialization file for the package.
│   ├── admin.py                     # Admin-related configurations and settings.
│   ├── apps.py                      # Application configuration settings.
│   ├── models.py                    # Database models for JWT authentication.
│   ├── serializers.py               # Serializers for converting complex data types to/from JSON.
│   ├── tests.py                     # Unit tests for the JWT authentication module.
│   ├── urls.py                      # URL routing for JWT authentication endpoints.
│   └── views.py                     # Views handling JWT authentication logic.
└── drf_throttling/
    ├── __pycache__/                 # Compiled Python files (cache).
    ├── migrations/                  # Database migration scripts for schema changes.
    ├── __init__.py                  # Initialization file for the package.
    ├── admin.py                     # Admin-related configurations and settings.
    ├── apps.py                      # Application configuration settings.
    ├── models.py                    # Database models for throttling logic.
    ├── tests.py                     # Unit tests for the throttling module.
    ├── throttling.py                # Custom throttling logic implementation.
    ├── urls.py                      # URL routing for throttling-related endpoints.
    ├── views.py                     # Views handling throttling logic.
    └── seed.py                      # Script to seed the database with fake student data.
```

## Throttling Details

- **Anonymous User Throttle:** Limits the rate of requests for unauthenticated users.
- **User Throttle:** Limits the rate of requests for authenticated users.
- **Custom Throttle:** Custom logic to throttle specific endpoints based on business requirements.


## Acknowledgements

- **Django:** A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Django REST Framework:** A powerful and flexible toolkit for building Web APIs.
- **djangorestframework-simplejwt:** A JSON Web Token authentication package for Django REST Framework.
- **HTTPie:** A command-line HTTP client that makes it easy to interact with APIs.
- **Faker:** A library for generating fake data for testing and development.