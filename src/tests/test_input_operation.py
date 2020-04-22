import unittest
import sys
from io import StringIO

from input_operation import input_operation

class TestInputUserCase(unittest.TestCase):
    """ Тестування уведення даних користувачем """

    def setUp(self):
        """ Перенаправимо стандартний вивід у змінну mystdout"""

        self.old_stdin = sys.stdin
        self.old_stdout = sys.stdout
        sys.stdout = self.mystdout = StringIO()

    def tearDown(self):
        """ Повернемо стандартний вивід і вивід на місце """
        sys.stdout = self.old_stdout
        sys.stdin = self.old_stdin

    def test_break(self):
        """ тестування виходу break """
        f = StringIO('0\n\n')
        sys.stdin = f
        out = input_operation()
        f.close()
        text = self.mystdout.getvalue()
        self.assertListEqual(out, [-1, 0, 0])
        self.assertEqual(text, 'Enter item number and key Enter or '
                               'Enter - continue or zero - break ' )

    def test_continue(self):
        """ тестування завершення Enter"""
        f = StringIO('\n\n')
        sys.stdin = f
        out = input_operation()
        f.close()
        text = self.mystdout.getvalue()
        self.assertListEqual(out, [1, 0, 0])
        self.assertEqual(text, 'Enter item number and key Enter or '
                               'Enter - continue or zero - break ')

    def test_choice(self):
        """ тестування правильного вибору"""
        f = StringIO('3\n2\n')
        sys.stdin = f
        out = input_operation()
        f.close()
        text = self.mystdout.getvalue()
        self.assertListEqual(out, [0, 3, 2])
        self.assertEqual(text, 'Enter item number and key Enter or '
                               'Enter - continue or zero - break ' 
                               'Enter quantity of goods and key Enter')

    def test_choice_error(self):
        """ тестування неправильного вибору номеру"""
        f = StringIO('##\n\n')
        sys.stdin = f
        out = input_operation()
        f.close()
        text = self.mystdout.getvalue()
        self.assertListEqual(out, [2, 0, 0])
        self.assertEqual(text, 'Enter item number and key Enter or '
                               'Enter - continue or zero - break ')

    def test_quantity_error(self):
        """ тестування неправильного вибору кількості"""
        f = StringIO('1\n##\n')
        sys.stdin = f
        out = input_operation()
        f.close()
        text = self.mystdout.getvalue()
        self.assertListEqual(out, [3, 0, 0])
        self.assertEqual(text, 'Enter item number and key Enter or '
                               'Enter - continue or zero - break ' 
                               'Enter quantity of goods and key Enter')

if __name__ == '__main__':
    unittest.main()
