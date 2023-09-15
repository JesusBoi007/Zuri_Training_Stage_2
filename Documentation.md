Usage
You can use this API to manage person data. Here are the available API endpoints:

Create a Person: POST /api/
Retrieve a Person: GET /api/{id}/
Update a Person: PUT /api/{id}/
Partial Update of a Person: PATCH /api/{id}/
Delete a Person: DELETE /api/{id}/
List All Persons: GET /api/
For detailed information on each endpoint and how to format requests, refer to the API Endpoints section.

API Endpoints
Create a Person
URL: /api/
Method: POST
Request Body: JSON object containing person data (first_name, last_name, age)
Response: JSON representation of the created person

Retrieve a Person
URL: /api/{id}/
Method: GET
Response: JSON representation of the person with the specified ID

Update a Person
URL: /api/{id}/
Method: PUT
Request Body: JSON object containing updated person data (first_name, last_name, age)
Response: JSON representation of the updated person

Partial Update of a Person
URL: /api/{id}/
Method: PATCH
Request Body: JSON object containing partial person data (e.g., {"age": 30})
Response: JSON representation of the partially updated person

Delete a Person
URL: /api/{id}/
Method: DELETE
Response: No content (204)

List All Persons
URL: /api/
Method: GET
Response: JSON array containing all person records

Examples
Here are some examples of how to use the API:

Create a New Person:
curl -X POST -H "Content-Type: application/json" -d '{"first_name": "John", "last_name": "Doe", "age": 30}' http://localhost:8000/api/

Retrieve a Person:
curl http://localhost:8000/api/1/

Update a Person:
curl -X PUT -H "Content-Type: application/json" -d '{"first_name": "Jane", "last_name": "Smith", "age": 25}' http://localhost:8000/api/1/

Delete a Person:
curl -X DELETE http://localhost:8000/api/1/
For more examples and details, please refer to the Usage section.