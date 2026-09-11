# Kitepche

**Kitepche** is a reading platform for Kyrgyz-language children's books, built around an original NLP component: a readability analyzer that scores how difficult a Kyrgyz text is to read, so books can eventually be matched to a child's reading level automatically.

Kyrgyz is a low-resource language with very little existing NLP tooling. This project's core technical contribution is building that tooling — text analysis and readability scoring — from scratch, then wrapping it in a real product.

**Status:** MVP (minimum viable product) — core readability engine and frontend UI are functional and in active development. Authentication, a book database, and an admin panel are the next phase (see Roadmap).

---

## Project architecture

The project is split into two services:

1. **Backend (`/backend`)** — a FastAPI service exposing the Kyrgyz text readability analyzer as an API.
2. **Frontend (/frontend)** — a React web app for browsing the book library and analyzing Kyrgyz text readability. Login UI is in place but not yet wired to authentication (see Roadmap).

---

## What's built (MVP)

### Backend
- FastAPI app with two endpoints:
  - `GET /health` — health check
  - `POST /analyze` — accepts raw Kyrgyz text, returns readability metrics
- Original Kyrgyz-aware tokenizer (word/sentence segmentation handling Cyrillic script plus Kyrgyz-specific letters ө, ү)
- Original vowel-based syllable counter for Kyrgyz words
- Two readability scoring models implemented:
  - **ARI** (Automated Readability Index)
  - A **Flesch-style formula (Ateşman constants)**, adapted from Turkish as a first-pass approximation in the absence of a native Kyrgyz readability formula — a known limitation being tracked for future validation/retraining
- Returns word, sentence, character, and syllable counts alongside both readability scores

### Frontend
- React 19 + Vite 8 + Tailwind CSS v4, with React Router for client-side routing
- Landing page with header, hero banner, and a filterable book library (by age group: 6–7, 8–9, 10–11, 12+)
- Analyze page (`/analyze`): submits text to the backend's `POST /analyze` and displays word/sentence/syllable counts alongside ARI and Kyrgyz readability scores — implemented and working end-to-end
- Login button present in the header UI as a placeholder — not yet wired to any logic (auth doesn't exist yet, see Roadmap)
- Sample catalog of 6 books to demonstrate the library UI

---

## Scope of the MVP

This is a functioning proof of concept, not yet a production product. Deliberately out of scope for this phase:
- Persistent storage — the book catalog is currently sample data, not a database
- User accounts and authentication
- Automated tests, CI/CD, and deployment infrastructure
- ML-based scoring (current scoring is formula-based; see Roadmap)

---

## Tech stack

| Layer    | Tech |
|----------|------|
| Backend  | Python, FastAPI, Pydantic, Uvicorn |
| Frontend | React 19, Vite 8, Tailwind CSS v4, ESLint |

---

## Running locally

**Backend**
```bash
cd backend
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
API at `http://localhost:8000`, interactive docs at `http://localhost:8000/docs`.

**Frontend**
```bash
cd frontend
npm install
npm run dev
```
App at `http://localhost:5173`.

---

## API reference

**`POST /analyze`**
```json
// Request
{ "text": "Kыргыз тилиндеги текст..." }

// Response
{
  "words_count": 0,
  "sentences_count": 0,
  "characters_count": 0,
  "total_syllables": 0,
  "avg_syllables_per_word": 0.0,
  "avg_words_per_sentence": 0.0,
  "avg_characters_per_word": 0.0,
  "ari_score": 0.0,
  "readability_score": 0.0
}
```

**`GET /health`** → { "status": "ok" }

---

## Roadmap

**Phase 2 — Product foundation**
- Books database: replace the hardcoded catalog with real persistent storage
- Reading flow: when a user opens a book to read, the frontend fetches the book's content from the backend (new endpoint, e.g. `GET /books/{id}`) instead of using static data
- User registration and login: build real auth behind the existing "Login" button in the header
- Admin panel: a restricted view for adding/editing/removing books in the catalog, gated behind auth once it exists

**Phase 3 — ML & NLP depth** *(not required for the current MVP — see note below)*
- Move from formula-based scoring toward a trained/fine-tuned model for Kyrgyz text difficulty classification
- Build and validate a proper Kyrgyz readability formula (replacing the borrowed Turkish constants) against real reading-level data
- Explore additional NLP features (e.g. vocabulary-level tagging) to support recommendations

> **On ML:** the current MVP's readability scoring is fully functional using classical formulas (ARI + an adapted Ateşman formula) — no ML is required for it to work end-to-end. ML becomes worthwhile once a labeled Kyrgyz corpus (text tagged by reading level) exists to train and validate against; until then it's tracked as a future enhancement, not a blocker.

**Phase 4 — Production readiness**
- Automated tests, CI/CD
- Containerization and deployment

---
