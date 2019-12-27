import requests


def get_urls(service):
    return service['URLs']


def check_url(url):
    try:
        response = requests.get(url)
        if(response.status_code == 200):  # reference https://realpython.com/python-requests/
            return True
        else:
            print("Response code = "+str(response.status_code)+ "\tURL = "+url)
            return False
    except requests.exceptions.ConnectionError:
        return False
