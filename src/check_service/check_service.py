import yaml
from flask import make_response, abort
from src.check_service import functions


def check_service(service):
    availabe = False
    availabe_urls = list()
    for url in functions.get_urls(service):
        if(functions.check_url(url)):
            availabe = True
            availabe_urls.append(url)

    service['URLs'] = availabe_urls
    response = dict()
    response['service'] = service
    response['available'] = availabe

    return response
