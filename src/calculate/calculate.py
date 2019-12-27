import os
import random
from src.calculate import functions
from flask import make_response, abort
from src.check_service import check_service
from src.check_service.functions import check_url
import time


def calculate(operation, x, y, proxy_error, service_error, delay):
    if(delay == True):
        time.sleep(3)

    if(proxy_error == True):
        # If the proxy server occurs an error in real-world cases,
        # the server will raise an exception in somewhere that developers cannot predict
        raise Exception("Proxy Server Error Exception")

    # Get service from the YAML file
    selected_service = functions.get_service(operation)
    if(selected_service == None):
        # 400 bad request
        abort(400, "Operation {operator} not found".format(operator=operation))

    # check if the service is available
    service_info = check_service.check_service(selected_service)
    if(service_info['available'] == False):
        # If the service is not available
        # 500 internal server error
        abort(500, "Service(s) unavailable")

    # Only get working URLs
    selected_service = service_info['service']
    # Deal with the request using the selected_service
    URLs = selected_service['URLs']
    selected_URL = random.choice(URLs)

    print("Using the URL = "+selected_URL)
    service_response = functions.service_request(
        selected_URL, x, y, service_error)

    if(functions.check_response(service_response)):
            print("Service JSON = "+str(service_response.json()))
            service_json = service_response.json()
            response_body = functions.build_response_body(
                selected_service, x, y, service_json)
            if(response_body['error'] == True):
                reason = response_body['message']
                print("Bad request. message: "+reason)
                abort(400, reason)  # 400 bad request
            else:
                return make_response(response_body, 200)

    # Otherwise, the service has raised an error
    # 500 internal server error
    abort(
        500, "Internal Service Error! The %s service is not working properly" % (selected_service['operation']))
