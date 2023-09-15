
# Zuri_Training_Stage_2 CRUD API ENDPOINT

## Simple Django REST API

Welcome to the Simple Django REST API for managing person data. This API allows you to perform basic CRUD (Create, Read, Update, Delete) operations on person records.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before getting started, make sure you have the following software installed on your system:

- Python
- Django
- Django Rest Framework

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-django-api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd your-django-api
   ```

3. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

4. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

Your Django API should now be running at http://localhost:8000/.
```

Feel free to copy and paste this markdown into your `README.md` file, and customize it further if needed.

# Usage

You can use this API to manage person data. Here are the available API endpoints:

- **Create a Person**: POST `/api/`
- **Retrieve a Person**: GET `/api/{id}/`
- **Update a Person**: PUT `/api/{id}/`
- **Partial Update of a Person**: PATCH `/api/{id}/`
- **Delete a Person**: DELETE `/api/{id}/`
- **List All Persons**: GET `/api/`

For detailed information on each endpoint and how to format requests, refer to the **API Endpoints** section.

## API Endpoints

### Create a Person

- **URL**: `/api/`
- **Method**: POST
- **Request Body**: JSON object containing person data (first_name, last_name, age)
- **Response**: JSON representation of the created person

### Retrieve a Person

- **URL**: `/api/{id}/`
- **Method**: GET
- **Response**: JSON representation of the person with the specified ID

### Update a Person

- **URL**: `/api/{id}/`
- **Method**: PUT
- **Request Body**: JSON object containing updated person data (first_name, last_name, age)
- **Response**: JSON representation of the updated person

### Partial Update of a Person

- **URL**: `/api/{id}/`
- **Method**: PATCH
- **Request Body**: JSON object containing partial person data (e.g., `{"age": 30}`)
- **Response**: JSON representation of the partially updated person

### Delete a Person

- **URL**: `/api/{id}/`
- **Method**: DELETE
- **Response**: No content (204)

### List All Persons

- **URL**: `/api/`
- **Method**: GET
- **Response**: JSON array containing all person records

## Examples

Here are some examples of how to use the API:

- **Create a New Person**:

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"first_name": "John", "last_name": "Doe", "age": 30}' http://localhost:8000/api/
Retrieve a Person:

bash
Copy code
curl http://localhost:8000/api/1/
Update a Person:

bash
Copy code
curl -X PUT -H "Content-Type: application/json" -d '{"first_name": "Jane", "last_name": "Smith", "age": 25}' http://localhost:8000/api/1/
Delete a Person:

bash
Copy code
curl -X DELETE http://localhost:8000/api/1/
For more examples and details, please refer to the Usage section.

sql
Copy code

Feel free to copy and paste this markdown into your `README.m

Contributing
Feel free to contribute to this project by opening issues or pull requests. Your feedback and contributions are highly appreciated!