# Zuri_Training_Stage_2
CRUD API ENDPOINT

Simple Django REST API
Welcome to the Simple Django REST API for managing person data. This API allows you to perform basic CRUD (Create, Read, Update, Delete) operations on person records.

Table of Contents
Prerequisites
Installation
Usage
API Endpoints
Examples
Contributing
License
Prerequisites

Before getting started, make sure you have the following software installed on your system:

Python
Django
Django Rest Framework

Installation
Clone the repository:
git clone https://github.com/yourusername/your-django-api.git

Navigate to the project directory:
cd your-django-api

Create and activate a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate

Install project dependencies:
pip install -r requirements.txt

Apply database migrations:
python manage.py migrate

Start the development server:
python manage.py runserver
Your Django API should now be running at http://localhost:8000/.

Usage
You can use this API to manage person data. Here are the available API endpoints:

Create a Person: POST /api/persons/
Retrieve a Person: GET /api/persons/{id}/
Update a Person: PUT /api/persons/{id}/
Partial Update of a Person: PATCH /api/persons/{id}/
Delete a Person: DELETE /api/persons/{id}/
List All Persons: GET /api/persons/
For detailed information on each endpoint and how to format requests, refer to the API Endpoints section.

API Endpoints
Create a Person
URL: /api/persons/
Method: POST
Request Body: JSON object containing person data (first_name, last_name, age)
Response: JSON representation of the created person

Retrieve a Person
URL: /api/persons/{id}/
Method: GET
Response: JSON representation of the person with the specified ID

Update a Person
URL: /api/persons/{id}/
Method: PUT
Request Body: JSON object containing updated person data (first_name, last_name, age)
Response: JSON representation of the updated person

Partial Update of a Person
URL: /api/persons/{id}/
Method: PATCH
Request Body: JSON object containing partial person data (e.g., {"age": 30})
Response: JSON representation of the partially updated person

Delete a Person
URL: /api/persons/{id}/
Method: DELETE
Response: No content (204)

List All Persons
URL: /api/persons/
Method: GET
Response: JSON array containing all person records

Examples
Here are some examples of how to use the API:

Create a New Person:
curl -X POST -H "Content-Type: application/json" -d '{"first_name": "John", "last_name": "Doe", "age": 30}' http://localhost:8000/api/persons/

Retrieve a Person:
curl http://localhost:8000/api/persons/1/

Update a Person:
curl -X PUT -H "Content-Type: application/json" -d '{"first_name": "Jane", "last_name": "Smith", "age": 25}' http://localhost:8000/api/persons/1/

Delete a Person:
curl -X DELETE http://localhost:8000/api/persons/1/
For more examples and details, please refer to the Usage section.

Contributing
Feel free to contribute to this project by opening issues or pull requests. Your feedback and contributions are highly appreciated!