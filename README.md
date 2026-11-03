# CareerBuddy - AI Resume Analyzer & Career Assistant

A beginner-friendly Python (Flask) website.

## Features
- Upload a resume (PDF / DOCX / TXT)
- Resume score out of 100 with a breakdown
- Skills detected by category
- Missing sections and improvement tips
- Job description match percentage
- Top 3 career suggestions
- Simple career chatbot

## How to run (Windows)
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000 in your browser.

## Project structure
| File | What it does |
|------|--------------|
| app.py | Flask routes (URLs) |
| analyzer.py | Reads files, finds skills, scores resume |
| assistant.py | Rule-based career chatbot |
| skills_data.py | Lists of skills, roles, roadmaps |
| templates/ | HTML pages (Jinja2) |
| static/style.css | Styling |

## Ideas to extend
- Save results in SQLite
- Replace the rule-based chatbot with an AI API (keep the key in an environment variable)
- Use scikit-learn TF-IDF for smarter job matching
