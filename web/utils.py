""" contains utility functions, like validating query params. """
from datetime import datetime


def validate_params(args):
    date_from = args.get('date_from')
    date_to = args.get('date_to')
    origin = args.get('origin')
    destination = args.get('destination')

    # checks if any query parameter is missing
    if (date_from is None) or (date_to is None) or (origin is None) or (destination is None):
        return {'result': False,
                "message": "Parameters not found"}
    
    # checks if origin or destination value is not entered
    if (len(origin) == 0 or len(destination) == 0):
            return {'result': False,
            "message": "Please enter valid origin and destination values"}
            
    # validates if datetime is valid, and in correct format
    try:
        datetime.strptime(date_from, "%Y-%m-%d")
        datetime.strptime(date_to, "%Y-%m-%d")
    except:
        return {'result': False,
                "message": "Please enter date in the correct format YYYY-MM-DD."}
    
    startDate = datetime.strptime(date_from, "%Y-%m-%d")
    endDate = datetime.strptime(date_to, "%Y-%m-%d")
    
    # checks if start date is less than ending date
    valid_date = is_valid_date_difference(startDate, endDate)
    if (not valid_date):
        return {'result': False,
                "message": "Please enter valid start and ending date. Correct format: YYYY-MM-DD."}
    
    # returns valid parameters to use for fetching data from db
    return {'result': True, 'date_from': datetime.strptime(date_from, "%Y-%m-%d"),
            'date_to': datetime.strptime(date_to, "%Y-%m-%d"), 'origin': origin, 'destination': destination}


def is_valid_date_difference(startDate, endDate):
    if (startDate > endDate):
        return False
    else:
        return True