import unittest
from pay import pay

class MyTestCase(unittest.TestCase):
    def test_zero(self):
        a = pay()
        self.assertEqual(a, 0)


if __name__ == '__main__':
    unittest.main()
