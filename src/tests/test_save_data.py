import unittest
from save_data import save_data


class MyTestCase(unittest.TestCase):
    def test_zero(self):
        a = save_data()
        self.assertEqual(a, 0)


if __name__ == '__main__':
    unittest.main()
