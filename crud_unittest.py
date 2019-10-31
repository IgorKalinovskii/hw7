import requests
import unittest

class TestCrud(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base_url = 'http://pulse-rest-testing.herokuapp.com/'
        cls.book_data1 = {'title': 'Происхождение видов', 'author': 'Чарльз Дарвин'}
        cls.book_data2 = {'title': 'Война миров', 'author': 'Герберт Уэллс'}
        cls.book_id = None

    def setUp(self):
        create = requests.post(self.base_url + 'books/', self.book_data1)
        self.book_id = create.json()['id']

    def tearDown(self) -> None:
        delete = requests.delete(self.base_url + 'books/' + str(self.book_id))


    def test_1_Create(self):
        create = requests.post(self.base_url + 'books/', self.book_data1)
        self.book_id = create.json()['id']
        self.assertEqual(create.status_code, 201)
        get_created = requests.get(self.base_url+'books/' + str(self.book_id) + '/')
        self.assertEqual(get_created.json(), create.json())

    def test_2_Read(self):
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
