# Student Management System with Django and JWT Authentication

This project is a simple Student Management System built using Django and Django REST Framework. It includes JWT (JSON Web Token) authentication for securing the API endpoints.

## Features

- CRUD operations for Student model
- JWT authentication for API endpoints
- Admin interface for managing students

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

## Accessing APIs using HTTPie

HTTPie is a command-line HTTP client that makes it easy to interact with APIs. Below are some examples of how to use HTTPie to access the APIs in this project.

### Obtain JWT Token

First, you need to obtain a JWT token by logging in with your superuser credentials.

```bash
http POST http://127.0.0.1:8000/token/ username=your-username password=your-password
```

You will receive a response with an access token and a refresh token.

### Accessing Student API

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

- `models.py`: Defines the Student model.
- `urls.py`: Configures the URL routing for the API endpoints.
- `views.py`: Contains the viewset for the Student model.
- `settings.py`: Django settings for the project
- `admin.py`: Registers the Student model with the Django admin interface.
- `serializers.py`: Defines the serializer for the Student model.

## Acknowledgements

- Django
- Django REST Framework
- djangorestframework-simplejwt
- HTTPie