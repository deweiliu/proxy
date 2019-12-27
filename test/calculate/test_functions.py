# reference https://www.guru99.com/pytest-tutorial.html
from src.calculate import functions
import yaml
from src.check_service import check_service


def setup_configuration():
    with open('configuration.yml', 'r') as file:
        configuration = yaml.safe_load(file)
    return configuration


def test_select_service():

    # read configuration file
    config = setup_configuration()

    # test add
    expected_service_name = "add"
    service = functions.select_service(
        expected_service_name, config['services'])
    assert expected_service_name == service['operation']

    # test subtract
    expected_service_name = "multiply"
    service = functions.select_service(
        expected_service_name, config['services'])
    assert expected_service_name == service['operation']

    # test multiply
    expected_service_name = "multiply"
    service = functions.select_service(
        expected_service_name, config['services'])
    assert str(expected_service_name) == str(service['operation'])


def test_build_response_body():

    # read configuration file
    config = setup_configuration()
    answer = 10
    service_response = {'answer': answer, 'error': False}

    for service in config['services']:
        result = functions.build_response_body(service, 0, 0, service_response)
        assert str(answer) == result['answer']


def test_service_request():
    x = [-10, -3, -1, 1, 3, 10]
    y = [-100, -30, -10, 10, 30, 100]

    # read configuration file
    config = setup_configuration()

    for service in config['services']:
        service_info = check_service.check_service(service)
        if(service_info['available'] == True):
            service = service_info['service']
            service_name = service['operation']
            for url in service['URLs']:
                for i in range(len(x)):
                    expected_answer = None
                    if(service_name == "add"):
                        expected_answer = x[i]+y[i]
                    elif(service_name == "subtract"):
                        expected_answer = x[i]-y[i]
                    elif(service_name == "multiply"):
                        expected_answer = x[i]*y[i]
                    if(expected_answer == None):
                        # Service not on test list
                        pass
                    else:
                        # Test the service_request
                        response_answer = functions.service_request(
                            url, x[i], y[i]).json()
                        assert expected_answer == response_answer['answer']
