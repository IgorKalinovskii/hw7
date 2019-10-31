import unittest
import requests
from crud import crud


class TestCrud(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.obj = crud()
        # cls.book_id = cls.obj.book_id
        cls.url = cls.obj.base_url
        # cls.book_data1 = cls.obj.book_data1
        # cls.book_data1 = cls.obj.book_data2

    def test_1_Create(self):
        create = self.obj.create()
        self.assertEqual(create.status_code, 201)
        get_create = requests.get(self.url +'books/' + str(create.json()['id']) + '/')
        self.assertCountEqual(create.json(), get_create.json())


    def test_2_Read(self):
        read = self.obj.read()
        self.assertEqual(read.status_code, 200)
        self.assertEqual(read.json()['title'], 'Происхождение видов')
        self.assertEqual(read.json()['author'], 'Чарльз Дарвин')

    def test_3_Update(self):
        update = self.obj.update()
        self.assertEqual(update.status_code, 200)
        self.assertEqual(update.json()['title'], 'Война миров')
        self.assertEqual(update.json()['author'], 'Герберт Уэллс')

    def test_4_Delete(self):
        delete = self.obj.delete()
        self.assertEqual(delete.status_code, 204)
        get_deleted = requests.get()


myTestSuit = unittest.TestLoader().loadTestsFromTestCase(TestCrud)


if __name__ == "__main__":
    from HtmlTestRunner import HTMLTestRunner
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output=r"E:\workspace\test_test"))
    # unittest.main()

