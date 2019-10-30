from crud import crud
import unittest
import requests

class TestCrud(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.obj = crud()

    def testCreate(self):
        self.obj.create()
    # def create(self):
    #     create = requests.post(self.base_url + 'books/', self.book_data1)
    #     self.book_id = create.json()['id']
    #     return create.json()
        test_create = requests.post(self.obj.base_url + 'books/', self.obj.book_data1)
        self.assertCountEqual(test_create.json(), self.obj.create())

if __name__ == "__main__":
     from HtmlTestRunner import HTMLTestRunner
     unittest.main(verbosity=2, testRunner=HTMLTestRunner(output=r"d:/reps/"))

    # import unittest
    # from first import Employee
    # import sys

    # class OurTestClass(unittest.TestCase):
    #     def test_1(self):
    #         data = [1, 2, 3, 4, 5]
    #         for i in data:
    #             with self.subTest(i):
    #                 print(i)
    #                 res = i % 2
    #                 self.assertEqual(1, res)
    #
    #     @unittest.skipIf(sys.platform.startswith("win"), reason="Не запускается на Windows")
    #     def test_2(self):
    #         # 1st way
    #         with self.assertRaises(TypeError):
    #             Employee("Vasya P", year=0)
    #         # 2nd way
    #         # self.assertRaises(TypeError, Employee, "O p", 1200)
    #
    # class TestClass(unittest.TestCase):
    #     @classmethod
    #     def setUpClass(cls) -> None:
    #         cls._commonattribut = "bla"
    #         print("\nsetUpClass")
    #
    #     @classmethod
    #     def tearDownClass(cls) -> None:
    #         print("\ntearDownClass")
    #
    #     def setUp(self):
    #         print("\nsetup of", self)
    #
    #     def tearDown(self) -> None:
    #         print("\ntearDown", self)
    #
    #     def test_1(self):
    #         print(self._commonattribut)
    #         print("\ntest_1", self)
    #
    #     def test_2(self):
    #         print("\ntest_2", self)
    #
    # myTestSuit = unittest.TestLoader().loadTestsFromTestCase(OurTestClass)
    #
    # if __name__ == "__main__":
    #     from HtmlTestRunner import HTMLTestRunner
    #     unittest.main(verbosity=2, testRunner=HTMLTestRunner(output=r"E:\workspace\test_test"))