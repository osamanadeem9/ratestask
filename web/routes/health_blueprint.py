from flask import Blueprint, Response

from urls import HEALTH_URL

health_blueprint = Blueprint("health", __name__)


@health_blueprint.route(HEALTH_URL, methods=['GET'])
def health_check():
    return Response("Rates Task API working...", 200)
