import unittest
from calculation import calculation

class MyTestCase(unittest.TestCase):
    def test_zero(self):
        a = calculation()
        self.assertEqual(a, 0)


if __name__ == '__main__':
    unittest.main()
