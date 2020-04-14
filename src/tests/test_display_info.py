import unittest
import sys
from io import StringIO
from display_info import display_info

class DisplaySimpleTestCase(unittest.TestCase):
    """ Тестування простого текстового виводу """
    def setUp(self):
        """ Перенаправимо стандартний вивід у змінну mystdout"""
        self.maxDiff = 1800
        self.old_stdout = sys.stdout
        sys.stdout = self.mystdout = StringIO()

    def tearDown(self):
        """ Повернемо стандартний вивід на місце """
        self.maxDiff = None
        sys.stdout = self.old_stdout

    def test_zero(self):
        """ Відсутні товари"""
        kadr = ' N|    goods                | num | price |choice|  value  \n' + \
               '  |                         |     |       |      |         \n'*25 + \
               '                                     Cost |                \n' + \
               ' NOT GOODS                                                 \n'
        display_info([],[])
        text = self.mystdout.getvalue()
        self.assertMultiLineEqual(text, kadr)

    def test_one(self):
        """ Один товар """
        kadr = ' N|    goods                | num | price |choice|  value  \n' + \
               ' 1| goods                   |    5|  10.00|      |         \n' + \
               '  |                         |     |       |      |         \n'*24 + \
               '                                     Cost |                \n' + \
               '                                                           \n'
        goods = [['goods ', 10.0, 5]]
        a = display_info([],[])
        text = self.mystdout.getvalue()
        self.assertMultiLineEqual(text, kadr)

    def test_25(self):
        """ 25 товарів """
        good25 = [['good ' + str(i), 10.23 + i, 5 + i] for i in range(1, 26)]
        good25[1][0] = 'good 1234567890123456789'
        good25[1][1] = 9999.99
        good25[1][2] = 99999
        kadr = ' N|    goods                | num | price |choice|  value  \n'
        n = 0
        for good, price, num in good25:
            n = n + 1
            kadr = kadr + f'{n:2}| {good:<24}|{num:5}|{price:7.2f}|      |         \n'

        kadr = kadr + '                                     Cost |                \n' + \
                      '                                                           \n'
        display_info(good25,[])
        text = self.mystdout.getvalue()
        self.assertMultiLineEqual(text, kadr)

if __name__ == '__main__':
    unittest.main()
