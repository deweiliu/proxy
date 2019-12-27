import requests
import yaml
import json
CONFIGURATION_FILE = 'configuration.yml'


def get_service(operation):
    """
    get the service from the configuration file
    return None if no service matches the given operation
    """
    with open(CONFIGURATION_FILE, 'r') as file:
        configuration = yaml.safe_load(file)
    services = configuration['services']
    return select_service(operation, services)


def select_service(operation_name, services):

    for service in services:
        if(service['operation'] == operation_name):
            return service

    return None


def build_response_body(service, x, y, service_response):
    response = dict()
    if(service_response['error'] == True):
        response['error'] = True
        message = "Message from the %s service = " % (
            service['operation']) + str(service_response['message'])
        response['message'] = message
    else:
        response['error'] = False
        response['expression'] = str(x)+str(service['operator'])+str(y)
        response['answer'] = str(service_response['answer'])
    return response


def service_request(url, x, y, service_error=None):
    parameters = dict()
    parameters['x'] = x
    parameters['y'] = y
    if(service_error == True):
        parameters['testingError'] = 'true'
    try:
        print("Sending request to "+str(url))
        print("With parameters = "+str(parameters))
        response = requests.get(url=url, params=parameters)

    except:
        return None  # None means service has raised an unknown error
    return response  # if the GET request was successful


def build_json_response(response_code, error, **kwargs):
    response = dict()
    response['response_code'] = response_code
    response['error'] = error

    for key in kwargs:
        response[key] = kwargs[key]

    return response


def check_response(response):
    responseOK = False
    if(response == None):
        print("No response")
    else:
        # The services are disigned to only return 200 
        if(response.status_code == 200):
            try:
                get_json = response.json()
                responseOK = True
            except Exception:
                print("Response body is not JSON")
        else:
            print("response code = "+str(response.status_code))
    return responseOK
