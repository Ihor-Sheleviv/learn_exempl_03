import unittest
from display_info import display_info

class MyTestCase(unittest.TestCase):
    def test_zero(self):
        a = display_info()
        self.assertEqual(a, 0)


if __name__ == '__main__':
    unittest.main()
