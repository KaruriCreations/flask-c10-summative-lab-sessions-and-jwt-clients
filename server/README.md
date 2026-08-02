# Flask Notes App API

A Flask backend API for managing personal notes with session-based authentication and pagination. Built for Moringa School Phase 4 Summative Lab.

## Features
- User signup, login, logout, and session checks (`flask_bcrypt` + Flask session).
- Note management (CRUD operations with ownership protection).
- Paginated note listings.

## Setup & Installation

1. Install dependencies:
   ```bash
   pipenv install && pipenv shell
   ```

2. Run database migrations:
   ```bash
   flask db upgrade
   ```

3. Seed the database with sample data:
   ```bash
   python seed.py
   ```

## Running the App

Start the Flask server:
```bash
python app.py
```
The API runs at `http://localhost:5555`.

## Endpoints Summary

- **Auth**: `POST /signup`, `POST /login`, `DELETE /logout`, `GET /check_session`
- **Notes**: `GET /notes` (supports `?page=` & `?per_page=`), `POST /notes`, `PATCH /notes/<id>`, `DELETE /notes/<id>`
