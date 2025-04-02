# FastAPI Todo App

A simple FastAPI application for managing todo items.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the development server with hot reload:
```bash
uvicorn app:app --reload
```

The application will be available at:
- Main application: http://127.0.0.1:8000
- API documentation (Swagger UI): http://127.0.0.1:8000/docs
- Alternative API documentation (ReDoc): http://127.0.0.1:8000/redoc

## API Endpoints

- `GET /`: Hello World message
- `POST /items`: Create a new todo item
- `GET /items`: List all items (with pagination)
- `GET /items/{item_id}`: Get a specific item by ID

## Data Model

Items have the following structure:
```json
{
    "text": "string",
    "is_done": boolean
}
``` 