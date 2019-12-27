import yaml
from flask import make_response, abort
from src.check_service.check_service import check_service


def services():
    with open("configuration.yml", 'r') as file:
        configuration = yaml.safe_load(file)

    services = list()
    unavailable_services = list()
    for service in configuration['services']:
        result = check_service(service)

        # do not include the actual service URLs to the response sent to the frontend
        # the frontend just needs to know the URL of this proxy service
        del service['URLs']

        # if the service is available
        if(result['available'] == True):
            services.append(service)
        else:
            unavailable_services.append(service)

    response = dict()
    response['services'] = services
    response['unavailable_services'] = unavailable_services

    return make_response(response, 200)
