from flask import Blueprint, Response

error_blueprint = Blueprint("errors", __name__)


@error_blueprint.app_errorhandler(Exception)
def server_error():
    return Response(f"Oops, got a server error!", status=500)
