# Domain-Specific Flask + Gemini Chatbot

This project is a reusable domain-specific chatbot built with Flask and the Google Gemini API.

## Features
- No login/register
- Gemini API key in `.env` (or configurable in `config.py`)
- Configurable Gemini model
- `config.py` controls title, domain, system prompt, behavior, welcome message, theme and PORT
- Temporary session-based chat history
- Each browser session has its own conversation
- Domain-only answering rule
- Responsive UI for mobile, tablet, laptop and desktop
- Gunicorn/Render deployment
- `/health` endpoint

## Folder structure
```text
app.py
config.py
.env
requirements.txt
templates/
  index.html
README.md
```

## 1. Install
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## 2. API key
Edit `.env`:
```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
FLASK_SECRET_KEY=change-this-to-a-random-secret
PORT=5000
```

You can also set the API key in `config.py`, but `.env` is recommended.

## 3. Run locally
```bash
python app.py
```
Open:
http://127.0.0.1:5000

## 4. Render
Create a GitHub repository and upload these files.

Build Command:
```bash
pip install -r requirements.txt
```

Start Command:
```bash
gunicorn app:app
```

Add these Render environment variables:
- `GEMINI_API_KEY`
- `FLASK_SECRET_KEY`

Render supplies `PORT` automatically; the app reads it when present.

## 5. Customize
Edit only `config.py` to create another domain chatbot:
- `CHATBOT_TITLE`
- `DOMAIN`
- `SYSTEM_PROMPT`
- `BEHAVIOR`
- `WELCOME_MESSAGE`
- `PRIMARY_COLOR`
- `DARK_COLOR`
- `SOFT_COLOR`
- `PORT`
- `GEMINI_MODEL`

## Security note
Do not commit your real `.env` API key to GitHub. Add `.env` to `.gitignore` for public repositories.
