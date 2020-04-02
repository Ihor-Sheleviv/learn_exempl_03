"""
файл із вказаним іменем відсутній;
файл із вказаним іменем порожній;
у файлі пустий список;
у файлі у списку помилка у структурі списку;
список з одним товаром;
список з чотирма товарами;
список із 25 товарами;
список із 26 товарами.
"""
import unittest
import os

from load_data import load_data


class LoadDataCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Create test data in files"""
        with open('.\\data\\empty.txt', 'w') as f:
            f.write("")
        with open('.\\data\\zero.txt', 'w') as f:
            f.write("[]")
        with open('.\\data\\listerror.txt', 'w') as f:
            f.write("[['good1'")
        with open('.\\data\\incorrect.txt', 'w') as f:
            f.write("[[good1]]")
        with open('.\\data\\onegood.txt', 'w') as f:
            f.write("[['good 1',10.00,20]]")
        with open('.\\data\\fourgoods.txt', 'w') as f:
            f.write("[['good 1',10.00,20],['good 2',12.00,30],"
                      "['good 3',10.20,25],['good 4',10.04,08],]")
        good25 = [['good '+str(i),10.23+i,5+i] for i in range(1,26)]
        with open('.\\data\\twentyfive.txt', 'w') as f:
            f.write(str(good25))
        good26 = [['good '+str(i),10.23+i,5+i] for i in range(1,27)]
        with open('.\\data\\twentysix.txt', 'w') as f:
            f.write(str(good26))

    @classmethod
    def tearDownClass(cls):
        """Delete files of test"""
        os.remove('.\\data\\empty.txt')
        os.remove('.\\data\\zero.txt')
        os.remove('.\\data\\listerror.txt')
        os.remove('.\\data\\incorrect.txt')
        os.remove('.\\data\\onegood.txt')
        os.remove('.\\data\\fourgoods.txt')
        os.remove('.\\data\\twentyfive.txt')
        os.remove('.\\data\\twentysix.txt')

    def test_dir(self):
        """ Вказана тека відсутня """
        a = load_data('.\\none','none.txt')
        self.assertListEqual(a, [1,[]])

    def test_notfile(self):
        """ Вказаний файл відсутній """
        a = load_data('.\\data','none.txt')
        self.assertListEqual(a, [2,[]])

    def test_empty_file(self):
        """ Вказаний файл пустий """
        a = load_data('.\\data', 'empty.txt')
        self.assertListEqual(a, [3, []])

    def test_zero_file(self):
        """ Вказаний файл має пустий список """
        a = load_data('.\\data', 'zero.txt')
        self.assertListEqual(a, [4, []])

    def test_error_list(self):
        """ Вказаний містить помилковий список (синтаксис) """
        a = load_data('.\\data', 'listerror.txt')
        self.assertListEqual(a, [5, []])

    def test_incorrect_list(self):
        """ Вказаний містить невірний список (не синтаксис) """
        a = load_data('.\\data', 'incorrect.txt')
        self.assertListEqual(a, [6, []])

    def test_onegood(self):
        """ містить один товар """
        a = load_data('.\\data', 'onegood.txt')
        self.assertListEqual(a, [0, [['good 1',10.00,20]]])

    def test_fourgoods(self):
        """ містить чотири товари """
        a = load_data('.\\data', 'fourgoods.txt')
        self.assertListEqual(a, [0, [['good 1',10.00,20],['good 2',12.00,30],
                                     ['good 3',10.20,25],['good 4',10.04, 8],]])

    def test_twentyfive(self):
        """ містить 25 товари """
        good25 = [['good ' + str(i), 10.23 + i, 5 + i] for i in range(1, 26)]
        a = load_data('.\\data', 'twentyfive.txt')
        self.assertListEqual(a, [0, good25])

    def test_twentyfive(self):
        """ містить 25 товари """
        good26 = [['good ' + str(i), 10.23 + i, 5 + i] for i in range(1, 27)]
        a = load_data('.\\data', 'twentyfive.txt')
        self.assertListEqual(a, [26, good26])


if __name__ == '__main__':
    unittest.main()
