import requests
import pytest


@pytest.fixture(scope="session")
def url():
    return "http://pulse-rest-testing.herokuapp.com/"

@pytest.fixture(scope="session")
def book_data1():
    return {'title': 'Происхождение видов', 'author': 'Чарльз Дарвин'}

@pytest.fixture(scope="session")
def book_data2():
    return {'title': 'Война миров', 'author': 'Герберт Уэллс'}

@pytest.fixture(scope="session")
def setup(url, book_data1):
    create = requests.post(url + 'books/', book_data1)
    b = create.json()
    yield b
    delete = requests.delete(url + 'books/' + str(create.json()['id']))


def test_create(url, book_data1):
    create = requests.post(url + 'books/', book_data1)
    assert create.status_code == 201
    get_created = requests.get(url + 'books/' + str(create.json()["id"]))
    assert get_created.json()['title'] == 'Происхождение видов'
    assert get_created.json()['author'] == 'Чарльз Дарвин'


def test_read(setup, url, book_data1):
    read = requests.get(url + 'books/' + str(setup['id']) + '/')
    assert read.status_code == 200
    assert read.json()['title'] == 'Происхождение видов'
    assert read.json()['author'] == 'Чарльз Дарвин'


def test_update(setup,url,book_data2):
    update = requests.put(url + 'books/' + str(setup['id']) + '/', book_data2)
    assert update.status_code == 200
    assert update.json()['title'] == "Война миров"
    assert update.json()['author'] == 'Герберт Уэллс'

def test_delete(setup,url):
    delete = requests.delete(url + 'books/' + str(setup['id']))
    assert delete.status_code == 204
    get_deleted = requests.get(url + 'books/' + str(setup['id']))
    assert get_deleted.status_code == 404
