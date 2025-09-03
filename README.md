# ACEest Fitness & Gym — DevOps Assignment (Flask + Pytest + Docker + GitHub Actions)

  A minimal, production-ready starter demonstrating **Flask** application development, **Git** version control, **Pytest** unit testing, **Docker** containerization, and a **CI pipeline on GitHub Actions** that **builds the Docker image and runs tests inside the image on every push**.

## What’s included
  - A Flask web app with:
    - `/` — simple UI to add and list workouts
    - `/api/workouts` — REST API to create/list workouts (JSON)
    - `/health` — health check endpoint
  - Pytest tests for the core routes
  - Dockerfile that packages the app **and tests**
  - GitHub Actions workflow that:
    1. Builds the Docker image
    2. Runs `pytest` **inside** the built image

## Prerequisites (macOS)
  - **Git** — `xcode-select --install`
  - **Python 3.11+** — `python3 --version`
  - **pip** — `python3 -m pip --version`
  - **Docker Desktop** — Install from https://www.docker.com/products/docker-desktop/

## Project structure

```
aceest-fitness-devops/
├─ app/
│  ├─ __init__.py
│  ├─ routes.py
│  └─ static/
│     └─ styles.css
│  └─ templates/
│     └─ index.html
├─ tests/
│  └─ test_app.py
├─ .github/
│  └─ workflows/
│     └─ ci.yml
├─ .gitignore
├─ .dockerignore
├─ Dockerfile
├─ pytest.ini
├─ requirements.txt
├─ run.py
└─ README.md
```

## Run in local

  ```bash
  # 1) Create and activate a virtual environment
  python3 -m venv .venv
  source .venv/bin/activate 

  # 2) Install dependencies
  pip install -r requirements.txt

  # 3) Run tests
  pytest

  # 4) Launch the app
  python run.py
  # App will be at http://127.0.0.1:5000/
  ```

## Run with Docker

  ```bash
  # Build the image
  docker build -t aceest-fitness:local .

  # Run tests INSIDE the container
  docker run --rm aceest-fitness:local pytest

  # Start the web app (Ctrl+C to stop)
  docker run --rm -p 5000:5000 aceest-fitness:local
  # Open http://localhost:5000/
  ```

## GitHub Actions (CI/CD)

  This repo includes `.github/workflows/ci.yml` which:
  1. Builds the Docker image from the **Dockerfile**.
  2. Runs `pytest` **inside** that image.

## Endpoints

  - `GET /health` → `{"status": "ok"}`
  - `GET /api/workouts` → list of workouts
  - `POST /api/workouts` → create a workout

**POST body (JSON or form-data):**

  ```json
  {
    "workout": "Running",
    "duration": 30
  }
  ```

## Suggested Git workflow

  ```bash
  git init
  git add .
  git commit -m "feat: initial Flask app, tests, Dockerfile, CI workflow"

  # Create a repo on GitHub (public), then:
  git remote add origin https://github.com/mathysaru/FlaskWebApp.git
  git branch -M main
  git push -u origin main

  # Create a feature branch for a new change
  git checkout -b feat/add-calories-field
  # ...make changes...
  git add .
  git commit -m "feat(workouts): support calories field"
  git push -u origin feat/add-calories-field
  # Open a Pull Request → Actions should run automatically
  ```

---

## Learnings

  - Understood how Flask apps are structured with routes, templates, and models.
  - Learned to write a Dockerfile and solve common issues with dependencies.
  - Practiced running the app inside a Docker container.
  - Saw how DevOps practices (version control, CI/CD readiness, containerization) apply even to small projects.

## Author

  Sarumathy G.
  Introduction to DevOps – BITS Pilani
  2024tm93153@wilp.bits-pilani.ac.in