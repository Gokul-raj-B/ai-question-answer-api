# AI API using FastAPI

## Project Description

This project is a simple AI API built using Python and FastAPI.

It accepts a text input from the user through a POST API endpoint and returns a response.

## Technologies Used

* Python
* FastAPI
* Uvicorn
* JSON
* REST API

## API Endpoint

**POST /generate**

The user sends a text input to the `/generate` endpoint.

### Example Input

```json
{
  "text": "Explain artificial intelligence in simple terms"
}
```

### Example Response

```json
{
  "input": "Explain artificial intelligence in simple terms",
  "response": "This is a simple AI response."
}
```

## How It Works

```text
User
  ↓
POST /generate
  ↓
FastAPI
  ↓
Python processing
  ↓
Response
  ↓
User
```

## How to Run

Install the required packages:

```bash
uv pip install -r requirements.txt
```

Run the FastAPI server:

```bash
uvicorn main:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

Use the Swagger UI to test the `/generate` endpoint.

## Learning Outcome

This project demonstrates how a Python-based AI capability can be exposed through a REST API using FastAPI and how requests and responses are handled using JSON.
