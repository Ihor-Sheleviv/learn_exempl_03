import unittest
import os
from save_data import save_data, WrongFileData


PATH_FILE = '.\\data'
FILE_DATA = 'goods.dat' # файл з товарами
FILE_BK = 'goods.dbk'  # резервна копія
# дані у резервному файлі
goods_old = [['good 1', 10.00, 17], ['good 2', 12.00, 30],
             ['good 3', 10.20, 24], ['good 4', 10.04, 18]]
# дані в основному файлі
goods_data = [['good 1', 10.00, 10], ['good 2', 12.00, 29],
              ['good 3', 10.20, 24], ['good 4', 10.04, 12]]
# нові дані
goods = [['good 1', 10.00, 9],  ['good 2', 12.00, 29],
         ['good 3', 10.20, 20], ['good 4', 10.04, 12]]

class TestSaveDataCase(unittest.TestCase):
    """  збереження даних про товари    """
    def setUp(cls):
        """Create test data in files"""
        with open(PATH_FILE+'\\'+FILE_BK, 'w') as f:
            f.write(str(goods_old))
        with open(PATH_FILE + '\\' + FILE_DATA, 'w') as f:
            f.write(str(goods_data))

    def tearDown(cls):
        """Delete files of test"""
        if os.access(PATH_FILE + '\\' + FILE_BK, os.F_OK):
            os.remove(PATH_FILE+'\\'+FILE_BK)
        if os.access(PATH_FILE + '\\' + FILE_DATA, os.F_OK):
            os.remove(PATH_FILE + '\\' + FILE_DATA)

    def test_zero_zero(self):
        """ коли список товарів пустий """
        # тоді функція нічого не робить
        goods = []
        a = save_data(goods, PATH_FILE, FILE_DATA)
        self.assertEqual(a, -1, 'Not -1 code for zero goods')

        # перевіряємо чи є файл даних і що в ньому
        fd = os.access(PATH_FILE+'\\'+FILE_DATA, os.F_OK)
        self.assertTrue(fd, 'Not data file!')
        with open(PATH_FILE+'\\'+FILE_DATA, 'r') as f:
            self.assertMultiLineEqual(str(goods_data), f.read(), 'Data not true')
        # перевіряємо чи є резервний файл і що в ньому
        fb = os.access(PATH_FILE + '\\' + FILE_BK, os.F_OK)
        self.assertTrue(fb, 'Not backup file!')
        with open(PATH_FILE + '\\' + FILE_BK, 'w') as f:
            self.assertMultiLineEqual(str(goods_old), f.read(), 'BackUp not true')

    def test_no_file_data(self):
        """ коли файла з даними нема """
        # генеруємо виключення WrongFileData
        os.remove(PATH_FILE + '\\' + FILE_DATA)
        with self.assertRaises(WrongFileData) as ex:
            a = save_data(goods, PATH_FILE, FILE_DATA)
        self.assertEqual(ex.message, 'The machine does not work. Contact this admin!')

    def test_err_wr_data(self):
        """ коли файл даних не пишеться """
        # вивалюємося? "
        with open(PATH_FILE + '\\' + FILE_BK,'w') as f:
            with self.assertRaises(WrongFileData) as ex:
                a = save_data(goods, PATH_FILE, FILE_DATA)
            self.assertEqual(ex.message, 'The machine does not work. Contact this admin!')

    def test_err_data_bk(self):
        """ коли не перейменовується в резервний """
        # вивалюємося? "
        with open(PATH_FILE + '\\' + FILE_BK,'w') as f:
            with self.assertRaises(WrongFileData) as ex:
                a = save_data(goods, PATH_FILE, FILE_DATA)
            self.assertEqual(ex.message, 'The machine does not work. Contact this admin!')

    def test_normal(self):
        """ нормальна ситуація """
        # перейменовуємо файл даних у резервний, записуємо дані в основний
        a = save_data(goods, PATH_FILE, FILE_DATA)
        self.assertEqual(a, 0)

        # перевіряємо чи є файл даних і що в ньому
        fd = os.access(PATH_FILE+'\\'+FILE_DATA, os.F_OK)
        self.assertTrue(fd, 'Not data file!')
        with open(PATH_FILE+'\\'+FILE_DATA, 'r') as f:
            self.assertMultiLineEqual(str(goods), f.read(), 'Data not true')
        # перевіряємо чи є резервний файл і що в ньому
        fb = os.access(PATH_FILE + '\\' + FILE_BK, os.F_OK)
        self.assertTrue(fb, 'Not backup file!')
        with open(PATH_FILE + '\\' + FILE_BK, 'w') as f:
            self.assertMultiLineEqual(str(goods_data), f.read(), 'BackUp not true')


if __name__ == '__main__':
    unittest.main()