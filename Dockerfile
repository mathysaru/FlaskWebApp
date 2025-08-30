# syntax=docker/dockerfile:1
FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1     PYTHONUNBUFFERED=1

# Install runtime dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

# Copy app source and tests into the image (so tests can run inside the container)
COPY app ./app
COPY run.py ./run.py
COPY tests ./tests
COPY pytest.ini ./pytest.ini

EXPOSE 5000

# Default command runs the web app (CI will override the command to run tests)
CMD ["python", "run.py"]