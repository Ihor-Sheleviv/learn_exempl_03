import unittest

from load_data import load_data


class MyTestCase(unittest.TestCase):
    def test_zero(self):
        a = load_data()
        self.assertEqual(a, 0)


if __name__ == '__main__':
    unittest.main()
