# reference https://www.guru99.com/pytest-tutorial.html
from src.check_service import functions
from faker import Faker


def test_check_url():
    urls = ["http://qub.ac.uk",
            "http://gitlab2.eeecs.qub.ac.uk", ]
    invalid_urls = ["http://DomainNotExist-bnaownbsangoanlfhew.com",
                    "http://DomainNotExist-nbonboaehahlnafl.com"]
    for url in urls:
        assert True == functions.check_url(url)
    for url in invalid_urls:
        assert False == functions.check_url(url)


def test_get_urls():
    faker = Faker()
    service = dict()
    urls = faker.words()
    service['URLs'] = urls
    assert urls == functions.get_urls(service)
