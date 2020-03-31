import unittest
from save_story import save_story

class MyTestCase(unittest.TestCase):
    def test_zero(self):
        a = save_story()
        self.assertEqual(a, 0)


if __name__ == '__main__':
    unittest.main()
