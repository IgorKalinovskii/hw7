import requests
import pytest


def test_even():
    data = 10
    assert data % 2 == 0


@pytest.fixture(scope="session")
def url():
    return "http://pulse-rest-testing.herokuapp.com/"


def test_book(url):
    r = requests.post(url+"books", data = {"title": "1", "author": "2"})
    assert r.status_code == 201
    # TODO: clear


@pytest.fixture()
def book(url):
    r = requests.post(url + "books", data={"title": "1", "author": "2"})
    b = r.json()
    yield b
    requests.delete(f"{url}books/{b['id']}")


@pytest.fixture(scope="session")
def clear_roles_by_id(url):
    id_list = []
    yield id_list
    for role_id in id_list:
        requests.delete(f"{url}roles/{role_id}")


def test_role(url, book, clear_roles_by_id):
    role = {"name": "1", "type": "2", "book": f"{url}books/{book['id']}"}
    r = requests.post(url+"roles", data = role)
    assert r.status_code == 201
    response_data = r.json()
    clear_roles_by_id.append(response_data["id"])