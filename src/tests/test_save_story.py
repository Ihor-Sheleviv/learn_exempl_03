import unittest
import os
import datetime
from unittest import mock
from save_story import save_story, WrongFileStory


def fake_write():
    raise IOError('IO')

def fake_copyfile():
    raise IOError('IO')


PATH_FILE = '.\\data'
FILE_DATA = 'story.dat'  # файл історії
FILE_BK = 'story.dbk'  # резервна копія

# дані у резервній копії не важливо що там
data_old = str([[['good 1', 10.00, 27], ['good 2', 12.00, 30],
                 ['good 3', 10.20, 30], ['good 4', 10.04, 20]],
                [['good 1', 3], ['good 3', 1]],
                [0, 4, 3]])
today = datetime.datetime.today()
data_old = today.strftime("%Y-%m-%d-%H.%M.%S") + ' ' + data_old + '\n'

# дані у файлі історії до запису
data = str([[['good 1', 10.00, 24], ['good 2', 12.00, 30],
             ['good 3', 10.20, 29], ['good 4', 10.04, 20]],
            [['good 1', 2], ['good 3', 1]], [0, 4, 2]])
today = datetime.datetime.today()
data = today.strftime("%Y-%m-%d-%H.%M.%S") + ' ' + data + '\n'

# поточні дані про товар
goods = [['good 1', 10.00, 17], ['good 2', 12.00, 30],
         ['good 3', 10.20, 24], ['good 4', 10.04, 18]]
# дані про вибір
choice = [['good 1', 1], ['good 3', 1]]
# дані про дії клієнта
code_out = [0, 4, 1]


class TestSaveStoryCase(unittest.TestCase):
    """  збереження історії дій    """

    def setUp(cls):
        """Create test data in files"""
        with open(PATH_FILE + '\\' + FILE_BK, 'w') as f:
            f.write(str(data_old))
        with open(PATH_FILE + '\\' + FILE_DATA, 'w') as f:
            f.write(str(data_old) + str(data))

    def tearDown(cls):
        """Delete files of test"""
        if os.access(PATH_FILE + '\\' + FILE_BK, os.F_OK):
            os.remove(PATH_FILE + '\\' + FILE_BK)
        if os.access(PATH_FILE + '\\' + FILE_DATA, os.F_OK):
            os.remove(PATH_FILE + '\\' + FILE_DATA)

    def test_err_wr_data(self):
        """ коли файл даних не пишеться """
        # вивалюємося? "

        with self.assertRaises(WrongFileStory) as ex:
            with mock.patch('save_story.my_write', fake_write):
                a = save_story(data, PATH_FILE, FILE_DATA)
        self.assertEqual(ex.exception.args[0],
                         'The machine does not work. Error 102. Contact this admin!')

    def test_err_data_bk(self):
        """ коли не перейменовується в резервний """
        # вивалюємося? "
        with open(PATH_FILE + '\\' + FILE_BK, 'w') as f:
            with self.assertRaises(WrongFileStory) as ex:
                with mock.patch('save_story.copyfile', fake_copyfile):
                    a = save_story(data, PATH_FILE, FILE_DATA)
            self.assertEqual(ex.exception.args[0],
                             'The machine does not work. Error 101. Contact this admin!')

    def test_normal(self):
        """ нормальна ситуація """
        # перейменовуємо файл даних у резервний, записуємо дані в основний

        # що передаємо у функцію запису
        data_new = [goods, choice, code_out]
        # те що має бути записане у файлі історії
        today = datetime.datetime.today()
        date_new = today.strftime("%Y-%m-%d-%H.%M.%S")
        data_str = [ data_old, data, date_new + ' ' + str(data_new) + '\n']

        # записуємо історію
        a = save_story(data_new, PATH_FILE, FILE_DATA)
        self.assertEqual(a, 0)

        # перевіряємо чи є файл даних і що в ньому
        fd = os.access(PATH_FILE + '\\' + FILE_DATA, os.F_OK)
        self.assertTrue(fd, 'Not data file!')
        with open(PATH_FILE + '\\' + FILE_DATA, 'r') as f:
            #
            data_lines = f.readlines()
            self.assertListEqual(data_str, data_lines, 'Data not true')

        # перевіряємо чи є резервний файл і що в ньому
        fb = os.access(PATH_FILE + '\\' + FILE_BK, os.F_OK)
        self.assertTrue(fb, 'Not backup file!')
        with open(PATH_FILE + '\\' + FILE_BK, 'r') as f:
            data_lines = f.readlines()
            self.assertListEqual([data_old, data], data_lines, 'BackUp not true')

if __name__ == '__main__':
    unittest.main()

