import unittest
from input_operation import input_operation


class MyTestCase(unittest.TestCase):
    def test_zero(self):
        a = input_operation()
        self.assertEqual(a, 0)


if __name__ == '__main__':
    unittest.main()
