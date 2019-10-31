import requests
import unittest

class TestCrud(unittest.TestCase):
    def __init__(self, base_url = 'http://pulse-rest-testing.herokuapp.com/',
                   book_data1 = {'title': 'Происхождение видов', 'author': 'Чарльз Дарвин'},
                   book_data2 = {'title': 'Война миров', 'author': 'Герберт Уэллс'}):
        self.base_url = base_url
        self.book_data1 = book_data1
        self.book_data2 = book_data2
        self.book_id = None

    def testCreate(self):
        create = requests.post(self.base_url + 'books/', self.book_data1)
        self.book_id = create.json()['id']
        self.assertEqual(create.status_code, 201)
        get_created = requests.get(self.base_url+'books/' + str(self.book_id) + '/')
        for item in get_created.json():
            self.assertEqual(get_created.json()[item], self.book_data1[item])
        # return create

    def read(self):
        read = requests.get(self.base_url+'books/' + str(self.book_id) + '/')
        return read

    def update(self):
        update = requests.put(self.base_url+'books/' + str(self.book_id) + '/', self.book_data2)
        return update

    def delete(self):
        delete = requests.delete(self.base_url + 'books/' + str(self.book_id))
        return delete


    def debug_printer(self):
        print ('create', self.create())
        print('read', self.read())
        print('update', self.update())
        print('delete', self.delete())

myTestSuit = unittest.TestLoader().loadTestsFromTestCase(TestCrud)


if __name__ == "__main__":
    unittest.main()
    # from HtmlTestRunner import HTMLTestRunner
    # unittest.main(verbosity=2, testRunner=HTMLTestRunner(output=r"E:\workspace\test_test"))
    # a = crud()
    # a.create()
    # a.read()
    # a.update()
    # a.delete()
    # a.debug_printer()
