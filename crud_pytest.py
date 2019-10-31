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
def id()


def test_create(url,book_data1):
    create = requests.post(url + 'books/', book_data1)
    self.book_id = create.json()['id']


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



import requests
import pytest

class Test_crud():
    @classmethod
    def setup_class(cls):
        cls.base_url = 'http://pulse-rest-testing.herokuapp.com/'
        cls.book_data1 = {'title': 'Происхождение видов', 'author': 'Чарльз Дарвин'}
        cls.book_data2 = {'title': 'Война миров', 'author': 'Герберт Уэллс'}
        cls.book_id = None

    def setup_method(self):
        create = requests.post(self.base_url + 'books/', self.book_data1)
        self.book_id = create.json()['id']

    def teardown_method(self):
        delete = requests.delete(self.base_url + 'books/' + str(self.book_id))


    def test_1_create(self):
        create = requests.post(self.base_url + 'books/', self.book_data1)
        self.book_id = create.json()['id']
        self.assertEqual(create.status_code, 201)
        get_created = requests.get(self.base_url+'books/' + str(self.book_id) + '/')
        self.assertEqual(get_created.json(), create.json())

    def test_2_read(self):
        read = requests.get(self.base_url+'books/' + str(self.book_id) + '/')
        self.assertEqual(read.status_code, 200)

        self.assertEqual(read.json()['title'], 'Происхождение видов')
        self.assertEqual(read.json()['author'], 'Чарльз Дарвин')

        self.assertEqual(read.json()['title'], self.book_data1['title'])
        self.assertEqual(read.json()['author'], self.book_data1['author'])

        self.book_data1['id'] = read.json()['id']
        self.assertDictEqual(self.book_data1, read.json())



    def test_3_Update(self):
        update = requests.put(self.base_url + 'books/' + str(self.book_id) + '/', self.book_data2)
        self.assertEqual(update.status_code, 200)
        self.assertEqual(update.json()['title'], self.book_data2['title'])
        self.assertEqual(update.json()['author'], self.book_data2['author'])

    def test_4_Delete(self):
        delete = requests.delete(self.base_url + 'books/' + str(self.book_id))
        self.assertEqual(delete.status_code, 204)
        get_deleted = requests.get((self.base_url + 'books/' + str(self.book_id)))
        self.assertEqual(get_deleted.status_code, 404)

myTestSuit = unittest.TestLoader().loadTestsFromTestCase(TestCrud)


if __name__ == "__main__":
    unittest.main()
    # from HtmlTestRunner import HTMLTestRunner
    # unittest.main(verbosity=2, testRunner=HTMLTestRunner(output=r"F:\test"))
