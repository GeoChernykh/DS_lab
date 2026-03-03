from flask import Flask
from app.api.forecast_route import forecast_bp
from app.errors import register_error_handlers


def create_app():
    app = Flask(__name__)

    app.register_blueprint(forecast_bp)

    register_error_handlers(app)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)