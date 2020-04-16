import unittest
import sys
from io import StringIO
from display_info import display_info

class DisplaySimpleTestCase(unittest.TestCase):
    """ Тестування простого текстового виводу """
    def setUp(self):
        """ Перенаправимо стандартний вивід у змінну mystdout"""
        self.maxDiff = 2000
        self.old_stdout = sys.stdout
        sys.stdout = self.mystdout = StringIO()

    def tearDown(self):
        """ Повернемо стандартний вивід на місце """
        sys.stdout = self.old_stdout
        self.maxDiff = None

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
        a = display_info(goods, [])
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

class DisplayChoiceTestCase(unittest.TestCase):
    """ Тестування простого текстового виводу """
    def setUp(self):
        """ Перенаправимо стандартний вивід у змінну mystdout"""
        self.maxDiff = 3000
        self.old_stdout = sys.stdout
        sys.stdout = self.mystdout = StringIO()

    def tearDown(self):
        """ Повернемо стандартний вивід на місце """
        sys.stdout = self.old_stdout
        self.maxDiff = None

    def test_one_one(self):
        """ Один товар один вибір"""
        kadr = ' N|    goods                | num | price |choice|  value  \n' + \
               ' 1| goods                   |    5|  10.00|     2|    20.00\n' + \
               '  |                         |     |       |      |         \n'*24 + \
               '                                     Cost |           20.00\n' + \
               '                                                           \n'
        goods = [['goods ', 10.0, 5]]
        choice = [['goods ', 2]]
        a = display_info(goods, choice)
        text = self.mystdout.getvalue()
        self.assertMultiLineEqual(text, kadr)

    def test_25_4(self):
        """ 25 товарів 4 обраних"""
        good25 = [['good ' + str(i), 10.23 + i, 5 + i] for i in range(1, 26)]
        good25[1][0] = 'good 1234567890123456789'
        good25[1][1] = 9999.99
        good25[1][2] = 99998
        good25[4][2] = 7
        good25[9][2] = 14
        good25[24][2] = 28
        kadr = ' N|    goods                | num | price |choice|  value  \n' + \
               ' 1| good 1                  |    6|  11.23|      |         \n' + \
               ' 2| good 1234567890123456789|99998|9999.99|     1|  9999.99\n' + \
               ' 3| good 3                  |    8|  13.23|      |         \n' + \
               ' 4| good 4                  |    9|  14.23|      |         \n' + \
               ' 5| good 5                  |    7|  15.23|     3|    45.69\n' + \
               ' 6| good 6                  |   11|  16.23|      |         \n' + \
               ' 7| good 7                  |   12|  17.23|      |         \n' + \
               ' 8| good 8                  |   13|  18.23|      |         \n' + \
               ' 9| good 9                  |   14|  19.23|      |         \n' + \
               '10| good 10                 |   14|  20.23|     1|    20.23\n' + \
               '11| good 11                 |   16|  21.23|      |         \n' + \
               '12| good 12                 |   17|  22.23|      |         \n' + \
               '13| good 13                 |   18|  23.23|      |         \n' + \
               '14| good 14                 |   19|  24.23|      |         \n' + \
               '15| good 15                 |   20|  25.23|      |         \n' + \
               '16| good 16                 |   21|  26.23|      |         \n' + \
               '17| good 17                 |   22|  27.23|      |         \n' + \
               '18| good 18                 |   23|  28.23|      |         \n' + \
               '19| good 19                 |   24|  29.23|      |         \n' + \
               '20| good 20                 |   25|  30.23|      |         \n' + \
               '21| good 21                 |   26|  31.23|      |         \n' + \
               '22| good 22                 |   27|  32.23|      |         \n' + \
               '23| good 23                 |   28|  33.23|      |         \n' + \
               '24| good 24                 |   29|  34.23|      |         \n' + \
               '25| good 25                 |   28|  35.23|     2|    70.46\n' + \
               '                                     Cost |        10145.37\n' + \
               ' Thank you for your purchase                               \n'

        choice = [['good 1234567890123456789', 1],
                  ['good 5', 3], ['good 10', 1], ['good 25', 1]]

        display_info(good25,choice,warning='Thank you for your purchase' )
        text = self.mystdout.getvalue()
        self.assertMultiLineEqual(text, kadr)


if __name__ == '__main__':
    unittest.main()
