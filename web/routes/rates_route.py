import psycopg2
from database.sql_helper import Database
from flask import Blueprint, make_response, json, request, Response
from urls import RATES_URL, PARENT_URL
from utils import validate_params

db = Database()

rates_blueprint = Blueprint("rates_api_route", __name__, url_prefix=RATES_URL)  # initializes blueprint for our API


@rates_blueprint.route(PARENT_URL, methods=['GET'])
def get_rates():
    params = validate_params(request.args)  # validates GET parameters
    is_validated = params['result']

    # returns respective error message if routes parameters are not valid
    if not is_validated:
        return Response(params['message'], 401)
    else:
        try:
            records_arr = db.fetch_avg_rates(params)

            # converts fetched routes records to json format, for displaying.
            response = Response(json.dumps(records_arr, indent=4), 200)
            response.headers['Content-Type'] = 'application/json'
            return response

        except psycopg2.Error:
            return Response('Error serving data from database', 401)

        except OSError:
            return Response('Can not open/read database query', 401)
