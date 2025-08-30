from flask import Blueprint, jsonify, request, current_app, render_template

bp = Blueprint("main", __name__)

# Health check
@bp.get("/health")
def health():
    return jsonify({"status": "ok"}), 200

# Serve index.html
@bp.get("/")
def index():
    # Render index.html which now links the static CSS
    return render_template("index.html")

# List all workouts
@bp.get("/api/workouts")
def list_workouts():
    # Ensure workouts list exists
    if not hasattr(current_app, "workouts"):
        current_app.workouts = []
    return jsonify(current_app.workouts), 200

# Add a workout
@bp.post("/api/workouts")
def add_workout():
    # Accept JSON or form-encoded data
    data = request.get_json(silent=True) or request.form

    workout = (data.get("workout") or "").strip()
    duration_raw = data.get("duration")

    if not workout:
        return jsonify({"error": "Workout is required."}), 400

    # Validate duration is a positive integer
    try:
        duration = int(duration_raw)
        if duration <= 0:
            raise ValueError
    except Exception:
        return jsonify({"error": "Duration must be a positive integer."}), 400

    # Initialize workouts list if not exists
    if not hasattr(current_app, "workouts"):
        current_app.workouts = []

    entry = {"workout": workout, "duration": duration}
    current_app.workouts.append(entry)
    return jsonify(entry), 201
