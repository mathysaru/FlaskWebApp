from flask import Flask
from typing import Optional

def create_app(test_config: Optional[dict] = None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="dev",
        TESTING=False,
    )

    # simple in-memory store for workouts
    app.workouts = []  # list of {"workout": str, "duration": int}

    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    if test_config:
        app.config.update(test_config)

    return app
