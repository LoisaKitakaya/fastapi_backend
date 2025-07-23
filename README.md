# Recipe and Meal Planning API

## Overview

This project is a FastAPI-based backend for a Recipe and Meal Planning Helper, designed as part of a technical assessment. It integrates with Google's Gemini AI (free tier) to generate structured recipe responses based on user queries about ingredients. The API provides endpoints for health checks and recipe generation, with a focus on clean code, synchronous endpoints, and robust error handling.

### Features

- **Health Check Endpoint**: `GET /` returns a status message to confirm the API is running.
- **Query Endpoint**: `POST /api/query` accepts a user query (e.g., "What can I cook with chicken, rice, and broccoli?") and returns a structured recipe response.
- **Gemini AI Integration**: Uses `gemini-2.0-flash-001` to generate recipe data in JSON format.
- **Pydantic Validation**: Ensures structured responses with a nested Details model for recipe details.
- **Docker Support**: Containerized setup for consistent deployment.

### Prerequisites

- Python 3.13+ (for local setup)
- Docker (for containerized setup)
- A Google Gemini AI API key (free tier) from Google AI Studio
- A .env file with: `GEMINI_API_KEY=your_api_key`

### Setup Instructions

#### Local Setup

1. Clone the Repository:

```bash
git clone https://github.com/LoisaKitakaya/fastapi_backend.git

cd fastapi_backend
```

2. Create a Virtual Environment:

```bash
python -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Dependencies:

```bash
pip install -r requirements.txt
```

4. Set Up Environment Variables:

   - Create a .env file in the project

```bash
GEMINI_API_KEY=your_api_key

# Replace your_api_key with your Gemini AI API key.
```

5. Run the Application:

```bash
fastapi dev main:app
```

6. Access the API:

   - Health check: Open http://127.0.0.1:8000/ in a browser or use:

```bash
curl http://127.0.0.1:8000/

# Open http://127.0.0.1:8000/docs for interactive API documentation.
```

Expected response:

```json
{ "message": "Recipe and Meal Planning API is running" }
```

#### Docker Setup

1. Clone the Repository (if not already done):

```bash
git clone https://github.com/LoisaKitakaya/fastapi_backend.git

cd fastapi_backend
```

2. Set Up Environment Variables:

   - Create a .env file in the project

```bash
GEMINI_API_KEY=your_api_key

# Replace your_api_key with your Gemini AI API key.
```

3. Build the Docker Image:

```bash
docker build -t recipe-api .
```

4. Run the Docker Container:

```bash
docker run -d -p 8000:8000 --env-file .env recipe-api
```

5. Access the API:

   - Health check: Open http://0.0.0.0:8000/ or use:

```bash
curl http://0.0.0.0:8000/

# Swagger UI: Open http://0.0.0.0:8000/docs.
```

Expected response:

```json
{ "message": "Recipe and Meal Planning API is running" }
```

#### Usage

- Health Check:

  - Endpoint: GET /
  - Response: Confirms the API is running.

Example:

```bash
curl http://0.0.0.0:8000/
```

- Query Recipes:

  - Endpoint: POST /api/query
  - Request Body:{"query": "What can I cook with chicken, rice, and broccoli?"}

Response:

```json
{
  "answer": "Chicken Broccoli Fried Rice",
  "details": {
    "recipe_name": "Chicken Broccoli Fried Rice",
    "ingredients": ["200g chicken breast", "1 cup rice", "1 cup broccoli"],
    "instructions": ["Cook rice", "Sauté chicken", "Stir-fry broccoli"],
    "tips": ["Add soy sauce for flavor"],
    "prep_time": "30 minutes"
  }
}
```

Example:

```bash
curl -X POST "http://0.0.0.0:8000/api/query" -H "Content-Type: application/json" -d '{"query": "What can I cook with chicken, rice, and broccoli?"}'
```

- Swagger UI:

  - Access `http://0.0.0.0:8000/docs` for interactive testing of endpoints.

## Project Structure

```plain
.
├── services/
  ├── __init__.py
│ └── gemini.py
├── .env
├── .gitignore
├── Dockerfile
├── main.py
├── README.md
└── requirements.txt
```
