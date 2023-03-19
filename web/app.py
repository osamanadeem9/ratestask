from flask import Flask
import os
import psycopg2
from dotenv import load_dotenv
from routes.rates_route import rates_blueprint
from routes.error_route import error_blueprint
from routes.health_blueprint import health_blueprint


def create_app():
    app = Flask(__name__)
    load_dotenv()

    # blueprint helps to structure the application, registering routes and makes code cleaner.
    app.register_blueprint(rates_blueprint)
    app.register_blueprint(health_blueprint)
    app.register_blueprint(error_blueprint)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
