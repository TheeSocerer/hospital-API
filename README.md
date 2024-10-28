# Patient Management API Documentation

## Overview
This API provides endpoints for managing patient records and their medical history in a healthcare system. It includes functionality for creating, reading, updating, and deleting patient information, as well as managing medical records.

## Base URL
```
http://localhost:8000/api/
```

## Authentication
The API uses Token Authentication. All requests must include an Authorization header with a valid token.

### Getting an Authentication Token
```http
POST /api-token-auth/
Content-Type: application/json

{
    "username": "your_username",
    "password": "your_password"
}
```

**Response:**
```json
{
    "token": "your-auth-token"
}
```

### Using the Token
Include the token in the Authorization header for all API requests:
```
Authorization: Token your-auth-token
```

## Endpoints

### 1. Patient Management

#### List All Patients
```http
GET /api/patients/
Authorization: Token your-auth-token
```

**Response:**
```json
[
    {
        "patient_id": "P12345",
        "first_name": "John",
        "last_name": "Doe",
        "date_of_birth": "1990-01-01",
        "gender": "Male",
        "contact_number": "1234567890",
        "email": "john@example.com",
        "created_at": "2024-03-20T10:00:00Z",
        "updated_at": "2024-03-20T10:00:00Z",
        "medical_records": []
    }
]
```

#### Create New Patient
```http
POST /api/patients/
Authorization: Token your-auth-token
Content-Type: application/json

{
    "patient_id": "P12345",
    "first_name": "John",
    "last_name": "Doe",
    "date_of_birth": "1990-01-01",
    "gender": "Male",
    "contact_number": "1234567890",
    "email": "john@example.com"
}
```

#### Get Specific Patient
```http
GET /api/patients/{patient_id}/
Authorization: Token your-auth-token
```

#### Update Patient
```http
PUT /api/patients/{patient_id}/
Authorization: Token your-auth-token
Content-Type: application/json

{
    "first_name": "John",
    "last_name": "Doe",
    "date_of_birth": "1990-01-01",
    "gender": "Male",
    "contact_number": "1234567890",
    "email": "john@example.com"
}
```

#### Delete Patient
```http
DELETE /api/patients/{patient_id}/
Authorization: Token your-auth-token
```

### 2. Medical Records

#### Add Medical Record
```http
POST /api/patients/{patient_id}/add_medical_record/
Authorization: Token your-auth-token
Content-Type: application/json

{
    "diagnosis": "Common Cold",
    "treatment": "Prescribed cold medication",
    "prescription": "Antihistamines",
    "notes": "Follow-up in 1 week",
    "visit_date": "2024-03-20"
}
```

#### Get Patient's Medical History
```http
GET /api/patients/{patient_id}/medical_history/
Authorization: Token your-auth-token
```

**Response:**
```json
[
    {
        "id": 1,
        "diagnosis": "Common Cold",
        "treatment": "Prescribed cold medication",
        "prescription": "Antihistamines",
        "notes": "Follow-up in 1 week",
        "visit_date": "2024-03-20",
        "created_at": "2024-03-20T10:00:00Z",
        "updated_at": "2024-03-20T10:00:00Z",
        "patient": "P12345"
    }
]
```


## Search Functionality
The API supports searching patients by:
- patient_id
- first_name
- last_name
- email

Example:
```http
GET /api/patients/?search=John
Authorization: Token your-auth-token
```

## Error Handling

### Common HTTP Status Codes
- 200: Successful request
- 201: Successfully created
- 400: Bad request
- 401: Unauthorized
- 403: Forbidden
- 404: Not found
- 500: Internal server error

### Error Response Format
```json
{
    "detail": "Error message description"
}
```

## Rate Limiting
Currently, there are no rate limits implemented.

## Security Recommendations
1. Always use HTTPS in production
2. Keep authentication tokens secure
3. Implement token expiration in production
4. Use strong passwords
5. Regularly rotate authentication tokens

## Development Setup
1. Create a venv:
```bash
python3 -m venv venv
```
2.  activate venv:
```bash
source venv/bin/activate
```
3. install the requirents:
```bash
pip install -r requirements.txt

```
3. update the requirement txt()
```bash
pip freeze > requirements.txt
```
4. Run development server:
```bash
python manage.py runserver
```
## Testing with cURL

### Get Token
```bash
curl -X POST http://localhost:8000/api-token-auth/ \
-H "Content-Type: application/json" \
-d '{"username": "your_username", "password": "your_password"}'
```

### Create Patient
```bash
curl -X POST http://localhost:8000/api/patients/ \
-H "Authorization: Token your-token-here" \
-H "Content-Type: application/json" \
-d '{
    "patient_id": "P12345",
    "first_name": "John",
    "last_name": "Doe",
    "date_of_birth": "1990-01-01",
    "gender": "Male",
    "contact_number": "1234567890",
    "email": "john@example.com"
}'
```

### Add Medical Record
```bash
curl -X POST http://localhost:8000/api/patients/P12345/add_medical_record/ \
-H "Authorization: Token your-token-here" \
-H "Content-Type: application/json" \
-d '{
    "diagnosis": "Common Cold",
    "treatment": "Prescribed cold medication",
    "prescription": "Antihistamines",
    "notes": "Follow-up in 1 week",
    "visit_date": "2024-03-20"
}'
```
